import { test, expect, request as apiRequest } from '@playwright/test';

const API = 'http://127.0.0.1:8000';
const ADMIN = { email: 'admin@urbaneyes.city', password: 'Admin123!' };
const OFFICER = { email: 'officer@urbaneyes.city', password: 'Officer123!' };

async function apiLogin(email: string, password: string) {
  const ctx = await apiRequest.newContext();
  const r = await ctx.post(`${API}/api/v1/auth/login`, { data: { email, password } });
  if (!r.ok()) throw new Error(`API login failed for ${email}: ${r.status()}`);
  const tokens = await r.json();
  const me = await ctx.get(`${API}/api/v1/auth/me`,
    { headers: { Authorization: `Bearer ${tokens.access_token}` } });
  const user = await me.json();
  await ctx.dispose();
  return { tokens, user };
}

async function signIn(page: any, email: string, password: string, shots: string) {
  await page.goto('/login');
  await page.getByPlaceholder('Email').fill(email);
  await page.getByPlaceholder('Password').fill(password);
  await page.getByRole('button', { name: /sign in to command center/i }).click();
  await expect(page).not.toHaveURL(/login/, { timeout: 15000 });
  await page.screenshot({ path: `e2e/screenshots/${shots}-login.png` });
}

test('full municipal flow: admin analyze → request → officer resolve → admin verify', async ({ page }, testInfo) => {
  const tag = testInfo.project.name;
  const errors: string[] = [];
  page.on('pageerror', (e) => errors.push(`pageerror: ${e.message}`));
  page.on('console', (m) => {
    if (m.type() === 'error') errors.push(`console: ${m.text().slice(0, 200)}`);
  });

  // ---- Admin: login + dashboard ----
  await signIn(page, ADMIN.email, ADMIN.password, tag);
  await expect(page.getByRole('heading', { name: /city operations command/i })).toBeVisible();
  await expect(page.getByText(/monitored streets/i).first()).toBeVisible();
  await page.screenshot({ path: `e2e/screenshots/${tag}-admin-dashboard.png` });

  // ---- Street analysis: upload + run + result ----
  // Isolated street per project so parallel/sequential runs never share analyses.
  const setupCtx = await apiRequest.newContext();
  const { tokens: adminTok } = await apiLogin(ADMIN.email, ADMIN.password);
  const streetList = await (await setupCtx.get(`${API}/api/v1/streets`,
    { headers: { Authorization: `Bearer ${adminTok.access_token}` } })).json();
  await setupCtx.dispose();
  const streetId = (tag === 'desktop' ? streetList[0] : streetList[1]).id;
  await page.goto(`/admin/streets?street=${streetId}`);
  await expect(page.getByRole('heading', { name: /street analysis/i })).toBeVisible();
  await page.locator('input[type="file"]').setInputFiles('e2e/fixtures/street.mp4');
  await expect(page.getByText('street.mp4', { exact: false }).first()).toBeVisible({ timeout: 20000 });
  await page.getByRole('button', { name: /run street analysis/i }).click();
  // Wait for THIS run: busy indicator appears, then disappears when the new analysis lands.
  // (Never match a stale "AI explanation" card from previous runs.)
  await expect(page.getByText(/analyzing…/i).first()).toBeVisible({ timeout: 20000 });
  await expect(page.getByText(/analyzing…/i).first()).toBeHidden({ timeout: 120000 });
  // Reload so the rendered card is guaranteed to be API truth (newest analysis),
  // not any in-flight client state — then submit from that card.
  await page.reload();
  await expect(page.getByText(/ai explanation/i)).toBeVisible({ timeout: 20000 });
  await expect(page.getByText(/recommended municipal action/i)).toBeVisible();
  await page.screenshot({ path: `e2e/screenshots/${tag}-analysis.png` });

  // ---- Critical confirmation gate → municipal request ----
  await page.getByRole('button', { name: /submit municipal request/i }).click();
  await expect(page.getByText(/confirm municipal request/i)).toBeVisible();
  await page.getByRole('button', { name: /confirm & submit request/i }).click();
  try {
    await expect(page).toHaveURL(/requests\/\d+/, { timeout: 15000 });
  } catch {
    const banner = await page.locator('body').innerText();
    console.log(`SUBMIT-DEBUG url=${page.url()} banner=${banner.slice(0, 500)}`);
    throw new Error('submit did not navigate; see SUBMIT-DEBUG above');
  }
  const code = (await page.locator('h1').first().innerText()).trim();
  expect(code).toMatch(/UE-\d{4}-\d{4}/);
  await page.screenshot({ path: `e2e/screenshots/${tag}-request.png` });

  // ---- Officer: queue → lifecycle ----
  await page.getByRole('button', { name: /sign out/i }).click();
  await signIn(page, OFFICER.email, OFFICER.password, `${tag}-officer`);
  await expect(page.getByRole('heading', { name: /what needs my attention/i })).toBeVisible();
  await page.getByRole('link', { name: /queue/i }).first().click();
  await page.getByRole('link', { name: code }).first().click();
  await expect(page.getByText(code).first()).toBeVisible();

  await page.getByRole('button', { name: 'under review', exact: true }).click();
  await expect(page.getByText('UNDER REVIEW').first()).toBeVisible({ timeout: 15000 });
  await page.getByRole('button', { name: 'accepted', exact: true }).click();
  await expect(page.getByText('ACCEPTED').first()).toBeVisible({ timeout: 15000 });

  const { user: officer } = await apiLogin(OFFICER.email, OFFICER.password);
  await page.getByPlaceholder('Officer user ID').fill(String(officer.id));
  await page.getByRole('button', { name: 'Assign', exact: true }).click();
  await expect(page.getByText('ASSIGNED').first()).toBeVisible({ timeout: 15000 });

  await page.getByRole('button', { name: 'in progress', exact: true }).click();
  await expect(page.getByText('IN PROGRESS').first()).toBeVisible({ timeout: 15000 });

  await page.locator('label', { hasText: 'Upload after image' }).locator('input')
    .setInputFiles('e2e/fixtures/after.png');
  await expect(page.getByText(/after · /).first()).toBeVisible({ timeout: 15000 });
  await page.getByRole('button', { name: /mark resolved/i }).click();
  await expect(page.getByText('RESOLVED').first()).toBeVisible({ timeout: 15000 });
  await page.screenshot({ path: `e2e/screenshots/${tag}-resolved.png` });

  // ---- Admin verifies final state + notifications ----
  await page.getByRole('button', { name: /sign out/i }).click();
  await signIn(page, ADMIN.email, ADMIN.password, `${tag}-admin2`);
  await page.goto('/admin/notifications');
  await expect(page.getByText(/resolved/i).first()).toBeVisible({ timeout: 15000 });
  await page.screenshot({ path: `e2e/screenshots/${tag}-notifications.png` });

  expect(errors).toEqual([]);
});
