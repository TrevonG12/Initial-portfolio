# make_portfolio.py
# Run this INSIDE your Next.js project root (where package.json is).
# It will create/overwrite the modern portfolio files (Next.js + Tailwind).

from pathlib import Path

ROOT = Path(".").resolve()

def write(rel_path: str, content: str):
    path = ROOT / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"Wrote: {rel_path}")

FILES = {
"src/app/globals.css": """@tailwind base;
@tailwind components;
@tailwind utilities;

:root { color-scheme: dark; }

html, body { height: 100%; }

body { @apply bg-zinc-950 text-zinc-100 antialiased; }

::selection { background: rgba(99, 102, 241, 0.35); }

a { @apply text-zinc-100; }

/* Modern subtle grid background */
.bg-grid {
  background-image:
    radial-gradient(circle at 1px 1px, rgba(255,255,255,0.08) 1px, transparent 0);
  background-size: 26px 26px;
}

/* Glass surface */
.glass {
  background: rgba(24, 24, 27, 0.55);
  border: 1px solid rgba(255,255,255,0.08);
  backdrop-filter: blur(10px);
}

/* Smooth anchor scrolling */
html { scroll-behavior: smooth; }

/* Nice focus ring */
:focus-visible {
  outline: 2px solid rgba(99, 102, 241, 0.75);
  outline-offset: 3px;
  border-radius: 10px;
}
""",

"src/app/layout.tsx": """import "./globals.css";
import type { Metadata } from "next";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";

export const metadata: Metadata = {
  title: "Trevon Griffin | CS Portfolio",
  description: "Computer Science major graduating May 2026. Full-stack & Python projects.",
  openGraph: {
    title: "Trevon Griffin | Portfolio",
    description: "Modern CS portfolio — projects, skills, experience.",
    images: ["/og.png"]
  }
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <div className="min-h-screen bg-grid">
          <Navbar />
          {children}
          <Footer />
        </div>
      </body>
    </html>
  );
}
""",

"src/app/page.tsx": """import Container from "@/components/Container";
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
""",

"src/data/site.ts": """export const site = {
  name: "Trevon Griffin",
  roleTag: "Computer Science",
  gradTag: "Graduating May 2026",
  headline: "Full-Stack • Python • Backend",
  summary:
    "I build clean, deployable web applications and backend systems. I’m focused on shipping practical software, writing maintainable code, and leveling up fast through real projects.",

  about:
    "Computer Science major graduating in May 2026. I’ve built and deployed a full-stack inventory and project management app, and I’m expanding my portfolio with additional projects in data, backend, and systems to be ready for internship and entry-level opportunities.",

  email: "trevongriffin88@gmail.com",

  links: {
    resume: "#",      // put your PDF in /public/resume.pdf then set to "/resume.pdf"
    github: "#",      // your GitHub
    linkedin: "#"     // your LinkedIn
  },

  topSkills: ["Python", "Flask", "MySQL", "HTML/CSS", "Java", "Git", "Deployments"],

  quickStats: [
    { title: "Featured Project", value: "Inventory & Project Management (Deployed)" },
    { title: "Primary Stack", value: "Flask + MySQL" },
    { title: "Currently Building", value: "2–3 projects for May grad portfolio" }
  ],

  skillGroups: [
    { label: "Languages", items: ["Python", "Java", "JavaScript (basic)"] },
    { label: "Frameworks & Tools", items: ["Flask", "MySQL", "HTML", "CSS", "Git", "Railway"] }
  ],

  projects: [
    {
      title: "Inventory & Project Management System",
      tag: "Featured • Deployed",
      description:
        "A full-stack web app to manage inventory items and project workflows behind secure authentication.",
      stack: ["Python", "Flask", "MySQL", "HTML/CSS", "Railway"],
      bullets: [
        "Built and deployed a full-stack Flask + MySQL application with authentication and protected routes",
        "Designed relational schemas to store inventory and project data",
        "Implemented full CRUD features to create, update, and track items/projects",
        "Deployed to production and configured environment/database connectivity"
      ],
      links: {
        live: "https://inventory-project-managament-production.up.railway.app/",
        code: "#"
      }
    },
    {
      title: "Data Dashboard (Coming Soon)",
      tag: "In Progress",
      description:
        "A Python analytics dashboard (data cleaning + visualization) to demonstrate data engineering fundamentals.",
      stack: ["Python", "pandas", "Streamlit"],
      bullets: [
        "Ingest and clean a real dataset",
        "Build interactive charts and filters",
        "Publish a live dashboard"
      ],
      links: { live: "#", code: "#" }
    },
    {
      title: "Mini Key-Value Store (Coming Soon)",
      tag: "In Progress",
      description:
        "A lightweight in-memory store with TTL and benchmarking to demonstrate systems + performance thinking.",
      stack: ["Python (or Go)", "Testing", "Benchmarks"],
      bullets: [
        "Implement core store operations and TTL expiration",
        "Add concurrency-safe access (optional)",
        "Benchmark read/write performance"
      ],
      links: { live: "#", code: "#" }
    }
  ],

  experience: [
    {
      title: "Tech Developer Intern",
      company: "Sponsors for Educational Opportunity",
      location: "Remote",
      dates: "Jul 2023 – Aug 2023",
      bullets: [
        "Completed 300+ hours of software engineering training focused on data structures, algorithms, and full-stack web development",
        "Designed and implemented full-stack apps using Python (Flask) and MySQL with HTML/CSS/JavaScript",
        "Collaborated in a mentorship program focused on professional growth and career readiness"
      ]
    },
    {
      title: "Web & Graphic Designer",
      company: "Campbellsville University",
      location: "Campbellsville, KY",
      dates: "Aug 2021 – Dec 2021",
      bullets: [
        "Created fundraising graphics and flyers using Adobe and Microsoft tools to support scholarship initiatives",
        "Iterated designs strategically to improve donor engagement"
      ]
    }
  ],

  education: {
    school: "Campbellsville University",
    degree: "B.S. Computer Science",
    grad: "Expected May 2026",
    courses: ["Intro to Programming (Java)", "Programming II (Java)", "Computer Concepts & Applications"]
  }
} as const;
""",

"src/components/Container.tsx": """export default function Container({
  children,
  className = ""
}: {
  children: React.ReactNode;
  className?: string;
}) {
  return (
    <div className={`mx-auto w-full max-w-6xl px-5 md:px-8 ${className}`}>
      {children}
    </div>
  );
}
""",

"src/components/SectionHeading.tsx": """export default function SectionHeading({
  title,
  subtitle
}: {
  title: string;
  subtitle?: string;
}) {
  return (
    <div className="mb-6">
      <h2 className="text-2xl md:text-3xl font-semibold tracking-tight">{title}</h2>
      {subtitle ? <p className="mt-2 text-zinc-400">{subtitle}</p> : null}
    </div>
  );
}
""",

"src/components/Badge.tsx": """const variants = {
  solid: "bg-white/10 text-zinc-100 border-white/10",
  subtle: "bg-zinc-900/60 text-zinc-200 border-white/10"
} as const;

export default function Badge({
  children,
  variant = "solid"
}: {
  children: React.ReactNode;
  variant?: keyof typeof variants;
}) {
  return (
    <span className={`inline-flex items-center rounded-full border px-3 py-1 text-xs tracking-wide ${variants[variant]}`}>
      {children}
    </span>
  );
}
""",

"src/components/Button.tsx": """import Link from "next/link";

type Props = {
  href: string;
  children: React.ReactNode;
  variant?: "primary" | "ghost";
  external?: boolean;
};

export default function Button({ href, children, variant = "primary", external }: Props) {
  const base =
    "inline-flex items-center justify-center rounded-2xl px-5 py-3 text-sm font-medium transition " +
    "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-indigo-400/70";

  const styles =
    variant === "primary"
      ? "bg-white text-zinc-950 hover:bg-zinc-200 shadow-soft"
      : "bg-white/5 text-zinc-100 hover:bg-white/10 border border-white/10";

  if (external) {
    return (
      <a className={`${base} ${styles}`} href={href} target="_blank" rel="noreferrer">
        {children}
      </a>
    );
  }

  return (
    <Link className={`${base} ${styles}`} href={href}>
      {children}
    </Link>
  );
}
""",

"src/components/ProjectCard.tsx": """import Badge from "./Badge";
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
""",

"src/components/Navbar.tsx": """import Container from "./Container";

const links = [
  { href: "#about", label: "About" },
  { href: "#skills", label: "Skills" },
  { href: "#projects", label: "Projects" },
  { href: "#experience", label: "Experience" },
  { href: "#education", label: "Education" },
  { href: "#contact", label: "Contact" }
];

export default function Navbar() {
  return (
    <header className="sticky top-0 z-40 border-b border-white/10 bg-zinc-950/55 backdrop-blur">
      <Container className="py-4">
        <nav className="flex items-center justify-between gap-4">
          <a href="#top" className="font-semibold tracking-tight">
            TG<span className="text-zinc-400">.dev</span>
          </a>
          <div className="hidden md:flex items-center gap-6">
            {links.map((l) => (
              <a key={l.href} href={l.href} className="text-sm text-zinc-300 hover:text-white transition">
                {l.label}
              </a>
            ))}
          </div>
          <a href="#contact" className="text-sm rounded-2xl px-4 py-2 bg-white/5 hover:bg-white/10 border border-white/10 transition">
            Contact
          </a>
        </nav>
      </Container>
    </header>
  );
}
""",

"src/components/Footer.tsx": """import Container from "./Container";

export default function Footer() {
  return (
    <footer className="border-t border-white/10 py-10">
      <Container className="flex flex-col md:flex-row items-center justify-between gap-3">
        <p className="text-sm text-zinc-400">© {new Date().getFullYear()} Trevon Griffin</p>
        <p className="text-sm text-zinc-500">Built with Next.js + Tailwind</p>
      </Container>
    </footer>
  );
}
""",

# Tailwind animation helpers used by the hero (shadow-soft + shimmer/floaty)
"tailwind.config.js": """/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,ts,jsx,tsx,mdx}"],
  theme: {
    extend: {
      boxShadow: { soft: "0 10px 30px rgba(0,0,0,.25)" },
      keyframes: {
        floaty: { "0%,100%": { transform: "translateY(0)" }, "50%": { transform: "translateY(-6px)" } },
        shimmer: { "0%": { backgroundPosition: "0% 50%" }, "100%": { backgroundPosition: "200% 50%" } }
      },
      animation: {
        floaty: "floaty 6s ease-in-out infinite",
        shimmer: "shimmer 8s linear infinite"
      }
    }
  },
  plugins: []
};
"""
}

def main():
    # quick check to reduce "wrong folder" problems
    if not (ROOT / "package.json").exists():
        print("❌ I don’t see package.json in this folder.")
        print("➡️ Run this script INSIDE your Next.js project folder (the one with package.json).")
        return

    for rel, content in FILES.items():
        write(rel, content)

    print("\n✅ Done! Next:")
    print("1) npm install")
    print("2) npm run dev")
    print("3) Update links in src/data/site.ts (GitHub/LinkedIn/resume)")
    print("Optional: Put resume at public/resume.pdf and set links.resume to '/resume.pdf'.")

if __name__ == "__main__":
    main()
