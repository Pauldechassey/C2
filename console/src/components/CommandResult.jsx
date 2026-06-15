export default function CommandResult({ command }) {
  return (
    <div className="command-result">
      <div className="panel-header">OUTPUT</div>
      <div className="result-content">
        {!command && <span className="dim">select a command</span>}
        {command && !command.output && <span className="dim">no output yet</span>}
        {command?.output && <pre>{command.output}</pre>}
      </div>
    </div>
  )
}
