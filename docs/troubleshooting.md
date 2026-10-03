# Mengatasi masalah kompilasi

Mulai dari **kesalahan pertama** dalam log. Pesan terakhir sering hanya akibat kesalahan sebelumnya. Pastikan build dijalankan dari folder yang memuat `skripsi.tex`; gunakan berkas utama tersebut di Overleaf.

## `xelatex` atau `biber` tidak ditemukan

Pastikan distribusi TeX sudah terpasang dan perintah tersedia pada PATH terminal:

```bash
xelatex --version
biber --version
```

Tutup dan buka terminal setelah instalasi jika PATH belum diperbarui. Paket sistem berbeda menurut distribusi; gunakan pengelola paket TeX Anda. Python tidak memasang XeLaTeX atau Biber secara otomatis.

## `fontspec` membutuhkan XeTeX atau LuaTeX

Compiler yang dipilih kemungkinan pdfLaTeX. Template ini menggunakan **XeLaTeX**. Di Overleaf, ubah compiler pada pengaturan proyek; di komputer lokal, gunakan `python3 scripts/build.py preview`.

## Calibri tidak ditemukan

Mode `official` membutuhkan Calibri yang tersedia secara legal. Gunakan mode preview untuk melanjutkan penulisan:

```bash
python3 scripts/build.py preview
```

Untuk Calibri, pastikan font terpasang dan terbaca oleh XeLaTeX, atau gunakan folder font privat dengan key `font-dir={fonts/}` pada `metadata.tex`. Nama dan keluarga berkas harus cocok dengan konfigurasi kelas. Lihat [panduan font](customization.md#font) dan [Overleaf](overleaf.md#calibri-pada-proyek-privat).

Jangan mengunduh font dari sumber tanpa hak distribusi yang jelas atau memasukkannya ke issue/pull request. Mode preview menggunakan Carlito agar tersedia jalur kerja tanpa font proprietary.

## Carlito tidak ditemukan

Pasang keluarga Carlito melalui distribusi TeX atau pengelola font sistem yang sesuai, lalu jalankan kembali preview. Perintah `font=auto` membutuhkan setidaknya Calibri atau Carlito yang tersedia; otomatisasi pemilihan bukan pengunduhan font.

## Kelas, gambar, atau berkas bab tidak ditemukan

Periksa bahwa `skripsi.tex`, `filkomskripsi.cls`, dan `metadata.tex` berada pada folder proyek yang benar. Nama berkas pada `\input` dan `\includegraphics` harus cocok persis, termasuk huruf besar/kecil. Pada Overleaf, pilih main document yang berada di folder proyek tersebut.

Hindari path absolut dari komputer pribadi. Gunakan path relatif, misalnya `assets/nama-gambar.png`. Jika gambar tidak digunakan lagi, hapus pemanggilannya dari sumber; menghapus berkas saja akan menyebabkan build gagal.

## Sitasi muncul sebagai key atau referensi hilang

Periksa bahwa key sitasi ada di `bibliography/references.bib`. Jalankan build penuh agar Biber membaca database, lalu periksa log. Gunakan backend Biber yang disediakan template. Petunjuk rinci ada pada [bibliography.md](bibliography.md).

Untuk perubahan besar pada database atau compiler, simpan sumber, bersihkan build lokal, lalu bangun kembali:

```bash
python3 scripts/build.py clean
python3 scripts/build.py preview
```

## Daftar isi, gambar, tabel, atau lampiran belum berubah

Rujukan silang menggunakan berkas bantu dari kompilasi. Jalankan build penuh setelah mengganti judul atau menambah caption/lampiran. Periksa bahwa `\label` unik dan diletakkan setelah `\caption`; periksa pula apakah lampiran dipanggil setelah `\appendix`.

Daftar dapat kosong jika naskah belum mempunyai item jenis tersebut. Jangan mengetik daftar nomor halaman secara manual untuk menutup masalah kompilasi.

## Tabel atau teks melewati margin

Pesan `Overfull \hbox` perlu ditinjau pada PDF dan log. Penyebab yang umum adalah URL panjang, kolom tanpa pemenggalan, persamaan panjang, atau judul. Pecah baris/kolom dengan cara yang sesuai dan atur lebar tabel terhadap `\linewidth`.

Periksa keterbacaan sebelum mengecilkan font seluruh tabel. Jangan mengubah margin naskah untuk menyelesaikan satu tabel tanpa alasan format yang disetujui.

## Jumlah halaman berbeda antara preview dan official

Carlito dan Calibri dapat menghasilkan pemenggalan berbeda. Periksa ulang PDF dengan font akhir, khususnya sampul, heading, tabel/gambar, dan referensi. Nama mode official bukan pengesahan kampus.

## Build Overleaf melewati batas waktu

Periksa gambar yang sangat besar, gambar vektor kompleks, atau proses kompilasi tambahan. Kecilkan aset yang tidak memerlukan resolusi tinggi dan coba build lokal untuk membedakan masalah sumber dari batas runtime layanan. Batas Overleaf mengikuti layanan yang digunakan; template tidak mengubah kuota tersebut.

## Pelaporan masalah

Sertakan versi template, sistem operasi, compiler, perintah build, langkah reproduksi, dan kesalahan pertama. Tambahkan contoh LaTeX minimal atau screenshot bagian format yang bermasalah. Jangan mengunggah naskah lengkap bila tidak perlu; hapus identitas, NIM, tanda tangan, kredensial, serta data penelitian privat.

Gunakan [form issue](https://github.com/Vallykrie/skripsi-filkom-latex/issues/new/choose). Perbedaan terhadap pedoman dilaporkan sebagai permintaan format dengan rujukan, sedangkan build yang gagal dilaporkan sebagai bug.

[Kembali ke README](../README.md)
