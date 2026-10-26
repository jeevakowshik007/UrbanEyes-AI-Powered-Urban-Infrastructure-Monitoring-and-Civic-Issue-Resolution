import { Link } from 'react-router-dom';
import { GlassCard, Stage } from '../components/ui';

const QA: [string, string][] = [
  ['What is UrbanEyes?', 'An AI-assisted urban infrastructure platform. It watches recorded street videos with computer vision (YOLO26-Seg), explains findings with the built-in UrbanEyes Infrastructure Reasoning engine, and routes confirmed issues to municipal officers through an auditable request lifecycle.'],
  ['How does street analysis work?', 'Pick a street with recorded video → the backend validates the video, samples frames, runs YOLO26-Seg, aggregates evidence into weak/medium/critical severities, then the local reasoning engine explains the result and recommends a municipal action. No external AI service is involved.'],
  ['Do critical results auto-submit requests?', 'Never. A critical result opens a confirmation dialog. An administrator must explicitly review the evidence and choose “Submit Municipal Request”.'],
  ['What do weak / medium / critical mean?', 'The only three severity levels. Weak: routine monitoring. Medium: schedule maintenance. Critical: prioritize inspection and repair. Category severities (road, waste, drainage, infrastructure) show where the problem sits.'],
  ['How does the officer workflow go?', 'Pending → Under review → Accepted → Assigned → In progress → Resolved (or Rejected with a reason). Every transition is recorded with actor and timestamp. Resolving requires uploading repair evidence.'],
  ['Where do my videos and images go?', 'To S3-compatible storage in production (local disk in dev). Only validated video and image files are accepted, with strict size caps.'],
];

export default function Faq() {
  return (
    <Stage>
      <h1 className="font-display text-2xl font-bold">FAQ</h1>
      <div className="space-y-3">
        {QA.map(([q, a]) => (
          <GlassCard key={q}>
            <div className="font-semibold text-sm">{q}</div>
            <p className="text-sm text-slate-600 mt-1 leading-relaxed">{a}</p>
          </GlassCard>
        ))}
      </div>
      <Link to="/login" className="text-sm text-delft underline">Back to sign in</Link>
    </Stage>
  );
}
