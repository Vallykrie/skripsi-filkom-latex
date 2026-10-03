# Acuan format dan batas kepatuhan

Template ini merupakan implementasi komunitas yang **tidak resmi**. Pedoman kampus, program studi, dan arahan pembimbing mengungguli class ini. `official` adalah nama mode yang mewajibkan Calibri, bukan tanda persetujuan FILKOM.

## Sumber utama

- [Layanan Akademik FILKOM UB](https://filkom.ub.ac.id/pendidikan/layanan-akademik-filkom-ub/), diperiksa 3 Oktober 2026, masih menautkan Buku Panduan Skripsi v3.
- [Panduan Skripsi FILKOM v3.0 — PDF resmi](https://file-filkom.ub.ac.id/fileupload/assets/upload/filemanager/Skripsi/PanduanSkripsiFilkom-v3.0.pdf), dokumen yang digunakan untuk audit format. Dokumen kampus tidak dibundel dalam paket ini.
- Salinan Template Word Skripsi v3.0 yang diaudit dipakai sebagai pembanding pengaturan sampul, halaman awal, dan tipografi; tidak didistribusikan kembali. Ketersediaan unduhan Word terkini belum diverifikasi.
- [Template proposal LaTeX pendamping](https://github.com/Vallykrie/proposal-skripsi-filkom-latex) untuk bentuk naskah proposal Bab 1–3.

## Pemetaan implementasi

| Acuan | Implementasi |
|---|---|
| A4 satu sisi, kiri 4 cm dan sisi lain 3 cm | `geometry` dalam `filkomskripsi.cls` |
| Body Calibri 12 pt, spasi satu, inden 0,6 cm | Mode official, `fontspec`, `setspace`, dan panjang paragraf |
| Bab 16 pt; subbab/subsubbab 14 pt; level berikut 12 pt tebal miring | `titlesec` |
| Sampul SKRIPSI dan pernyataan syarat gelar | `makeskripsicover`, metadata `gelar` |
| Halaman awal Romawi; isi mulai Arab 1 | `skripsifrontmatter` / `skripsimainmatter` |
| Persetujuan sebelum ujian, pengesahan setelah proses disahkan | Berkas frontmatter terpisah dan pilihan input eksplisit |
| Abstrak dua bahasa dan identitas/pembimbing | Contoh halaman abstrak; English language setempat |
| Hasil, Pembahasan, Penutup untuk contoh nonimplementatif | Bab 4–6 bawaan; adaptasi jenis lain dalam customization |
| Caption tabel di atas, gambar di bawah; penomoran per bab | Contoh `table`, `figure`, dan referensi silang |
| Lampiran A/B dan daftar lampiran | `skripsiappendix` dan entri daftar tersendiri |
| Referensi yang disitasi, nama–tahun | Biber dan style `filkom-authoryear` |

Audit contoh Word menemukan margin atas 3,5 cm pada satu section dan heading level 3 berukuran 13 pt. Implementasi mengikuti aturan tertulis panduan, yaitu 3 cm dan 14 pt. Pemeriksaan build/PDF memverifikasi contoh distribusi; penilaian naskah pengguna tetap memerlukan telaah pembimbing.
