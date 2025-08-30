// src/pages/Landing.tsx
import React from "react";
import { Link } from "react-router-dom";

export default function Landing() {
  return (
    <div className="flex flex-col items-center justify-center text-center py-20 bg-gradient-to-r from-blue-600 to-indigo-700 text-white min-h-[80vh]">
      <h1 className="text-5xl font-extrabold mb-6">Welcome to FactForge</h1>
      <p className="text-lg max-w-2xl mb-8">
        Combat misinformation with AI-powered fact-checking. Verify claims instantly with trusted sources.
      </p>
      <div className="flex gap-4">
        <Link to="/register" className="px-6 py-3 bg-white text-blue-700 font-semibold rounded shadow hover:bg-gray-200 transition">
          Get Started
        </Link>
        <Link to="/login" className="px-6 py-3 bg-blue-900 font-semibold rounded shadow hover:bg-blue-800 transition">
          Login
        </Link>
      </div>
    </div>
  );
}
