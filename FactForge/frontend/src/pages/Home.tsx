import React, { useState } from "react";
import { factCheck } from "../services/api";
import ResultCard from "../components/ResultCard";

export default function Home() {
  const [input, setInput] = useState("");
  const [result, setResult] = useState<any>(null);
  const token = localStorage.getItem("ff_token") || "";

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const { data } = await factCheck(input, token);
      setResult(data);
    } catch {
      alert("Error fetching fact-check result");
    }
  };

  return (
    <div className="max-w-2xl mx-auto py-8">
      <h2 className="text-2xl font-bold mb-4">FactForge Home</h2>
      <form onSubmit={handleSubmit} className="flex gap-2 mb-4">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Enter a claim"
          className="flex-1 border p-2 rounded"
        />
        <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded">
          Check
        </button>
      </form>
      {result && <ResultCard data={result} />}
    </div>
  );
}
