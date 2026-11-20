"""Zip Use_Golden_Key.sdkmod. One root folder, named like the file."""

from __future__ import annotations

import hashlib
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "src" / "Use_Golden_Key"
DIST = ROOT / "dist"
OUTPUT = DIST / "Use_Golden_Key.sdkmod"
SHA_PATH = DIST / "Use_Golden_Key.sdkmod.sha256"
MANIFEST_PATH = DIST / "Use_Golden_Key.manifest.json"
MEMBERS = (
    "Use_Golden_Key/",
    "Use_Golden_Key/__init__.py",
    "Use_Golden_Key/pyproject.toml",
    "Use_Golden_Key/README.md",
)


def main() -> None:
    DIST.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(OUTPUT, "w") as bundle:
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
    digest = hashlib.sha256(OUTPUT.read_bytes()).hexdigest()
    SHA_PATH.write_text(
        f"{digest}  {OUTPUT.name}\n",
        encoding="utf-8",
        newline="\n",
    )
    MANIFEST_PATH.write_text(
        json.dumps(
            {
                "archive": "dist/Use_Golden_Key.sdkmod",
                "member_count": len(MEMBERS),
                "members": list(MEMBERS),
                "schema": 1,
                "sha256": digest,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"built={OUTPUT.relative_to(ROOT).as_posix()} sha256={digest}")


if __name__ == "__main__":
    main()
