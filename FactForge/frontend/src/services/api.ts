
import axios from 'axios'

const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000'

export async function analyzeText(input:string){
  const res = await axios.post(`${API_BASE}/api/analyze`, { input, mode:'text', lang:'en' })
  return res.data
}
