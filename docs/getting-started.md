# Memulai template skripsi FILKOM UB

Panduan ini memakai berkas utama `skripsi.tex`. Untuk layanan daring, gunakan [panduan Overleaf](overleaf.md).

## 1. Ambil salinan template

Pilih **[Use this template](https://github.com/Vallykrie/skripsi-filkom-latex/generate)** untuk membuat repository sendiri, atau unduh [ZIP v0.1.0](https://github.com/Vallykrie/skripsi-filkom-latex/archive/refs/tags/v0.1.0.zip). Pengguna Git dapat menjalankan:

```bash
git clone https://github.com/Vallykrie/skripsi-filkom-latex.git
cd skripsi-filkom-latex
```

Simpan naskah yang memuat data pribadi, tanda tangan, atau informasi penelitian terbatas di tempat yang sesuai. Template publik tidak mengharuskan skripsi Anda dipublikasikan.

## 2. Siapkan perangkat kompilasi

Anda membutuhkan Python 3, XeLaTeX, Biber, latexmk, dan paket LaTeX/font yang digunakan template. Distribusi TeX lengkap seperti TeX Live atau MacTeX memudahkan penyediaan dependensi. Make bersifat opsional; seluruh tindakan build utama dapat dijalankan dengan Python. Poppler (perintah `pdfinfo`, `pdftotext`, dan `pdffonts`) dibutuhkan untuk pemeriksaan PDF melalui `make check`.

Periksa ketersediaan perintah:

```bash
python3 --version
xelatex --version
biber --version
latexmk --version
```

Jika sistem menggunakan nama perintah `python` untuk Python 3, sesuaikan perintah Python di panduan ini. Jalankan build dari folder yang memuat `skripsi.tex`, bukan dari `chapters/`.

## 3. Isi metadata

Edit `metadata.tex`: judul, judul Inggris, nama, NIM, program studi, departemen, gelar, tahun, dan pembimbing. Contoh identitas dalam template harus diganti dengan data Anda; tidak ada identitas contoh yang membuktikan persetujuan pembimbing.

Pertahankan koma serta pasangan kurung kurawal dalam `\filkomsetup{...}`. Untuk karakter khusus pada teks LaTeX, gunakan `\&`, `\%`, `\_`, atau `\#` sesuai kebutuhan. Panduan lengkap tersedia di [customization.md](customization.md).

## 4. Buat PDF pertama

```bash
python3 scripts/build.py preview
```

Keluaran berada pada `build/skripsi-preview.pdf`. Build preview memakai Carlito. Periksa bahwa sampul, abstrak Indonesia/Inggris, daftar isi, daftar gambar/tabel/lampiran, bab, referensi, dan lampiran muncul sebagaimana diharapkan.

Jika build gagal, baca kesalahan pertama dalam log dan [panduan troubleshooting](troubleshooting.md). Jangan langsung mengedit kelas untuk mengatasi kesalahan ketik di isi bab.

## 5. Ganti isi contoh dengan penelitian Anda

- `frontmatter/`: persetujuan, orisinalitas, prakata, dan abstrak.
- `chapters/`: Bab 1–6. Tulis isi sesuai struktur yang disetujui pembimbing.
- `bibliography/references.bib`: sumber yang benar-benar dibaca dan digunakan.
- `appendices/`: materi pendukung yang memang perlu dilampirkan.
- `assets/`: gambar yang Anda punya hak untuk gunakan.

Hapus contoh yang tidak relevan. Tabel atau kalimat contoh bukan hasil empiris. Jangan mengisi tanggal persetujuan, nama penguji, atau tanda tangan seolah-olah proses akademik telah terjadi.

## 6. Periksa dan siapkan font akhir

```bash
python3 scripts/build.py check
make test
```

Perintah `make test` menjalankan pengujian template; Make diperlukan untuk perintah ini. Pemeriksaan teknis melengkapi pembacaan PDF oleh penulis, bukan menggantikannya.

Pemeriksaan struktur PDF ditujukan untuk contoh distribusi enam bab dengan Lampiran A/B. Jika Anda mengubah struktur bab atau halaman awal, sesuaikan `scripts/check_pdf.py` dengan struktur naskah Anda; kompilasi `preview` tetap dapat digunakan secara terpisah.

Jika ketentuan naskah Anda memerlukan Calibri dan font sudah tersedia secara legal:

```bash
python3 scripts/build.py official
```

Keluaran berada pada `build/skripsi-official.pdf`. Periksa ulang pemenggalan, tabel, sitasi, dan nomor halaman setelah beralih dari Carlito. Nama mode `official` bukan pernyataan bahwa universitas telah menyetujui naskah.

Untuk membersihkan keluaran kompilasi:

```bash
python3 scripts/build.py clean
```

Simpan perubahan sumber sebelum bekerja. Rincian referensi ada pada [bibliography.md](bibliography.md); rincian font dan struktur bab ada pada [customization.md](customization.md).

[Kembali ke README](../README.md)
