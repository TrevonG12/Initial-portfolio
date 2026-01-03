const variants = {
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
