import React from "react"
import SourceBadge from "./SourceBadge"

export default function ResultCard({ data }: { data: any }) {
  return (
    <div className="bg-white shadow-md rounded-xl p-6 my-4">
      <h2 className="text-2xl font-bold mb-4">Fact-Check Results</h2>

      {/* Claims */}
      {data.claims?.length > 0 && (
        <div className="mb-4">
          <h3 className="text-lg font-semibold mb-2">Claims</h3>
          <ul className="list-disc list-inside text-gray-700">
            {data.claims.map((c: any, i: number) => (
              <li key={i}>{c.text}</li>
            ))}
          </ul>
        </div>
      )}

      {/* Verdicts */}
      {data.verdicts?.length > 0 && (
        <div className="mb-4">
          <h3 className="text-lg font-semibold mb-2">Verdicts</h3>
          <ul className="space-y-2">
            {data.verdicts.map((v: any, i: number) => (
              <li
                key={i}
                className="flex items-center gap-2 text-gray-800"
              >
                <span
                  className={`px-2 py-1 rounded text-xs font-bold ${
                    v.label === "true"
                      ? "bg-green-100 text-green-700"
                      : v.label === "false"
                      ? "bg-red-100 text-red-700"
                      : "bg-yellow-100 text-yellow-700"
                  }`}
                >
                  {v.label.toUpperCase()}
                </span>
                <span>{v.claim}</span>
                <em className="text-gray-500 text-sm">
                  ({Math.round(v.confidence * 100)}%)
                </em>
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Explanations */}
      {data.explanations?.length > 0 && (
        <div className="mb-4">
          <h3 className="text-lg font-semibold mb-2">Explanations</h3>
          <ul className="list-disc list-inside text-gray-700">
            {data.explanations.map((e: any, i: number) => (
              <li key={i}>{e.text}</li>
            ))}
          </ul>
        </div>
      )}

      {/* Sources */}
      {data.sources?.length > 0 && (
        <div className="mb-4">
          <h3 className="text-lg font-semibold mb-2">Sources</h3>
          <div className="flex flex-wrap gap-2">
            {data.sources.map((s: any, i: number) => (
              <SourceBadge
                key={i}
                title={s.title}
                url={s.url}
                publisher={s.publisher}
              />
            ))}
          </div>
        </div>
      )}

      {/* Shareable */}
      {data.shareable?.tweet && (
        <div className="mt-4">
          <h3 className="text-lg font-semibold mb-2">Shareable</h3>
          <div className="bg-gray-100 rounded p-3 text-sm flex justify-between items-center">
            <span>{data.shareable.tweet}</span>
            <button
              onClick={() => navigator.clipboard.writeText(data.shareable.tweet)}
              className="ml-2 px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600 text-xs"
            >
              Copy
            </button>
          </div>
        </div>
      )}
    </div>
  )
}
