import React, { useState } from 'react'
import axios from 'axios'
const API = import.meta.env.VITE_API_BASE || 'http://localhost:8000'

export default function Register(){
  const [email,setEmail]=useState(''); const [password,setPassword]=useState(''); const [loading,setLoading]=useState(false)
  const register = async ()=>{ setLoading(true); try{ await axios.post(`${API}/auth/register`, {email,password}); alert('Registered — now login'); window.location.href='/login' }catch(e:any){ alert(e?.response?.data?.detail || 'Register failed') }finally{ setLoading(false) } }
  return (
    <div className="card" style={{maxWidth:520,margin:'40px auto'}}>
      <h2>Register</h2>
      <div style={{display:'grid',gap:12}}>
        <input className="text" placeholder="Email" value={email} onChange={e=>setEmail(e.target.value)} />
        <input className="text" placeholder="Password" type="password" value={password} onChange={e=>setPassword(e.target.value)} />
        <div style={{display:'flex',gap:12}}>
          <button className="button" onClick={register} disabled={!email||!password||loading}>{loading?'...':'Register'}</button>
        </div>
      </div>
    </div>
  )
}
