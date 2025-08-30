import axios from 'axios'
const API = import.meta.env.VITE_API_BASE || 'http://localhost:8000'
function headers(){ const t = localStorage.getItem('ff_token'); return t ? { Authorization: `Bearer ${t}` } : {} }
export async function analyzeText(input:string){ const res = await axios.post(`${API}/api/analyze`, {input, mode:'text', lang:'en'}, { headers: headers() }); return res.data }
