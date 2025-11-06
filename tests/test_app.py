# tests/test_app.py
import importlib

def _import_target():
    for mod in ("app", "main"):
        try:
            m = importlib.import_module(mod)
            if hasattr(m, "save_note"):
                return m
        except Exception:
            pass
    raise ImportError("Could not find save_note in app.py or main.py")

def test_save_note_trims_and_limits():
    m = _import_target()
    s = m.save_note("  hello  ")
    assert s == "hello"
    long_text = "x" * 250
    s2 = m.save_note(long_text)
    assert len(s2) == 200

def test_empty_note_raises():
    m = _import_target()
    import pytest
    with pytest.raises(Exception):
        m.save_note("")
