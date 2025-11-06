# Secure Input Demo (G2 Evidence)

### What this shows
- Input validation
- .env configuration
- Parameterised SQL queries

### Setup
```
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

### Run & screenshot
```
python main.py
# enter a valid note (accepted)
python main.py
# enter invalid chars like <script>... (blocked)
```
Take 2 screenshots:
1) Accepted note shows `[saved] id=...`
2) Blocked input shows `[blocked] ...`

### Upload to Portfolium
- Repo link or this folder zipped
- The two screenshots
- 3–4 sentences on what it fixes
