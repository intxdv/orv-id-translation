#!/usr/bin/env python3
"""
ORV Batch Quality Control (QC) Automated Validator.

Validates:
  1. Footnote Integrity (EPUB 3 <sup> noteref vs <aside> footnote pairs)
  2. Forbidden Terms ("Bab", "Rasi Bintang", "Dongeng", "Mas/Mbak")
  3. Untranslated English Leftovers
  4. Tag Integrity (unclosed <p>, <i>, <b>, <fieldset>)

Usage:
  python qc_batch.py 95
  python qc_batch.py --file ch_495.xhtml ch_496.xhtml
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
MANIFEST_PATH = os.path.join(PROJECT_ROOT, "resource", "project-manifest.md")

FORBIDDEN_PATTERNS = [
    (re.compile(r'\bBab\s+\d+', re.IGNORECASE), "Penggunaan kata 'Bab' (Wajib gunakan 'Chapter')"),
    (re.compile(r'\bRasi\s+Bintang\b', re.IGNORECASE), "Penggunaan 'Rasi Bintang' (Wajib 'Konstelasi')"),
    (re.compile(r'\bDongeng\b', re.IGNORECASE), "Penggunaan 'Dongeng' (Wajib 'Kisah')"),
    (re.compile(r'\b(Mas|Mbak)\s+[A-Z]', re.IGNORECASE), "Penggunaan honorifik lokal 'Mas/Mbak' (Wajib honorifik Korea, e.g. -ssi)"),
]

def get_chapters_for_batch(batch_num):
    chapters = []
    if not os.path.exists(MANIFEST_PATH):
        print(f"❌ Manifest tidak ditemukan di: {MANIFEST_PATH}")
        return chapters

    pattern = re.compile(rf'\|\s*(ch_\d+\.xhtml)\s*\|.*?\|\s*COMPLETED\s*\|\s*.*?(?:Batch\s*{batch_num}|B{batch_num})\b', re.IGNORECASE)
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        for line in f:
            m = pattern.search(line)
            if m:
                chapters.append(m.group(1))

    # Fallback to search any mention of Batch in line
    if not chapters:
        with open(MANIFEST_PATH, encoding="utf-8") as f:
            for line in f:
                if f"Batch {batch_num}" in line or f"B{batch_num}" in line:
                    m = re.search(r'ch_\d+\.xhtml', line)
                    if m:
                        chapters.append(m.group(0))
    return sorted(list(set(chapters)))

def validate_file(fpath):
    fname = os.path.basename(fpath)
    issues = []

    with open(fpath, encoding="utf-8") as f:
        lines = f.readlines()
    content = "".join(lines)

    # 1. Footnote Integrity
    sup_refs = set(re.findall(r'<sup\s+id=["\']fn(\d+)-ref["\']', content))
    aside_fns = set(re.findall(r'<aside\s+id=["\']fn(\d+)["\']', content))

    orphaned_sups = sup_refs - aside_fns
    orphaned_asides = aside_fns - sup_refs

    if orphaned_sups:
        issues.append(f"Footnote <sup> tanpa <aside> pasangan: fn{', fn'.join(sorted(orphaned_sups))}")
    if orphaned_asides:
        issues.append(f"Footnote <aside> tanpa <sup> pemanggil: fn{', fn'.join(sorted(orphaned_asides))}")

    # Check EPUB 3 epub:type attributes
    for m in re.finditer(r'<aside\s+id=["\']fn\d+["\']([^>]*)>', content):
        if 'epub:type="footnote"' not in m.group(1):
            issues.append(f"Tag <aside> tidak memiliki atribut epub:type=\"footnote\"")
            break

    # 2. Forbidden Patterns & Line Checks
    for idx, line in enumerate(lines, start=1):
        for pattern, desc in FORBIDDEN_PATTERNS:
            if pattern.search(line):
                # Ignore if it's within Catatan footnote explanation of origin
                if "Catatan [" in line and "Dongeng" in line:
                    continue
                issues.append(f"Baris {idx}: {desc} -> '{line.strip()[:80]}'")

        # 3. Detect raw English leftovers in paragraphs
        if line.strip().startswith("<p>") and line.strip().endswith("</p>"):
            clean_text = re.sub(r'<[^>]+>', '', line).strip()
            # If paragraph has > 8 English words like "The Constellations looked at..."
            en_words = re.findall(r'\b(the|and|of|to|in|is|you|that|it|he|was|for|on|are|as|with|his|they|at)\b', clean_text, re.IGNORECASE)
            id_words = re.findall(r'\b(dan|yang|di|ke|dari|ini|itu|dia|aku|mereka|adalah|untuk|pada|dengan|tidak|bisa|akan)\b', clean_text, re.IGNORECASE)
            if len(en_words) > 6 and len(id_words) == 0 and len(clean_text) > 40:
                issues.append(f"Baris {idx}: Terdeteksi sisa teks Bahasa Inggris tanpa terjemahan -> '{clean_text[:70]}...'")

    # 4. Check unclosed common tags
    for tag in ['p', 'i', 'b', 'fieldset']:
        opens = len(re.findall(rf'<{tag}\b[^>]*>', content))
        closes = len(re.findall(rf'</{tag}>', content))
        if opens != closes:
            issues.append(f"Jumlah tag <{tag}> ({opens}) tidak sama dengan penutup </{tag}> ({closes})")

    return issues

def run_qc_batch(batch_num=None, explicit_files=None):
    if explicit_files:
        target_files = [os.path.join(SRC_DIR, f) if not os.path.isabs(f) else f for f in explicit_files]
        batch_label = "Custom File Selection"
    else:
        chapters = get_chapters_for_batch(batch_num)
        if not chapters:
            print(f"❌ Tidak ada chapter yang ditemukan untuk Batch {batch_num} di manifest.")
            return False
        target_files = [os.path.join(SRC_DIR, ch) for ch in chapters]
        batch_label = f"Batch {batch_num} ({', '.join(chapters)})"

    print(f"\n=======================================================")
    print(f"🛡️ Running Automated QC for: {batch_label}")
    print(f"=======================================================")

    total_issues = 0
    for fpath in target_files:
        fname = os.path.basename(fpath)
        if not os.path.exists(fpath):
            print(f"\n❌ [{fname}] File tidak ditemukan di {fpath}")
            total_issues += 1
            continue

        issues = validate_file(fpath)
        if issues:
            print(f"\n❌ [{fname}] DITEMUKAN {len(issues)} ISU:")
            for issue in issues:
                print(f"   • {issue}")
            total_issues += len(issues)
        else:
            print(f"✅ [{fname}] LULUS (Semua kriteria valid)")

    print(f"\n-------------------------------------------------------")
    if total_issues == 0:
        print(f"🎉 STATUS: PASSED (100% Lulus QC - Siap Masuk Review)")
        print(f"-------------------------------------------------------\n")
        return True
    else:
        print(f"⚠️ STATUS: FAILED ({total_issues} isu perlu diperbaiki sebelum review)")
        print(f"-------------------------------------------------------\n")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Penggunaan:")
        print("  python qc_batch.py <batch_number>")
        print("  python qc_batch.py --file ch_XXX.xhtml ...")
        sys.exit(1)

    if sys.argv[1] == "--file":
        run_qc_batch(explicit_files=sys.argv[2:])
    else:
        batch_arg = sys.argv[1].replace("B", "").replace("b", "")
        run_qc_batch(batch_num=batch_arg)
