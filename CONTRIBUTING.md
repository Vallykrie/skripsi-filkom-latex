# Berkontribusi

Terima kasih telah membantu template skripsi LaTeX FILKOM UB. Kontribusi yang berguna meliputi perbaikan kompilasi, contoh penggunaan, dokumentasi, aksesibilitas penyajian, dan penyesuaian format yang mempunyai rujukan jelas.

## Melaporkan masalah

- Gunakan [form bug atau permintaan format](https://github.com/Vallykrie/skripsi-filkom-latex/issues/new/choose).
- Untuk bug, berikan contoh minimal, versi template, lingkungan, perintah build, dan pesan kesalahan pertama.
- Untuk perbedaan format, sertakan rujukan pedoman, tanggal/versinya, halaman/subbab, hasil aktual, dan hasil yang diharapkan.
- Jangan menyebut format sebagai ketentuan resmi tanpa rujukan. Bila arahan hanya berlaku pada satu pembimbing/program studi, jelaskan cakupannya.
- Hapus data pribadi, tanda tangan, kata sandi, dan materi penelitian terbatas dari log, screenshot, serta contoh.

## Mengirim pull request

1. Buat branch untuk satu perubahan yang jelas.
2. Pertahankan contoh naskah generik; jangan memakai skripsi pribadi sebagai fixture publik.
3. Sertakan dokumentasi untuk opsi baru atau perubahan perilaku build.
4. Jalankan pemeriksaan dari akar repository:

   ```bash
   make test
   make preview
   make check
   ```

5. Periksa PDF secara visual pada halaman terdampak. Untuk perubahan font atau halaman awal, periksa sampul, persetujuan, abstrak, dan daftar.
6. Jelaskan masalah, perubahan, serta hasil pemeriksaan dalam deskripsi pull request. Catat pemeriksaan yang tidak dijalankan beserta alasannya; jangan menyatakan lulus tanpa bukti.

Build Calibri hanya dijalankan jika font tersedia secara legal. Tidak tersedianya Calibri dapat dicatat secara terbuka; jangan menambahkan font proprietary untuk membuat pemeriksaan lolos. Logo Universitas Brawijaya dan aset pihak ketiga mengikuti [`NOTICE`](NOTICE).

## Lisensi dan lingkup

Kontribusi kode serta dokumentasi harus dapat dirilis di bawah [`LICENSE`](LICENSE), LPPL 1.3c atau versi lebih baru. Ikuti ketentuan lisensi, termasuk penanganan karya yang dimodifikasi. Jangan memasukkan aset yang tidak mempunyai hak penggunaan/distribusi yang sesuai.

Template ini tidak menjadi pengesahan akademik. Perubahan format ditinjau terhadap rujukan dan dampaknya pada pengguna; kebutuhan satu naskah dapat didokumentasikan sebagai penyesuaian lokal daripada dijadikan aturan bagi semua pengguna.
