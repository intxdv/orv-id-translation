#!/usr/bin/env python3
"""
ORV Terminology Lookup & Pre-Flight Entity Harvester.

Usage:
  1. Quick Search:
     python lookup_term.py "Way of the Wind"
     python lookup_term.py "One-eyed Father"

  2. Pre-Flight Batch Harvesting (Scan source chapters for recurring & new entities):
     python lookup_term.py --scan 497
     python lookup_term.py --scan 497 498 499 500
"""

import sys
import os
import re
import glob

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
SRC_DIR = os.path.join(PROJECT_ROOT, "orv-id-translation", "src", "OEBPS")
RAW_SOURCE_DIR = os.path.join(PROJECT_ROOT, "resource", "source-epub", "extracted", "OEBPS")
GLOSSARY_DIR = os.path.join(PROJECT_ROOT, "resource", "glossary")

def search_term(query):
    query_lower = query.lower()
    print(f"\n=======================================================")
    print(f"🔍 Searching ORV Translation Database for: '{query}'")
    print(f"=======================================================")

    # 1. Check constellations.md
    constellations_file = os.path.join(GLOSSARY_DIR, "constellations.md")
    if os.path.exists(constellations_file):
        with open(constellations_file, encoding="utf-8") as f:
            for line in f:
                if query_lower in line.lower() and "|" in line:
                    print(f"[constellations.md] -> {line.strip()}")

    # 2. Check introduced-terms.md
    intro_file = os.path.join(GLOSSARY_DIR, "introduced-terms.md")
    if os.path.exists(intro_file):
        with open(intro_file, encoding="utf-8") as f:
            matches = 0
            for line in f:
                if query_lower in line.lower() and "|" in line:
                    print(f"[introduced-terms.md] -> {line.strip()}")
                    matches += 1
                    if matches >= 5:
                        print("  (...dan entri lainnya)")
                        break

    # 3. Check translated target chapters in src/OEBPS/
    target_matches = []
    target_files = sorted(glob.glob(os.path.join(SRC_DIR, "ch_*.xhtml")), 
                          key=lambda p: int(re.search(r'ch_(\d+)', p).group(1)) if re.search(r'ch_(\d+)', p) else 0)

    for fpath in target_files:
        ch_num = re.search(r'ch_(\d+)', fpath).group(1)
        with open(fpath, encoding="utf-8") as f:
            content = f.read()
        if query_lower in content.lower():
            # Extract sample snippets
            for line in content.splitlines():
                if query_lower in line.lower():
                    clean_line = re.sub(r'<[^>]+>', '', line).strip()
                    if clean_line:
                        target_matches.append((ch_num, clean_line[:120]))
                        break
        if len(target_matches) >= 5:
            break

    if target_matches:
        print(f"\n📖 Ditemukan dalam Naskah Terjemahan ({len(target_matches)} contoh bab):")
        for ch_num, snippet in target_matches:
            print(f"  • Ch {ch_num}: {snippet}")
    else:
        print("\n⚠️ Belum ditemukan dalam naskah terjemahan target.")
    print("-------------------------------------------------------\n")

def scan_source_chapters(chapters):
    print(f"\n=======================================================")
    print(f"🌾 Pre-Flight Entity Harvesting for Chapters: {chapters}")
    print(f"=======================================================")

    all_brackets = set()
    all_quotes = set()

    for ch in chapters:
        ch_clean = str(ch).replace("ch_", "").replace(".xhtml", "")
        src_path = os.path.join(RAW_SOURCE_DIR, f"ch_{ch_clean}.xhtml")
        if not os.path.exists(src_path):
            print(f"❌ File sumber tidak ditemukan: {src_path}")
            continue

        with open(src_path, encoding="utf-8") as f:
            text = f.read()

        # Find brackets [...]
        b_matches = re.findall(r'\[(.*?)\]', text)
        for b in b_matches:
            b_clean = b.strip()
            # Filter noise
            if 3 < len(b_clean) < 80 and not b_clean.isdigit():
                all_brackets.add(b_clean)

        # Find quotes '...'
        q_matches = re.findall(r"['\u2018\u2019]([A-Z][a-zA-Z0-9\s\.\,\?\!\-\:]+?)['\u2018\u2019]", text)
        for q in q_matches:
            q_clean = q.strip()
            if 3 < len(q_clean) < 60:
                all_quotes.add(q_clean)

    # Output formatted table for task Markdown
    print("\n### 📋 Rekomendasi Tabel Istilah (Copy ke tasks/active/):")
    print("| Term Asli (EN) | Padanan Sah / Usulan | Kategori / Sumber |")
    print("| :--- | :--- | :--- |")

    # Check against constellations & intro
    constellations_text = ""
    cpath = os.path.join(GLOSSARY_DIR, "constellations.md")
    if os.path.exists(cpath):
        with open(cpath, encoding="utf-8") as f:
            constellations_text = f.read().lower()

    intro_text = ""
    ipath = os.path.join(GLOSSARY_DIR, "introduced-terms.md")
    if os.path.exists(ipath):
        with open(ipath, encoding="utf-8") as f:
            intro_text = f.read().lower()

    # Prioritize constellation modifiers from brackets
    for item in sorted(all_brackets | all_quotes):
        # Extract modifier if inside "Constellation, '...'"
        modifier_m = re.search(r"Constellation,\s*['\u2018\u2019](.*?)['\u2018\u2019]", item)
        entity_name = modifier_m.group(1) if modifier_m else item

        status = "⚠️ Istilah Baru"
        if entity_name.lower() in constellations_text or entity_name.lower() in intro_text:
            status = "✅ Ada di Glossary"

        print(f"| {entity_name} | **[Tentukan/Cek]** | {status} |")
    print("\n-------------------------------------------------------\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Penggunaan:")
        print("  python lookup_term.py <query>")
        print("  python lookup_term.py --scan <ch_number ...>")
        sys.exit(1)

    if sys.argv[1] == "--scan":
        chapters = sys.argv[2:]
        if not chapters:
            print("Tentukan nomor chapter, contoh: python lookup_term.py --scan 497 498")
            sys.exit(1)
        scan_source_chapters(chapters)
    else:
        query = " ".join(sys.argv[1:])
        search_term(query)
