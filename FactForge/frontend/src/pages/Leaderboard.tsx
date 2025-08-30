import React, { useEffect, useState } from 'react'
import axios from 'axios'
const API = import.meta.env.VITE_API_BASE || 'http://localhost:8000'

export default function Leaderboard(){
  const [rows,setRows]=useState<any[]>([])
  useEffect(()=>{ axios.get(`${API}/leaderboard/top`).then(r=>setRows(r.data)).catch(()=>{}) },[])
  return (
    <div>
      <h1>Leaderboard</h1>
      <div>
        {rows.map((r:any,i:number)=>(
          <div className="card" key={i}><strong>{i+1}. {r.user}</strong><div>Analyses: {r.count}</div></div>
        ))}
      </div>
    </div>
  )
}
