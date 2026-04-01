import zipfile
import os
import sys

def unzip_epub(epub_path, extract_to):
    if not os.path.exists(epub_path):
        print(f"Error: {epub_path} not found.")
        return
    
    with zipfile.ZipFile(epub_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted {epub_path} to {extract_to}")

if __name__ == "__main__":
    # Default paths for this project
    source = "../../resource/source-epub/orv_main.epub"
    target = "../src/"
    
    if len(sys.argv) > 2:
        source = sys.argv[1]
        target = sys.argv[2]
        
    unzip_epub(source, target)
