import Container from "@/components/Container";
import SectionHeading from "@/components/SectionHeading";
import Button from "@/components/Button";
import Badge from "@/components/Badge";
import ProjectCard from "@/components/ProjectCard";
import { site } from "@/data/site";

export default function Home() {
  return (
    <main>
      <section id="top" className="relative overflow-hidden">
        <div className="pointer-events-none absolute inset-0">
          <div className="absolute -top-40 left-1/2 h-[520px] w-[520px] -translate-x-1/2 rounded-full blur-3xl opacity-40 bg-gradient-to-r from-indigo-500 via-fuchsia-500 to-cyan-400 animate-shimmer" />
          <div className="absolute top-24 right-10 h-44 w-44 rounded-full blur-2xl opacity-30 bg-gradient-to-r from-emerald-400 to-cyan-400 animate-floaty" />
        </div>

        <Container className="relative pt-24 pb-10 md:pt-28">
          <div className="glass rounded-3xl shadow-soft p-6 md:p-10">
            <div className="flex flex-col gap-6 md:gap-8">
              <div className="flex flex-wrap items-center gap-2">
                <Badge>{site.roleTag}</Badge>
                <Badge variant="subtle">{site.gradTag}</Badge>
                <Badge variant="subtle">Open to SWE • Backend • Data</Badge>
              </div>

              <div className="space-y-4">
                <h1 className="text-4xl md:text-6xl font-semibold tracking-tight">
                  {site.name}
                  <span className="block text-zinc-300 mt-2 text-2xl md:text-3xl font-medium">
                    {site.headline}
                  </span>
                </h1>
                <p className="max-w-2xl text-zinc-300 leading-relaxed">
                  {site.summary}
                </p>
              </div>

              <div className="flex flex-col sm:flex-row gap-3">
                <Button href={site.links.resume} external>
                  View Resume
                </Button>
                <Button href={site.links.github} external variant="ghost">
                  GitHub
                </Button>
                <Button href={site.links.linkedin} external variant="ghost">
                  LinkedIn
                </Button>
              </div>

              <div className="flex flex-wrap gap-2 pt-2">
                {site.topSkills.map((s) => (
                  <Badge key={s} variant="subtle">
                    {s}
                  </Badge>
                ))}
              </div>
            </div>
          </div>

          <div className="mt-10 grid grid-cols-1 md:grid-cols-3 gap-4">
            {site.quickStats.map((q) => (
              <div key={q.title} className="glass rounded-2xl p-5">
                <p className="text-sm text-zinc-400">{q.title}</p>
                <p className="mt-2 text-lg font-medium">{q.value}</p>
              </div>
            ))}
          </div>
        </Container>
      </section>

      <section id="about" className="py-14">
        <Container>
          <SectionHeading title="About" subtitle="A quick snapshot of what I build and what I’m looking for." />
          <div className="glass rounded-3xl p-6 md:p-8">
            <p className="text-zinc-300 leading-relaxed">{site.about}</p>
          </div>
        </Container>
      </section>

      <section id="skills" className="py-14">
        <Container>
          <SectionHeading title="Skills" subtitle="Tools I use to ship real projects." />
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {site.skillGroups.map((g) => (
              <div key={g.label} className="glass rounded-3xl p-6">
                <p className="text-zinc-200 font-medium">{g.label}</p>
                <div className="mt-4 flex flex-wrap gap-2">
                  {g.items.map((it) => (
                    <Badge key={it} variant="subtle">{it}</Badge>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </Container>
      </section>

      <section id="projects" className="py-14">
        <Container>
          <SectionHeading title="Projects" subtitle="Featured work — deployed, practical, and built for real use." />
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-5">
            {site.projects.map((p) => (
              <ProjectCard key={p.title} project={p} />
            ))}
          </div>
        </Container>
      </section>

      <section id="experience" className="py-14">
        <Container>
          <SectionHeading title="Experience" subtitle="Hands-on work and leadership." />
          <div className="space-y-4">
            {site.experience.map((e) => (
              <div key={e.company + e.title} className="glass rounded-3xl p-6 md:p-8">
                <div className="flex flex-col md:flex-row md:items-start md:justify-between gap-2">
                  <div>
                    <p className="text-lg font-medium">{e.title}</p>
                    <p className="text-zinc-400">{e.company} • {e.location}</p>
                  </div>
                  <p className="text-zinc-400">{e.dates}</p>
                </div>
                <ul className="mt-4 list-disc pl-5 space-y-2 text-zinc-300">
                  {e.bullets.map((b) => (<li key={b}>{b}</li>))}
                </ul>
              </div>
            ))}
          </div>
        </Container>
      </section>

      <section id="education" className="py-14">
        <Container>
          <SectionHeading title="Education" subtitle="Degree + relevant coursework." />
          <div className="glass rounded-3xl p-6 md:p-8">
            <div className="flex flex-col md:flex-row md:items-start md:justify-between gap-2">
              <div>
                <p className="text-lg font-medium">{site.education.school}</p>
                <p className="text-zinc-400">{site.education.degree}</p>
              </div>
              <p className="text-zinc-400">{site.education.grad}</p>
            </div>
            <div className="mt-4 flex flex-wrap gap-2">
              {site.education.courses.map((c) => (
                <Badge key={c} variant="subtle">{c}</Badge>
              ))}
            </div>
          </div>
        </Container>
      </section>

      <section id="contact" className="py-14 pb-20">
        <Container>
          <SectionHeading title="Contact" subtitle="Let’s connect — I respond fast." />
          <div className="glass rounded-3xl p-6 md:p-8 flex flex-col md:flex-row md:items-center md:justify-between gap-6">
            <div>
              <p className="text-zinc-300">
                Email me at{" "}
                <a className="underline decoration-white/20 hover:decoration-white/60" href={`mailto:${site.email}`}>
                  {site.email}
                </a>
              </p>
              <p className="text-zinc-400 mt-2">Or reach me on GitHub / LinkedIn.</p>
            </div>
            <div className="flex flex-col sm:flex-row gap-3">
              <Button href={`mailto:${site.email}`}>Email</Button>
              <Button href={site.links.github} external variant="ghost">GitHub</Button>
              <Button href={site.links.linkedin} external variant="ghost">LinkedIn</Button>
            </div>
          </div>
        </Container>
      </section>
    </main>
  );
}
