import Badge from "./Badge";
import Button from "./Button";

type Project = {
  title: string;
  tag: string;
  description: string;
  stack: string[];
  bullets: string[];
  links: { live: string; code: string };
};

export default function ProjectCard({ project }: { project: Project }) {
  return (
    <div className="glass rounded-3xl p-6 md:p-7 shadow-soft">
      <div className="flex items-start justify-between gap-4">
        <div>
          <p className="text-lg font-semibold">{project.title}</p>
          <p className="mt-1 text-zinc-400">{project.description}</p>
        </div>
        <Badge>{project.tag}</Badge>
      </div>

      <div className="mt-4 flex flex-wrap gap-2">
        {project.stack.map((s) => (
          <Badge key={s} variant="subtle">{s}</Badge>
        ))}
      </div>

      <ul className="mt-5 list-disc pl-5 space-y-2 text-zinc-300">
        {project.bullets.map((b) => (
          <li key={b}>{b}</li>
        ))}
      </ul>

      <div className="mt-6 flex flex-col sm:flex-row gap-3">
        <Button href={project.links.live} external>Live Demo</Button>
        <Button href={project.links.code} external variant="ghost">Code</Button>
      </div>
    </div>
  );
}
