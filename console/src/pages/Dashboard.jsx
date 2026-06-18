import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import CommandList from '../components/CommandList'
import CommandResult from '../components/CommandResult'
import CommandForm from '../components/CommandForm'
import LogTerminal from '../components/LogTerminal'
import { getCommands, deleteCommand } from '../api/client'

export default function Dashboard() {
  const [commands, setCommands] = useState([])
  const [selectedId, setSelectedId] = useState(null)
  const navigate = useNavigate()

  useEffect(() => {
    fetchCommands()

    const token = localStorage.getItem('token')
    const proto = location.protocol === 'https:' ? 'wss:' : 'ws:'
    const ws = new WebSocket(`${proto}//${location.host}/ws/commands?token=${token}`)
    ws.onmessage = () => fetchCommands()

    return () => ws.close()
  }, [])

  async function fetchCommands() {
    try {
      const data = await getCommands()
      setCommands(data)
    } catch {}
  }

  async function handleDelete(id) {
    try {
      await deleteCommand(id)
      if (selectedId === id) setSelectedId(null)
    } catch {}
  }

  function logout() {
    localStorage.removeItem('token')
    navigate('/login')
  }

  const selected = commands.find(c => c.id === selectedId) ?? null

  return (
    <div className="dashboard">
      <header className="dashboard-header">
        <div className="header-left">
        </div>
        <button className="logout-btn" onClick={logout}>disconnect</button>
      </header>

      <div className="dashboard-body">
        <div className="command-panel">
          <CommandList commands={commands} selectedId={selectedId} onSelect={setSelectedId} onDelete={handleDelete} />
          <CommandForm
            onCreated={fetchCommands}
            nextOrder={commands.length + 1}
          />
        </div>
        <CommandResult command={selected} />
      </div>

      <LogTerminal />
    </div>
  )
}
