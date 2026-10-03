# Menggunakan template di Overleaf

## Unggah dan pilih compiler

1. Unduh [ZIP v0.1.0](https://github.com/Vallykrie/skripsi-filkom-latex/archive/refs/tags/v0.1.0.zip).
2. Buat proyek Overleaf dengan mengunggah ZIP tersebut.
3. Pastikan direktori yang memuat `skripsi.tex` juga memuat `filkomskripsi.cls` dan `metadata.tex`. Jika ZIP menghasilkan satu folder pembungkus, pilih `skripsi.tex` di dalam folder itu sebagai berkas utama.
4. Pada pengaturan proyek, pilih compiler **XeLaTeX** dan main document **`skripsi.tex`**.
5. Edit `metadata.tex`, lalu tekan **Recompile**.

Lihat petunjuk resmi Overleaf tentang [pemilihan compiler](https://www.overleaf.com/learn/latex/Choosing_a_LaTeX_Compiler) dan [berkas utama](https://www.overleaf.com/learn/latex/Multi-file_LaTeX_projects).

Jangan memilih `filkomskripsi.cls`, salah satu berkas bab, atau abstrak sebagai main document. Template memakai `fontspec` sehingga membutuhkan XeLaTeX, bukan pdfLaTeX.

## Font pratinjau

`skripsi.tex` dikompilasi langsung dalam mode preview dengan pemilihan font otomatis: Calibri jika tersedia, kemudian Carlito. Pada proyek tanpa Calibri, Carlito menyediakan jalur pratinjau terbuka.

Skrip lokal `python3 scripts/build.py preview` memaksa Carlito untuk reproduksibilitas pemeriksaan. Overleaf mengompilasi `skripsi.tex` secara langsung; tidak perlu menjalankan skrip Python atau Make di sana. Jika Anda memerlukan pemilihan font eksplisit, gunakan opsi kelas yang didokumentasikan di [customization.md](customization.md).

## Calibri pada proyek privat

Calibri tidak disertakan dalam repository ini. Jika Anda mempunyai berkas font yang boleh digunakan pada layanan tersebut:

1. Simpan proyek yang memuat font proprietary secara privat.
2. Unggah keluarga font ke folder `fonts/`: `calibri.ttf`, `calibrib.ttf`, `calibrii.ttf`, dan `calibriz.ttf`.
3. Tambahkan `font-dir={fonts/}` pada `\filkomsetup` di `metadata.tex`; lihat [pengaturan direktori font](customization.md#font).
4. Pilih mode/font Calibri sesuai opsi kelas, lalu kompilasi ulang dengan XeLaTeX.
5. Periksa bahwa font yang dimaksud benar-benar digunakan dan periksa perubahan pemenggalan halaman.

Hak penggunaan font mengikuti lisensi asalnya. Folder `fonts/` diabaikan Git dan paket ZIP publik template. Jangan memasukkan berkas Calibri ke pull request, ZIP publik, atau release template. Panduan resmi Overleaf mengenai font terdapat di [XeLaTeX](https://www.overleaf.com/learn/latex/XeLaTeX).

## Referensi dan lampiran

Overleaf mengelola siklus kompilasi untuk bibliografi. Gunakan database `bibliography/references.bib` dan sitasi seperti `\parencite{key}` atau `\textcite{key}`; jangan mengganti backend Biber menjadi BibTeX tanpa menyesuaikan konfigurasi. Lihat [panduan bibliografi](bibliography.md).

Daftar isi dan rujukan silang dapat membutuhkan kompilasi ulang. Tambahkan bab/lampiran melalui `\input{...}` pada `skripsi.tex`, lalu periksa nomor dan judulnya dalam PDF. Letakkan tambahan lampiran setelah `\appendix`.

## Jika build di Overleaf gagal

- Baca kesalahan pertama, bukan hanya pesan terakhir bahwa PDF gagal dibuat.
- Pastikan compiler XeLaTeX dan berkas utama `skripsi.tex`.
- Periksa huruf besar/kecil pada nama berkas dan path gambar.
- Jika perubahan font atau referensi belum terlihat, gunakan kompilasi ulang dari awal setelah menyimpan sumber.
- Untuk batas waktu kompilasi, kecilkan gambar besar dan coba build lokal. Ketersediaan waktu/runtime mengikuti paket Overleaf yang Anda gunakan.

Lihat [troubleshooting.md](troubleshooting.md) untuk masalah font, sitasi, dan daftar lampiran. Saat melaporkan masalah, kirim contoh minimal yang tidak memuat identitas, tanda tangan, atau data penelitian privat.

[Kembali ke README](../README.md)
