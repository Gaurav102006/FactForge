import React from 'react'
import { Link } from 'react-router-dom'

export default function Navbar({ isAuthed, onLogout }:{ isAuthed:boolean, onLogout:()=>void }){
  return (<div className="nav"><div className="nav-inner"><div><Link to='/' className="brand">FactForge</Link>{isAuthed && (<><Link to="/home" style={{marginLeft:16}}>Analyze</Link><Link to="/dashboard" style={{marginLeft:12}}>Dashboard</Link><Link to="/leaderboard" style={{marginLeft:12}}>Leaderboard</Link></>)}</div><div>{isAuthed? <button className="button" onClick={onLogout}>Logout</button>:<Link to="/login" className="button">Login</Link>}</div></div></div>)
}
