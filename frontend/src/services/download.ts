import api from './api';

/** Download a stored file: streams local files as a blob download,
 *  opens S3 presigned URLs in a new tab (keeps auth header off the signed GET). */
export async function downloadFile(key: string): Promise<void> {
  const r = await api.get('/api/v1/files', { params: { key }, responseType: 'blob' });
  const ct: string = (r.headers['content-type'] as string) || '';
  if (ct.includes('application/json')) {
    const txt = await (r.data as Blob).text();
    window.open((JSON.parse(txt) as { url: string }).url, '_blank', 'noopener');
    return;
  }
  const url = URL.createObjectURL(r.data as Blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = key.split('/').pop() || 'download';
  document.body.appendChild(a);
  a.click();
  a.remove();
  setTimeout(() => URL.revokeObjectURL(url), 5000);
}
