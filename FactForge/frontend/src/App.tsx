import React, { useState } from 'react'
import { Routes, Route, useNavigate, Navigate } from 'react-router-dom'
import Navbar from './components/Navbar'
import Footer from './components/Footer'
import Landing from './pages/Landing'
import Login from './pages/Login'
import Register from './pages/Register'
import Home from './pages/Home'
import Dashboard from './pages/Dashboard'
import Leaderboard from './pages/Leaderboard'
import ProtectedRoute from './routes/ProtectedRoute'

export default function App(){
  const [token, setToken] = useState<string | null>(
    localStorage.getItem('ff_token')
  )
  const navigate = useNavigate()

  const handleLogin = (t: string) => {
    localStorage.setItem('ff_token', t)
    setToken(t)
    navigate('/home')
  }

  const handleLogout = () => {
    localStorage.removeItem('ff_token')
    setToken(null)
    navigate('/')
  }

  return (
    <>
      <Navbar isAuthed={!!token} onLogout={handleLogout} />
      <div className="container mx-auto px-4 py-6">
        <Routes>
          {/* Public routes */}
          <Route path="/" element={<Landing />} />
          <Route path="/login" element={<Login onLogin={handleLogin} />} />
          <Route path="/register" element={<Register />} />

          {/* Protected routes */}
          <Route element={<ProtectedRoute isAuthed={!!token} />}>
            <Route path="/home" element={<Home />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
          </Route>

          {/* Fallback */}
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </div>
      <Footer />
    </>
  )
}
