# Sitasi dan daftar referensi

Template memakai `biblatex` dengan backend **Biber**. Database berada pada `bibliography/references.bib`; gaya lokal berada pada folder `bibliography/`. Jalur build menjalankan siklus kompilasi yang diperlukan agar sitasi dan daftar referensi terbentuk.

## Menambahkan sumber

1. Peroleh metadata dari halaman penerbit, DOI, katalog, atau sumber asal yang dapat diperiksa.
2. Tambahkan entri BibTeX ke `bibliography/references.bib`.
3. Beri setiap entri key unik dan stabil.
4. Periksa nama penulis, judul, tahun, jenis publikasi, volume/nomor/halaman, DOI, dan URL terhadap sumber aslinya.
5. Gunakan key tersebut dalam isi naskah, lalu kompilasi ulang.

Ekspor dari pengelola referensi membantu memulai, tetapi metadata tetap perlu diperiksa. Jangan memasukkan sumber yang tidak pernah diakses seolah-olah sudah digunakan. Contoh bawaan template menunjukkan sintaks; ganti atau hapus sesuai kebutuhan penelitian Anda.

## Menulis sitasi

Ganti `kunci-sumber` pada contoh berikut dengan key yang benar-benar ada dalam `.bib`:

```latex
\textcite{kunci-sumber} menjelaskan metode tersebut.
Penelitian tersebut memakai evaluasi kronologis \parencite{kunci-sumber}.
\parencite[hlm.~12]{kunci-sumber}
```

Untuk beberapa sumber:

```latex
\parencite{kunci-pertama,kunci-kedua}
```

Jangan mengetik nama penulis dan tahun secara manual untuk menggantikan sitasi yang semestinya dikelola bibliografi. Untuk kutipan langsung, periksa teks dan lokasi sumber; penulis tetap bertanggung jawab atas akurasi kutipan.

## Jenis entri dan kapitalisasi

Gunakan jenis entri yang sesuai: `@article` untuk artikel jurnal, `@book` untuk buku, `@inproceedings` untuk makalah prosiding, `@online` untuk halaman daring, dan jenis lain sesuai sumber. Jenis publikasi yang boleh digunakan dalam penelitian ditentukan pedoman atau protokol Anda, bukan kemampuan template.

Pisahkan penulis dengan `and` pada field `author`. Lindungi singkatan yang harus mempertahankan kapital dengan kurung kurawal, misalnya `{LaTeX}` atau `{API}` di dalam judul. Jangan memakai satu field `author` untuk seluruh daftar nama sebagai teks bebas.

Isi DOI pada field `doi` dan URL pada field `url`; gunakan URL langsung ke sumber, bukan halaman hasil pencarian. Jangan menambahkan DOI atau tanggal akses yang tidak dapat dibuktikan. Field `urldate`, jika diperlukan, menggunakan tanggal akses aktual berformat `YYYY-MM-DD`.

Gunakan `date` atau `year` hanya untuk tahun/tanggal penerbitan yang terverifikasi. Konfigurasi label sitasi tidak memakai `urldate` sebagai pengganti tahun penerbitan; sumber tanpa tanggal tampil dengan `n.d.`. Contoh dokumentasi daring bawaan sengaja tidak mengarang tahun penerbitan.

## Kompilasi dan pemeriksaan

```bash
python3 scripts/build.py preview
python3 scripts/build.py check
```

Setelah mengubah database, jalankan build lagi agar Biber membaca perubahan. Pada Overleaf, pilih XeLaTeX dan kompilasi ulang; lihat [panduan Overleaf](overleaf.md).

Periksa PDF untuk key sitasi yang masih muncul sebagai teks mentah, nama/tahun yang hilang, sumber berulang, serta daftar referensi yang tidak sesuai sumber. Baca log untuk `undefined citations` atau peringatan Biber. Hasil build yang menghasilkan PDF belum tentu memiliki referensi lengkap.

## Mengubah gaya

Perubahan gaya kutipan sebaiknya mengikuti pedoman yang berlaku dan arahan pembimbing. Jangan mengganti `biblatex`/Biber dengan paket lain hanya untuk mengatasi satu entri yang salah. Untuk perubahan gaya lokal, sertakan kasus contoh minimal dan verifikasi sitasi naratif, sitasi dalam kurung, beberapa penulis, DOI/URL, serta daftar referensi.

Jika format yang Anda perlukan belum terakomodasi, gunakan [issue permintaan format](https://github.com/Vallykrie/skripsi-filkom-latex/issues/new/choose) dengan rujukan yang bisa dibaca publik. Untuk kesalahan kompilasi, lihat [troubleshooting.md](troubleshooting.md).

[Kembali ke README](../README.md)
