import React from "react";
import { Link } from "react-router-dom";
import { Sun, Moon } from "lucide-react"; // icon library (install: npm i lucide-react)
import useTheme from "../hooks/useTheme";

export default function Navbar({ isAuthed, onLogout }: { isAuthed: boolean; onLogout: () => void }) {
  const { theme, toggleTheme } = useTheme();

  return (
    <nav className="bg-gray-900 dark:bg-gray-100 text-white dark:text-gray-900 px-8 py-4 flex justify-between items-center shadow-md transition">
      <div className="font-extrabold text-2xl text-blue-400 dark:text-blue-600">FactForge</div>
      
      <div className="flex gap-6 items-center">
        {isAuthed ? (
          <>
            <Link className="hover:text-blue-400 dark:hover:text-blue-600 transition" to="/home">Home</Link>
            <Link className="hover:text-blue-400 dark:hover:text-blue-600 transition" to="/dashboard">Dashboard</Link>
            <Link className="hover:text-blue-400 dark:hover:text-blue-600 transition" to="/leaderboard">Leaderboard</Link>
            <button onClick={onLogout} className="px-4 py-2 bg-red-600 hover:bg-red-700 dark:bg-red-400 dark:hover:bg-red-500 rounded text-sm text-white dark:text-gray-100 transition">
              Logout
            </button>
          </>
        ) : (
          <>
            <Link className="hover:text-blue-400 dark:hover:text-blue-600 transition" to="/login">Login</Link>
            <Link className="hover:text-blue-400 dark:hover:text-blue-600 transition" to="/register">Register</Link>
          </>
        )}

        {/* Theme Toggle */}
        <button
          onClick={toggleTheme}
          className="ml-4 p-2 rounded-full bg-gray-700 dark:bg-gray-300 text-white dark:text-gray-800 hover:scale-105 transition"
        >
          {theme === "light" ? <Moon size={20} /> : <Sun size={20} />}
        </button>
      </div>
    </nav>
  );
}
