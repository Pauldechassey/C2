use std::process::Command as Cmd;

pub fn execute(cmd: &str) -> String {
    match Cmd::new("sh").arg("-c").arg(cmd).output() {
        Ok(out) => String::from_utf8_lossy(&out.stdout).to_string(),
        Err(e)  => format!("error: {e}"),
    }
}