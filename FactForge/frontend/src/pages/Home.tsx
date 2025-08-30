import React, { useState } from 'react'
import ClaimInput from '../components/ClaimInput'
import ResultCard from '../components/ResultCard'
import Loader from '../components/Loader'
import { analyzeText } from '../services/api'

export default function Home(){
  const [input,setInput]=useState('Drinking hot water cures COVID.'); const [loading,setLoading]=useState(false); const [result,setResult]=useState<any>(null)
  const onAnalyze=async ()=>{ setLoading(true); setResult(null); try{ const res=await analyzeText(input); setResult(res) }catch(e){ alert('Error'); }finally{ setLoading(false) } }
  return (
    <div>
      <div className="card" style={{display:'grid',gridTemplateColumns:'1fr 320px',gap:16}}>
        <div>
          <h1>Analyze Claims</h1>
          <p>Paste text or a claim and get verdicts, explanations, and sources.</p>
          <ClaimInput value={input} onChange={setInput} onAnalyze={onAnalyze} loading={loading} />
          <div style={{marginTop:12}}>
            <button className="button" onClick={()=>setInput('5G towers cause COVID')}>5G & COVID</button>
            <button className="button" style={{marginLeft:8}} onClick={()=>setInput('Earth orbits the Sun')}>Heliocentric</button>
          </div>
        </div>
        <div className="card">
          <h3>About</h3>
          <p>FactForge uses AI and trusted sources to detect misinformation and craft human-friendly explanations.</p>
        </div>
      </div>

      {loading && <div className="card"><Loader/></div>}
      {result && !loading && <div className="card"><ResultCard data={result}/></div>}
    </div>
  )
}
