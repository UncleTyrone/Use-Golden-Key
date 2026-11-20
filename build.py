"""Zip Use_Golden_Key.sdkmod. One root folder, named like the file."""

from __future__ import annotations

import hashlib
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Use_Golden_Key"
DIST = ROOT / "dist" / "Use_Golden_Key.sdkmod"
MEMBERS = (
    "Use_Golden_Key/",
    "Use_Golden_Key/__init__.py",
    "Use_Golden_Key/pyproject.toml",
    "Use_Golden_Key/README.md",
)


def main() -> None:
    DIST.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(DIST, "w") as bundle:
        for member in MEMBERS:
            info = zipfile.ZipInfo(member)
            info.date_time = (2020, 1, 1, 0, 0, 0)
            info.compress_type = zipfile.ZIP_STORED
            if member.endswith("/"):
                info.external_attr = (0o755 << 16) | 0x10
                bundle.writestr(info, b"")
                continue
            info.external_attr = (0o644 << 16) | 0x20
            data = (SOURCE / member.removeprefix("Use_Golden_Key/")).read_bytes()
            bundle.writestr(info, data)
    digest = hashlib.sha256(DIST.read_bytes()).hexdigest()
    DIST.with_suffix(".sdkmod.sha256").write_text(
        f"{digest}  {DIST.name}\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"built={DIST} sha256={digest}")


if __name__ == "__main__":
    main()
