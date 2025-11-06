#!/usr/bin/env python3
import os, re, sqlite3
from dotenv import load_dotenv

# Load .env
load_dotenv()
DB_PATH = os.getenv("DB_PATH", "notes.db")
TABLE = os.getenv("TABLE_NAME", "notes")

SAFE_TEXT = re.compile(r"^[\w\s\.,\-!\?]{1,200}$")

def is_safe_text(text: str) -> bool:
    return bool(SAFE_TEXT.fullmatch(text))

def setup_db(conn):
    cur = conn.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {TABLE} (id INTEGER PRIMARY KEY AUTOINCREMENT, body TEXT)")
    conn.commit()

def save_note(conn, note: str) -> int:
    cur = conn.cursor()
    cur.execute(f"INSERT INTO {TABLE} (body) VALUES (?)", (note,))
    conn.commit()
    return cur.lastrowid

def list_notes(conn):
    cur = conn.cursor()
    cur.execute(f"SELECT id, body FROM {TABLE} ORDER BY id DESC")
    return cur.fetchall()

def main():
    note = input("Enter a short note (<=200 chars): ").strip()
    if not is_safe_text(note):
        print("[blocked] Invalid characters or length. Aborting.")
        return
    conn = sqlite3.connect(DB_PATH)
    setup_db(conn)
    note_id = save_note(conn, note)
    rows = list_notes(conn)
    conn.close()
    print(f"[saved] id={note_id}")
    for rid, body in rows[:5]:
        print(f"[recent] id={rid} body={body}")

if __name__ == "__main__":
    main()
