import React from "react";

export default function Footer() {
  return (
    <footer className="bg-gray-200 text-center p-3 mt-8">
      <p>© {new Date().getFullYear()} FactForge | Built with ❤️</p>
    </footer>
  );
}
