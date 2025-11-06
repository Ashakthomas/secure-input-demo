# tests/test_app.py
# ruff: noqa: E402  ← allow path-adjust before imports

import sys
from pathlib import Path

# Ensure repo root (where app.py lives) is on sys.path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app import save_note
import pytest

def test_save_note_trims_and_limits():
    assert save_note("  hello  ") == "hello"
    assert len(save_note("x" * 250)) == 200  # capped at 200

def test_empty_note_raises():
    with pytest.raises(Exception):
        save_note("")
