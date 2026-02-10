import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Classificados",
  description: "Classificados de Veículos",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pt-BR">
      <body
        className={`antialiased bg-black`}
      >
        <main className="mx-auto max-w-4xl pb-28">
          {children}
        </main>

      </body>
    </html>
  );
}


