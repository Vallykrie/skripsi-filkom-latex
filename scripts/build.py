"""Build the template with XeLaTeX/Biber; protect student files when cleaning."""
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
MODES = {"preview": "carlito", "official": "calibri"}
SUFFIXES = {
    ".aux", ".bbl", ".bcf", ".blg", ".fdb_latexmk", ".fls", ".loa",
    ".lof", ".log", ".lot", ".out", ".pdf", ".run.xml", ".synctex.gz",
    ".toc", ".xdv",
}
GENERATED = {
    f"skripsi-{mode}{suffix}" for mode in MODES for suffix in SUFFIXES
} | {"entry-preview.tex", "entry-official.tex", "missfont.log"}


def validated_build(path: Path, root: Path) -> Path:
    if path.is_symlink():
        raise ValueError("Direktori build tidak boleh berupa symlink")
    if path.resolve() != root.resolve() / "build":
        raise ValueError("Direktori build harus tepat berada di root/build")
    return path.resolve()


def clean_build_dir(path: Path = BUILD, root: Path = ROOT) -> None:
    path = validated_build(path, root)
    if path.exists():
        for child in path.iterdir():
            if child.name in GENERATED and (child.is_file() or child.is_symlink()):
                child.unlink()


def write_entry(mode: str, path: Path = BUILD, root: Path = ROOT) -> Path:
    if mode not in MODES:
        raise ValueError(f"Mode tidak didukung: {mode}")
    path = validated_build(path, root)
    path.mkdir(exist_ok=True)
    entry = path / f"entry-{mode}.tex"
    if entry.is_symlink():
        raise ValueError("Berkas entry tidak boleh berupa symlink")
    entry.write_text(
        f"\\PassOptionsToClass{{{mode},font={MODES[mode]}}}{{filkomskripsi}}\n"
        "\\input{skripsi.tex}\n", encoding="utf-8",
    )
    return entry


def remove_pdf(mode: str) -> None:
    path = validated_build(BUILD, ROOT) / f"skripsi-{mode}.pdf"
    if path.is_symlink():
        raise ValueError("Berkas PDF output tidak boleh berupa symlink")
    path.unlink(missing_ok=True)


def build(mode: str) -> int:
    entry = write_entry(mode)
    remove_pdf(mode)
    command = [
        "latexmk", "-xelatex", "-bibtex", "-interaction=nonstopmode",
        "-halt-on-error", "-file-line-error", f"-outdir={BUILD}",
        f"-jobname=skripsi-{mode}", str(entry),
    ]
    try:
        code = subprocess.run(command, cwd=ROOT, check=False).returncode
    except FileNotFoundError:
        print("latexmk tidak ditemukan. Gunakan TeX Live/MacTeX atau MiKTeX.")
        return 127
    if code:
        remove_pdf(mode)
    return code


def check() -> int:
    commands = [[sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"]]
    for command in commands:
        code = subprocess.run(command, cwd=ROOT, check=False).returncode
        if code:
            return code
    code = build("preview")
    if code:
        return code
    for script, args in [
        ("check_log.py", [str(BUILD / "skripsi-preview.log")]),
        ("check_pdf.py", [str(BUILD / "skripsi-preview.pdf"), "--mode", "preview"]),
        ("check_public.py", []),
    ]:
        code = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / script), *args],
            cwd=ROOT, check=False,
        ).returncode
        if code:
            return code
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("preview", "official", "check", "clean"))
    mode = parser.parse_args().mode
    try:
        if mode == "clean":
            clean_build_dir()
            return 0
        return check() if mode == "check" else build(mode)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
