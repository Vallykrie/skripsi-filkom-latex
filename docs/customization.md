# Menyesuaikan naskah skripsi

## Metadata dan sampul

Ubah judul dan identitas di `metadata.tex`, bukan langsung pada sampul atau kelas. Konfigurasi memakai `\filkomsetup{...}`:

```latex
\filkomsetup{
  judul={Judul Skripsi Anda},
  judul-inggris={Your Thesis Title},
  nama={Nama Lengkap Anda},
  nim={NIM Anda},
  program-studi={PROGRAM STUDI ANDA},
  departemen={DEPARTEMEN ANDA},
  fakultas={FAKULTAS ILMU KOMPUTER},
  universitas={UNIVERSITAS BRAWIJAYA},
  gelar={Sarjana Komputer},
  kota={MALANG},
  tahun={2026},
  pembimbing-1={Nama dan Gelar Pembimbing 1},
  pembimbing-2={Nama dan Gelar Pembimbing 2}
}
```

Sesuaikan tahun dengan naskah Anda. Pertahankan konfigurasi logo yang sudah ada jika digunakan; status aset Universitas Brawijaya dijelaskan dalam [`NOTICE`](../NOTICE). Lisensi kode template tidak otomatis menjadi lisensi logo.

Judul panjang akan terbungkus berdasarkan tata letak. Periksa hasilnya sebelum menambah pemenggalan manual; gunakan keputusan tata tulis yang disetujui pembimbing.

## Font

Kelas menyediakan pilihan font `auto`, `carlito`, dan `calibri`. Contoh untuk pratinjau dengan font terbuka:

```latex
\documentclass[font=carlito]{filkomskripsi}
```

Dengan `font=auto`, kelas mencoba Calibri lalu Carlito. Skrip `preview` memilih Carlito, sedangkan skrip `official` mensyaratkan Calibri. Jika menggunakan instalasi font lokal, pastikan keluarga Calibri tersedia bagi XeLaTeX.

Untuk berkas font pada proyek privat, tambahkan key berikut pada `\filkomsetup` di `metadata.tex`:

```latex
font-dir={fonts/},
```

Folder tersebut harus berisi `calibri.ttf` (regular), `calibrib.ttf` (bold), `calibrii.ttf` (italic), dan `calibriz.ttf` (bold italic) yang memang boleh Anda gunakan. Pilih `font=calibri` untuk meminta keluarga tersebut secara eksplisit. Folder `fonts/` diabaikan Git dan paket ZIP publik template; jangan menambahkan berkas proprietary ke repository publik.

Pergantian font dapat mengubah jumlah halaman dan pemenggalan tabel. Build dengan Calibri tidak membuktikan persetujuan akademik; naskah tetap perlu diperiksa terhadap ketentuan yang berlaku.

## Halaman awal

Folder `frontmatter/` memisahkan lembar persetujuan, orisinalitas, prakata, abstrak Indonesia, dan abstrak Inggris. Isi abstrak berdasarkan penelitian yang benar-benar dilakukan. Periksa kembali panjang abstrak dan jumlah kata kunci berdasarkan pedoman Anda.

Lembar persetujuan dan pernyataan orisinalitas perlu diisi sesuai proses nyata. Jangan membuat tanda tangan, nama penguji, tanggal ujian, atau status pengesahan fiktif. Template memakai lembar persetujuan secara default. Setelah ujian/revisi benar-benar disahkan, ganti pemanggilan persetujuan pada `skripsi.tex` dengan `\input{frontmatter/pengesahan}` yang disediakan terpisah dan awalnya dikomentari. Isi form, termasuk NIP jika diminta, berdasarkan ketentuan kampus; jangan menambahkan kedua form sekaligus tanpa arahan. Jika format halaman awal yang diminta fakultas berbeda, dokumentasikan rujukannya ketika mengusulkan penyesuaian template.

## Bab nonimplementatif

