import React, { useState } from 'react'
import ClaimInput from '../components/ClaimInput'
import ResultCard from '../components/ResultCard'
import Loader from '../components/Loader'
import { analyzeText } from '../services/api'

export default function Home() {
  const [input, setInput] = useState('Drinking hot water cures COVID.')
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState<any>(null)

  const onAnalyze = async () => {
    setLoading(true)
    setResult(null)
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

        {/* Demo Presets */}
        <div style={{marginTop:12}}>
          <span style={{opacity:.7, fontSize:14}}>Try Examples: </span>
          <button className="button" onClick={()=>setInput("5G towers cause COVID")}>5G & COVID</button>
          <button className="button" onClick={()=>setInput("Earth is flat")}>Flat Earth</button>
          <button className="button" onClick={()=>setInput("Vaccines cause autism")}>Vaccines</button>
        </div>
      </div>

      {loading && (
        <div className="card"><Loader /></div>
      )}

      {result && !loading && (
        <div className="card">
          <ResultCard data={result} />
        </div>
      )}

      <div className="footer">© 2025 FactForge — Demo</div>
    </div>
  )
}
