# AI-Assisted Content & Tooling Disclosure

> **SPDX Provenance Classification**: `ai-assisted`  
> **Human Governance Model**: Human-in-the-Loop (HITL)  
> **Terakhir Diperbarui**: 2026-10-30

Dokumen ini memuat transparansi mengenai penggunaan kecerdasan buatan (*Artificial Intelligence*) dalam proyek alih bahasa penggemar **Omniscient Reader's Viewpoint (ORV) Indonesian Translation**.

---

## 1. Filosofi & Batasan Peran (Human-in-the-Loop)

Proyek ini menjunjung tinggi kualitas sastra dan keaslian karya. AI **bukan** pengganti penerjemah dan **bukan** alat penerjemahan mesin mentah (*raw machine translation* / MTL tanpa kurasi).

Seluruh alur kerja menerapkan prinsip ketat **Human-in-the-Loop**:
- **Arah Artistik & Kurasi Bahasa**: Seluruh penentuan gaya bahasa, *tone* puitis narasi, adaptasi kultural Korea, serta keputusan redaksional berada 100% di bawah kendali dan tanggung jawab **Lead Translator (slvgnt—Taki)**.
- **Hak Veto & Verifikasi**: Setiap kalimat, istilah, dan catatan kaki (*footnote*) melewati tahap peninjauan manual sebelum dinyatakan layak masuk ke dalam edisi rilis EPUB.

---

## 2. Pemanfaatan Teknologi AI

Kecerdasan buatan (menggunakan Google Gemini melalui platform *agentic IDE* Antigravity) difungsikan secara spesifik sebagai **Computer-Assisted Translation (CAT) & Engineering Assistant** untuk:

1. **Akselerasi Draf & Pengecekan Grammar**:
   - Membantu penyusunan draf awal alih bahasa dari teks sumber bahasa Inggris.
   - Menyempurnakan struktur kalimat agar luwes dan sesuai kaidah tata bahasa Indonesia yang baik tanpa menghilangkan nuansa asli.
2. **Penegakan Konsistensi Glosarium (Terminology Enforcement)**:
   - Memastikan nama-nama Konstelasi, istilah skenario, dan deskripsi kemampuan (*skills*) patuh pada konvensi hibrida proyek (`glossary-main.md`, `constellations.md`, dan `introduced-terms.md`).
3. **Automated Quality Control (QC)**:
   - Menjalankan skrip validasi integritas struktur XHTML, validasi pasangan pop-up footnote EPUB 3 (`epub:type="noteref"` dan `epub:type="footnote"`), serta mendeteksi kata-kata terlarang secara otomatis.
4. **Automasi Build & Packaging**:
   - Mengelola kompilasi deterministik berkas EPUB sesuai spesifikasi standar IDPF / W3C EPUB 3.

---

## 3. Hak Cipta & Etika

- **Karya Asli**: *Omniscient Reader's Viewpoint* (전지적 독자 시점) adalah milik sah penulis **Sing Shong** (싱숑) dan ilustrator **Black Box** (검넴).
- **Proyek Non-Profit**: Proyek ini dikerjakan secara sukarela, nirlaba, dan didistribusikan gratis untuk sesama penggemar di Indonesia.
- **Kerahasiaan & Data**: Alur kerja tidak menggunakan data pribadi atau data privat di luar repositori publik proyek.

---

Untuk pertanyaan lebih lanjut mengenai tata kelola proyek atau pelaporan kesalahan terjemahan, silakan buka tiket melalui [GitHub Issues](https://github.com/intxdv/orv-id-translation/issues).
