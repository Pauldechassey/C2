import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { login } from '../api/client'

export default function Login() {
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const navigate = useNavigate()

  async function handleSubmit(e) {
    e.preventDefault()
    setError('')
    try {
      const { token } = await login(password)
      localStorage.setItem('token', token)
      navigate('/')
    } catch {
      setError('invalid password')
    }
  }

  return (
    <div className="login-container">
      <div className="login-box">
        <div className="login-header">
          <span className="dot red" />
          <span className="dot orange" />
          <span className="dot green" />
          <span className="login-title">TEAM SERVER</span>
        </div>
        <form onSubmit={handleSubmit}>
          <input
            className="login-input"
            type="password"
            placeholder="password"
            value={password}
            onChange={e => setPassword(e.target.value)}
            autoFocus
          />
          {error && <div className="login-error">{error}</div>}
          <button className="login-btn" type="submit">connect</button>
        </form>
      </div>
    </div>
  )
}
