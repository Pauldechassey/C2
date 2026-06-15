import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import CommandList from '../components/CommandList'
import CommandResult from '../components/CommandResult'
import CommandForm from '../components/CommandForm'
import LogTerminal from '../components/LogTerminal'
import { getCommands } from '../api/client'

export default function Dashboard() {
  const [commands, setCommands] = useState([])
  const [selectedId, setSelectedId] = useState(null)
  const navigate = useNavigate()

  useEffect(() => {
    fetchCommands()
    const interval = setInterval(fetchCommands, 3000)
    return () => clearInterval(interval)
  }, [])

  async function fetchCommands() {
    try {
      const data = await getCommands()
      setCommands(data)
    } catch {
      // ignore polling errors
    }
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
          <span className="dot red" />
          <span className="dot orange" />
          <span className="dot green" />
          <span className="header-title">TEAM SERVER</span>
        </div>
        <button className="logout-btn" onClick={logout}>disconnect</button>
      </header>

      <div className="dashboard-body">
        <div className="command-panel">
          <CommandList commands={commands} selectedId={selectedId} onSelect={setSelectedId} />
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
