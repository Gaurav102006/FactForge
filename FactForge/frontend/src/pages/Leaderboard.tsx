import React from "react";

export default function Leaderboard() {
  const mockData = [
    { user: "Alice", checks: 20 },
    { user: "Bob", checks: 15 },
    { user: "Charlie", checks: 12 },
  ];

  return (
    <div className="max-w-2xl mx-auto py-8">
      <h2 className="text-2xl font-bold mb-4">Leaderboard</h2>
      <ul className="border rounded divide-y">
        {mockData.map((row, i) => (
          <li key={i} className="p-3 flex justify-between">
            <span>{row.user}</span>
            <span>{row.checks} checks</span>
          </li>
        ))}
      </ul>
    </div>
  );
}
