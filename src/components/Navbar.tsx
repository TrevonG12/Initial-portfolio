import Container from "./Container";

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
