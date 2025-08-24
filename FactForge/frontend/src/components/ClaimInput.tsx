
import React from 'react'

export default function ClaimInput({ value, onChange, onAnalyze, loading }:{ value:string, onChange:(v:string)=>void, onAnalyze:()=>void, loading:boolean }){
  return (
    <div>
      <textarea className="input" value={value} onChange={e=>onChange(e.target.value)} placeholder="Paste article text or a claim..." />
      <div style={{display:'flex', gap:12, marginTop:12}}>
        <button className="button" onClick={onAnalyze} disabled={loading}>
          {loading ? 'Analyzing…' : 'Analyze'}
        </button>
        <span className="badge">GenAI</span>
        <span className="badge">Misinformation</span>
      </div>
    </div>
  )
}
