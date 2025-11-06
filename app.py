# app.py — tiny pure function for CI tests

def save_note(text: str) -> str:
    """
    Return a trimmed note (max 200 chars).
    Raises ValueError for empty/whitespace-only input.
    """
    text = (text or "").strip()
    if not text:
        raise ValueError("empty note")
    return text[:200]
