<div align="center">
  <img src="ORV.png" width="100%" alt="ORV Banner" />
  <br> <br>
  
  # [ OMNISCIENT READER'S VIEWPOINT ]
  ### — Indonesian Fan-Translation —

  [![Status: Ongoing](https://img.shields.io/badge/Status-Ongoing-blue?style=flat-square)](#)
  [![Language: Indonesian](https://img.shields.io/badge/Language-Indonesian-red?style=flat-square)](#)
  [![Workflow: AI--Assisted](https://img.shields.io/badge/Workflow-AI--Assisted-8A2BE2?style=flat-square)](AI-DISCLOSURE.md)
  [![Supervision: Human--in--the--Loop](https://img.shields.io/badge/Supervision-Human--in--the--Loop-success?style=flat-square)](AI-DISCLOSURE.md)
  [![License: MIT (Tools)](https://img.shields.io/badge/License-MIT%20(Tools)-green?style=flat-square)](LICENSE)

  *"Kisah ini ditujukan bagi satu orang pembaca yang terus bertahan hingga akhir."*
</div>

---

## 📖 Tentang Proyek
Selamat datang di repositori proyek translasi **Omniscient Reader's Viewpoint (ORV)**. Proyek ini adalah sebuah **mini project** yang dikerjakan secara personal untuk menerjemahkan webnovel legendaris ini ke dalam Bahasa Indonesia dengan kualitas yang detail dan tetap mempertahankan nuansa aslinya.

Proyek ini menggunakan alur kerja modern berbasis Markdown untuk memastikan fleksibilitas dalam proses penerjemahan dan kemudahan dalam pembuatan file EPUB akhir.

## 🛠️ Tim & Kolaborasi
- **Lead Translator**: **slvgnt—Taki**
- **Alur Kerja & Engineering**: *Computer-Assisted Translation* (CAT) & *Agentic Tooling* untuk konsistensi glosarium serta kendali mutu otomatis — baca rincian transparansi di [AI-DISCLOSURE.md](AI-DISCLOSURE.md).

## 📁 Struktur Repositori

```
orv-id-translation/
├── assets/                  # Gambar, sampul, dan aset visual
│   ├── cover.jpg
│   ├── cover-p1-v1.jpg
│   ├── stigma.png
│   └── style.css
├── content/                 # Draft translasi per-chapter (Markdown)
│   └── 00-intro.md
├── src/                     # Berkas EPUB siap-pakai
│   ├── META-INF/
│   │   └── container.xml
│   ├── OEBPS/
│   │   ├── images/
│   │   ├── intro.xhtml
│   │   ├── ch_1.xhtml ~ ch_551.xhtml
│   │   ├── afterword.xhtml
│   │   ├── content.opf
│   │   ├── toc.html
│   │   └── toc.ncx
│   ├── metadata.yaml
│   └── mimetype
├── tools/                   # Skrip bantu & kendali mutu (Python)
│   ├── lookup_term.py
│   ├── qc_batch.py
│   ├── repack_epub.py
│   └── unzip_epub.py
├── build/                   # Output build sementara
├── output/                  # File EPUB final siap dibaca
├── AI-DISCLOSURE.md         # Deklarasi transparansi penggunaan AI (Human-in-the-Loop)
├── LICENSE                  # Ketentuan penggunaan & lisensi alat bantu
└── README.md
```

## 📜 Kredit & Disklaimer
- **Penulis**: Sing Shong (싱숑)
- **Ilustrasi**: Black Box (검넴)
- **Sumber Terjemahan EN**: Komunitas penggemar internasional ([ORV Community Translation Project](https://discord.gg/CZdNvKaNNr))
- **Discord Komunitas EN**: [discord.gg/CZdNvKaNNr](https://discord.gg/CZdNvKaNNr)

> [!IMPORTANT]
> Proyek ini murni bersifat **non-profit** oleh penggemar untuk penggemar. Hak cipta sepenuhnya milik penulis asli. Harap dukung penulis melalui platform resmi jika memungkinkan. Rincian ketentuan lisensi dapat dilihat di berkas [LICENSE](LICENSE).

## 📖 Rekomendasi Aplikasi Pembaca (E-Reader)
Untuk menikmati pengalaman membaca terbaik (termasuk kompatibilitas HTML5 dan fitur interaktif *pop-up footnote* EPUB 3):

- **Android**: **Moon+ Reader Pro** (Aktifkan opsi *Pop-up footnote* pada menu *Miscellaneous*).
- **iOS / iPadOS / macOS**: **Apple Books** (Mendukung pop-up footnote secara *native*).
- **Windows / Linux**: **Thorium Reader** atau **Calibre** (E-book Viewer).
- **Web & Multi-platform (Semua Perangkat)**: **Readest** ([web.readest.com/reader](https://web.readest.com/reader/)) — pembaca EPUB *open-source* modern yang dapat diakses langsung melalui peramban web tanpa instalasi, maupun dipasang di berbagai platform (Android, iOS, Windows, macOS, Linux).

## 🐛 Laporan Kesalahan
Menemukan typo, istilah yang kurang tepat, atau masalah lain? Silakan buat laporan di:

👉 [github.com/intxdv/orv-id-translation/issues](https://github.com/intxdv/orv-id-translation/issues)

---

<div align="center">
  <img src="assets/stigma.png" width="30%" alt="Stigma Icon" />
  <br> <br>
  <i>Dibuat dengan dedikasi untuk satu-satunya pembaca.</i>
  <br> <br>
<!--
  <img
    src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGZhMjJhY2Vxb25lZ2t3N2pnenRtb2J0bTN2cHBocHpubjF3OWR0biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/zhQzdP7FLELaHlQ5kl/giphy.gif"
    style="width: 250px;"
  />

-->
</div>
