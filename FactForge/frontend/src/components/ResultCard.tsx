import React from 'react'
import SourceBadge from './SourceBadge'

export default function ResultCard({ data }:{ data:any }) {
  return (
    <div>
      <h2>Results</h2>
      
      <div style={{marginTop:12}}>
        <h3>Claims</h3>
        <ul>
          {data.claims?.map((c:any, idx:number)=>(
            <li key={idx}>• {c.text}</li>
          ))}
        </ul>
      </div>

      <div style={{marginTop:12}}>
        <h3>Verdicts</h3>
        <ul>
          {data.verdicts?.map((v:any, idx:number)=>(
            <li key={idx}>
              <span className={`badge ${v.label}`}>{v.label.toUpperCase()}</span>
              {v.claim} <em>({Math.round(v.confidence*100)}%)</em>
            </li>
          ))}
        </ul>
      </div>

      <div style={{marginTop:12}}>
        <h3>Explanations</h3>
        <ul>
          {data.explanations?.map((e:any, idx:number)=>(
            <li key={idx}>{e.text}</li>
          ))}
        </ul>
      </div>

      <div className="sources" style={{marginTop:12}}>
        <h3>Sources</h3>
        {data.sources?.map((s:any, idx:number)=>(
          <SourceBadge key={idx} title={s.title} url={s.url} publisher={s.publisher} />
        ))}
      </div>

      {data.shareable?.tweet && (
        <div style={{marginTop:12}}>
          <h3>Shareable</h3>
          <div className="card">{data.shareable.tweet}</div>
        </div>
      )}
    </div>
  )
}
