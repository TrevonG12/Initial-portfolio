import Link from "next/link";

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
