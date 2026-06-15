const BASE = '/api'

function authHeaders() {
  const token = localStorage.getItem('token')
  return {
    'Content-Type': 'application/json',
    ...(token ? { Authorization: `Bearer ${token}` } : {})
  }
}

export async function login(password) {
  const res = await fetch(`${BASE}/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ password })
  })
  if (!res.ok) throw new Error('Invalid password')
  return res.json()
}

export async function getCommands() {
  const res = await fetch(`${BASE}/commands/`, { headers: authHeaders() })
  if (!res.ok) throw new Error('Failed to fetch commands')
  return res.json()
}

export async function createCommand(command, order) {
  const res = await fetch(`${BASE}/commands/`, {
    method: 'POST',
    headers: authHeaders(),
    body: JSON.stringify({ command, order })
  })
  if (!res.ok) throw new Error('Failed to create command')
  return res.json()
}
