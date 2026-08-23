"""Fail if any language is missing UI keys."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from i18n import LANGS, _STRINGS  # noqa: E402


def test_keys_match() -> None:
    base = set(_STRINGS["en"])
    assert base, "english strings empty"
    for lang in LANGS:
        keys = set(_STRINGS[lang])
        missing = base - keys
        extra = keys - base
        assert not missing, f"{lang} missing {sorted(missing)}"
        assert not extra, f"{lang} extra {sorted(extra)}"


if __name__ == "__main__":
    test_keys_match()
    print("i18n ok", ",".join(LANGS), "keys", len(_STRINGS["en"]))
