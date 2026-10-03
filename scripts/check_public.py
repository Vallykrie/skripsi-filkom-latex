"""Audit the public template sample and local documentation links."""
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
BLOCKED_SAMPLE_TEXT = (
    "/Users/", "/home/", "C:\\Users\\",
)


def public_errors(root: Path = ROOT) -> list[str]:
    errors = []
    samples = [root / "metadata.tex", *sorted((root / "chapters").glob("*.tex")),
               *sorted((root / "frontmatter").glob("*.tex")),
               *sorted((root / "appendices").glob("*.tex")),
               root / "bibliography" / "references.bib"]
    for path in samples:
        if not path.is_file():
            errors.append(f"Sample tidak ditemukan: {path.relative_to(root)}")
            continue
        text = path.read_text(encoding="utf-8")
        for value in BLOCKED_SAMPLE_TEXT:
            if value.casefold() in text.casefold():
                errors.append(f"Isi pribadi pada sample {path.relative_to(root)}: {value}")
    for path in root.rglob("*.md"):
        if "build" in path.relative_to(root).parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            target = target.strip().split()[0].strip("<>")
            if target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            local = unquote(target.split("#", 1)[0])
            if local and not (path.parent / local).exists():
                errors.append(f"Tautan lokal rusak di {path.relative_to(root)}: {local}")
    if (root / ".git").exists():
        files = subprocess.run(
            ["git", "-C", str(root), "ls-files", "-z"],
            check=True, capture_output=True, text=True,
        ).stdout.split("\0")
        fonts = [name for name in files if Path(name).suffix.lower() in {".ttf", ".otf"}]
    else:
        fonts = [path for path in root.rglob("*")
                 if path.suffix.lower() in {".ttf", ".otf"}
                 and "fonts" not in path.relative_to(root).parts]
    if fonts:
        errors.append("Paket publik tidak boleh mengandung berkas font")
    return errors


def main() -> int:
    errors = public_errors()
    for error in errors:
        print(f"ERROR: {error}")
    if not errors:
        print("Public sample and local documentation links: PASS")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