Struktur awal mempunyai enam bab:

| Bab | Kerangka isi |
|---|---|
| 1. Pendahuluan | Latar belakang, rumusan masalah, tujuan, manfaat, dan batasan |
| 2. Landasan Kepustakaan | Penelitian terdahulu serta konsep dan metode yang digunakan |
| 3. Metodologi | Rancangan penelitian, data, prosedur, dan evaluasi |
| 4. Hasil | Temuan penelitian, tabel, gambar, dan keluaran analisis |
| 5. Pembahasan | Interpretasi hasil, hubungan dengan literatur, dan keterbatasan |
| 6. Penutup | Kesimpulan yang menjawab rumusan masalah dan saran |

Ini kerangka awal untuk disepakati, bukan penetapan struktur bagi seluruh program studi. Teks contoh perlu diganti; jangan menyajikannya sebagai penelitian Anda.

## Menyesuaikan penelitian implementatif

Kelas tidak memerlukan versi tambahan untuk mengganti struktur bab. Edit judul `\chapter{...}`, isi `chapters/`, serta urutan `\input{...}` pada `skripsi.tex` sesuai struktur yang disetujui pembimbing.

Sebagai contoh pembagian kerja penulisan, penelitian implementatif dapat memisahkan analisis/perancangan, implementasi, dan pengujian/evaluasi. Jumlah bab dan nama bab mengikuti pedoman serta kebutuhan penelitian; contoh tersebut bukan klaim format resmi. Metodologi tetap perlu menjelaskan prosedur, dan pengujian tetap perlu menyajikan bukti aktual.

Jika menambah bab, letakkan `\input{chapters/nama-berkas}` sebelum daftar referensi. Penomoran akan mengikuti urutan `\chapter`. Jangan menuliskan nomor bab secara manual pada judul.

Pemeriksaan struktur bawaan menguji contoh enam bab yang disertakan. Jika Anda mengubah jumlah/nama berkas atau jenis penelitian, sesuaikan pula pemeriksaan contoh agar menguji struktur baru yang memang Anda pilih; pertahankan pemeriksaan metadata, referensi, aset, dan build yang masih relevan. Perubahan lokal tersebut tidak otomatis menjadi struktur baku untuk semua pengguna template.

## Tabel, gambar, persamaan, dan rujukan

Gunakan caption serta label yang unik. Letakkan `\label` setelah `\caption` pada tabel/gambar. Contoh rujukan:

```latex
Tabel~\ref{tab:contoh} menyajikan hasil pengamatan.
Gambar~\ref{fig:contoh} menunjukkan rancangan penelitian.
```

Simpan gambar pada `assets/` dan gunakan path relatif. Pilih gambar dengan resolusi yang cukup serta hak penggunaan yang jelas. Hindari memperkecil tabel sampai sulit dibaca; ubah pemenggalan kolom atau susun penyajian ulang terlebih dahulu.

## Daftar lampiran

Tambahkan lampiran setelah `\appendix` pada `skripsi.tex`. Gunakan berkas terpisah di `appendices/` dan perintah bab lampiran yang digunakan contoh bawaan. Setelah menambah lampiran, kompilasi ulang dan periksa daftar lampiran serta urutan hurufnya.

Lampiran mendukung naskah; ia tidak menggantikan penyajian hasil utama. Jangan memasukkan kata sandi, identitas pihak lain, data berlisensi terbatas, atau tanda tangan yang tidak perlu dalam salinan publik.

## Mengubah tata letak kelas

Sebelum mengubah margin, font, heading, atau spasi dalam `filkomskripsi.cls`, pastikan ada alasan format yang jelas. Buat perubahan kecil, jalankan build/pengujian, dan periksa halaman terdampak. Untuk usulan perubahan lintas pengguna, ikuti [CONTRIBUTING.md](../CONTRIBUTING.md) dan sertakan rujukan pedoman.

[Kembali ke README](../README.md)
