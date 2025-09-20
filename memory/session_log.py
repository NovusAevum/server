from pathlib import Path

def recall_recent_sessions():
    log_path = Path(__file__).parent.parent / "log" / "session_notes.md"
    if not log_path.exists():
        return {"log": "No previous sessions recorded."}
    return {"log": log_path.read_text()}
