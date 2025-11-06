# tests/test_app.py
from app import save_note
import pytest

def test_save_note_trims_and_limits():
    assert save_note("  hello  ") == "hello"
    assert len(save_note("x" * 250)) == 200  # capped at 200

def test_empty_note_raises():
    with pytest.raises(Exception):
        save_note("")
