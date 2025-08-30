import React from 'react'
import { Link } from 'react-router-dom'

export default function Landing(){
  return (
    <div className="card">
      <h1>FactForge</h1>
      <p>AI-powered fact-checking. Paste any claim and get instant verdicts with explanations & trusted sources.</p>
      <div style={{marginTop:12}}>
        <Link to="/login" className="button">Get Started</Link>
        <Link to="/home" className="button" style={{marginLeft:8}}>Try Demo</Link>
      </div>
    </div>
  )
}
