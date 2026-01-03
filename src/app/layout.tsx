import "./globals.css";
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
