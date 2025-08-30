import React, { useEffect, useState } from 'react'
import axios from 'axios'
const API = import.meta.env.VITE_API_BASE || 'http://localhost:8000'

export default function Dashboard(){
  const [items,setItems]=useState<any[]>([])
  useEffect(()=>{
    const t = localStorage.getItem('ff_token'); if(!t) return;
    axios.get(`${API}/profile/me/analyses`,{headers:{Authorization:`Bearer ${t}`}}).then(r=>setItems(r.data)).catch(()=>{})
  },[])
  return (
    <div>
      <h1>Your History</h1>
      <div>
        {items.length===0? <div className="card">No analyses yet</div> : items.map(it=>(
          <div className="card" key={it.id}>
            <div><strong>Input:</strong><div>{it.input}</div></div>
            <div style={{marginTop:8}}><strong>Result:</strong><pre style={{whiteSpace:'pre-wrap'}}>{JSON.stringify(it.result,null,2)}</pre></div>
            <div style={{opacity:.7,fontSize:12,marginTop:8}}>At: {it.created_at}</div>
          </div>
        ))}
      </div>
    </div>
  )
}
