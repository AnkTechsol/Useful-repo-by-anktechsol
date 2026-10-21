#!/usr/bin/env python3
"""Build one upload-ready zip per gap-filler skill into dist/<plugin>/<skill>.zip.

Each zip has the skill folder at its root, the layout Claude expects when you
upload a skill. Standard library only.  Run from the repo root.
"""
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    n = 0
    for md in sorted((ROOT / "plugins").glob("*/skills/*/SKILL.md")):
        folder = md.parent
        out_dir = ROOT / "dist" / folder.parent.parent.name
        out_dir.mkdir(parents=True, exist_ok=True)
        out = out_dir / f"{folder.name}.zip"
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(folder.rglob("*")):
                if f.is_file() and "__pycache__" not in f.parts:
                    z.write(f, Path(folder.name) / f.relative_to(folder))
        n += 1
        print("built", out.relative_to(ROOT))
    print(f"{n} zips in dist/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
