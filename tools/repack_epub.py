import zipfile
import os
import sys

def repack_epub(source_dir, output_file):
    if not os.path.exists(source_dir):
        print(f"Error: {source_dir} not found.")
        return
    
    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # Ensure the path inside the zip starts from the contents of the dir
                arcname = os.path.relpath(file_path, source_dir)
                zip_ref.write(file_path, arcname)
    
    print(f"Repacked {source_dir} to {output_file}")

if __name__ == "__main__":
    source = "../src/"
    output = "../output/orv_id_translation.epub"
    
    if len(sys.argv) > 2:
        source = sys.argv[1]
        output = sys.argv[2]
        
    if not os.path.exists(os.path.dirname(output)):
        os.makedirs(os.path.dirname(output))
        
    repack_epub(source, output)
