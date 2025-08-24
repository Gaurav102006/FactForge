
import React, { useState } from 'react'
import ClaimInput from '../components/ClaimInput'
import ResultCard from '../components/ResultCard'
import { analyzeText } from '../services/api'

export default function Home() {
  const [input, setInput] = useState('Drinking hot water cures COVID.')
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState<any>(null)

  const onAnalyze = async () => {
    setLoading(true)
    try {
      const data = await analyzeText(input)
      setResult(data)
    } catch (e) {
      console.error(e)
      alert('Error contacting API')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container">
      <div className="card">
        <h1>FactForge</h1>
        <p>Paste text or a claim and get instant verdicts, explanations, and sources.</p>
        <ClaimInput value={input} onChange={setInput} onAnalyze={onAnalyze} loading={loading} />
      </div>

      {result && (
        <div className="card">
          <ResultCard data={result} />
        </div>
      )}

      <div className="footer">© 2025 FactForge — Demo</div>
    </div>
  )
}
