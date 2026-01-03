import Container from "./Container";

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
