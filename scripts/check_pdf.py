"""Check the bundled six-chapter sample PDF, not academic approval."""
import argparse
import re
import subprocess
from pathlib import Path

HEADINGS = (
    "BAB 1 PENDAHULUAN", "BAB 2 LANDASAN KEPUSTAKAAN", "BAB 3 METODOLOGI",
    "BAB 4 HASIL", "BAB 5 PEMBAHASAN", "BAB 6 PENUTUP", "DAFTAR REFERENSI",
)
FRONT = (
    "PERSETUJUAN", "PERNYATAAN ORISINALITAS", "PRAKATA", "ABSTRAK", "ABSTRACT",
    "DAFTAR ISI", "DAFTAR TABEL", "DAFTAR GAMBAR", "DAFTAR LAMPIRAN",
)


def validate_document_structure(text: str) -> list[str]:
    pages = [" ".join(p.upper().split()) for p in text.split("\f") if p.strip()]
    errors = []
    positions = []
    for heading in FRONT + HEADINGS + ("LAMPIRAN A ", "LAMPIRAN B "):
        found = [i for i, page in enumerate(pages) if page.startswith(heading)]
        if not found:
            errors.append(f"Bagian tidak ditemukan pada awal halaman: {heading}")
        else:
            positions.append(found[0])
    if positions != sorted(positions):
        errors.append("Urutan halaman awal atau bab tidak benar")
    if any(re.match(r"^BAB\s+[AB]\b", page) for page in pages):
        errors.append("Lampiran tidak boleh berlabel BAB A/B")
    return errors


def validate_fonts(fonts: set[str], mode: str) -> list[str]:
    lower = {f.casefold() for f in fonts}
    family = "calibri" if mode == "official" else "carlito"
    if mode not in {"preview", "official"}:
        raise ValueError("Mode tidak dikenal")
    if not any(f.startswith(family) for f in lower):
        return [f"Font {family} tidak ditemukan dalam PDF"]
    if mode == "official" and any(f.startswith("carlito") for f in lower):
        return ["Mode official tidak boleh memakai Carlito"]
    return []


def tool(command: list[str]) -> str:
    return subprocess.run(command, check=True, capture_output=True, text=True).stdout


def check_pdf(pdf: Path, mode: str) -> list[str]:
    if not pdf.is_file():
        return [f"PDF tidak ditemukan: {pdf}"]
    try:
        info = tool(["pdfinfo", str(pdf)])
        text = tool(["pdftotext", "-layout", str(pdf), "-"])
        font_output = tool(["pdffonts", str(pdf)])
    except (FileNotFoundError, subprocess.CalledProcessError) as exc:
        return [f"Pemeriksaan Poppler gagal: {exc}"]
    size = re.search(r"Page size:\s*([\d.]+)\s*x\s*([\d.]+)", info)
    errors = []
    if not size or abs(float(size[1]) - 595.28) > 1 or abs(float(size[2]) - 841.89) > 1:
        errors.append("Ukuran halaman bukan A4")
    fonts = set()
    for line in font_output.splitlines()[2:]:
        fields = line.split()
        if fields:
            fonts.add(fields[0].split("+", 1)[-1])
            if fields[-5] != "yes":
                errors.append(f"Font tidak tertanam: {fields[0]}")
    return errors + validate_document_structure(text) + validate_fonts(fonts, mode)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--mode", choices=("preview", "official"), default="preview")
    args = parser.parse_args()
    errors = check_pdf(args.pdf, args.mode)
    for error in errors:
        print(f"ERROR: {error}")
    if not errors:
        print(f"PDF sample valid ({args.mode}): {args.pdf}")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
