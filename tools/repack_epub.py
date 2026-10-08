import zipfile
import os
import sys

def repack_epub(source_dir, output_file):
    if not os.path.exists(source_dir):
        print(f"Error: {source_dir} not found.")
        return

    mimetype_path = os.path.join(source_dir, "mimetype")

    with zipfile.ZipFile(output_file, 'w') as zip_ref:
        # EPUB OCF Spec: 'mimetype' MUST be the first file and stored uncompressed (ZIP_STORED)
        if os.path.exists(mimetype_path):
            zip_ref.write(mimetype_path, "mimetype", compress_type=zipfile.ZIP_STORED)

        for root, dirs, files in os.walk(source_dir):
            # Sort for deterministic packaging
            dirs.sort()
            files.sort()
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_dir)

                # Skip mimetype as it is already written first
                if arcname == "mimetype":
                    continue

                zip_ref.write(file_path, arcname, compress_type=zipfile.ZIP_DEFLATED)

    print(f"Repacked {source_dir} to {output_file} (EPUB 3 compliant)")

if __name__ == "__main__":
    source = "../src/"
    output = "../output/orv_id_translation.epub"

    if len(sys.argv) > 2:
        source = sys.argv[1]
        output = sys.argv[2]

    if not os.path.exists(os.path.dirname(output)):
        os.makedirs(os.path.dirname(output))

    repack_epub(source, output)
