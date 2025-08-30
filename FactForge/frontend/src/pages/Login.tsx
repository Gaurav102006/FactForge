import React, { useState } from 'react'
import axios from 'axios'
const API = import.meta.env.VITE_API_BASE || 'http://localhost:8000'

export default function Login({ onLogin }:{ onLogin:(t:string)=>void }){
  const [email,setEmail]=useState(''); const [password,setPassword]=useState(''); const [loading,setLoading]=useState(false)
  const login = async ()=>{ setLoading(true); try{ const form=new URLSearchParams(); form.append('username',email); form.append('password',password); const {data}=await axios.post(`${API}/auth/login`, form, {headers:{'Content-Type':'application/x-www-form-urlencoded'}}); onLogin(data.access_token) }catch(e:any){ alert(e?.response?.data?.detail || 'Login failed') }finally{ setLoading(false) } }
  return (
    <div className="card" style={{maxWidth:520,margin:'40px auto'}}>
      <h2>Login</h2>
      <div style={{display:'grid',gap:12}}>
        <input className="text" placeholder="Email" value={email} onChange={e=>setEmail(e.target.value)} />
        <input className="text" placeholder="Password" type="password" value={password} onChange={e=>setPassword(e.target.value)} />
        <div style={{display:'flex',gap:12}}>
          <button className="button" onClick={login} disabled={!email||!password||loading}>{loading?'...':'Login'}</button>
          <a href="/register" className="button">Register</a>
        </div>
      </div>
    </div>
  )
}
