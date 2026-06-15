export default function CommandList({ commands, selectedId, onSelect, onDelete }) {
  return (
    <div className="command-list">
      <div className="panel-header">COMMANDS</div>
      <table className="cmd-table">
        <thead>
          <tr>
            <th>#</th>
            <th>COMMAND</th>
            <th>STATUS</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {commands.length === 0 && (
            <tr><td colSpan={4} className="empty">no commands</td></tr>
          )}
          {commands.map(cmd => (
            <tr
              key={cmd.id}
              className={`cmd-row ${selectedId === cmd.id ? 'active' : ''}`}
              onClick={() => onSelect(cmd.id)}
            >
              <td className="dim">{cmd.order}</td>
              <td className="cmd-text">{cmd.command}</td>
              <td><StatusBadge status={cmd.status} /></td>
              <td>
                <button
                  className="delete-btn"
                  onClick={e => { e.stopPropagation(); onDelete(cmd.id) }}
                >×</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

function StatusBadge({ status }) {
  const cls = { DONE: 'status-done', PENDING: 'status-pending', FAILED: 'status-failed' }[status] ?? ''
  return <span className={`status ${cls}`}>{status}</span>
}
