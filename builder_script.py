# builder_script.py
import os
import zipfile
import shutil

def zip_folder(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)

def build_toolkit():
    print("[+] Starting MASAN Toolkit Builder...")

    # Create temporary working directory
    temp_dir = "MASAN_TOOLKIT_FINAL"
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)

    # Copy toolkit files
    print("[+] Copying toolkit files...")
    shutil.copytree('toolkit_files', os.path.join(temp_dir, 'core'))

    # Copy launcher scripts
    print("[+] Copying launcher files...")
    shutil.copytree('launchers', os.path.join(temp_dir, 'launchers'))

    # Add readme
    with open(os.path.join(temp_dir, 'README.txt'), 'w') as f:
        f.write("MASAN Ultimate Toolkit\nBuilt by MASAN\n")

    # Zip the toolkit
    print("[+] Creating MASAN_TOOLKIT_FINAL.zip...")
    zip_folder(temp_dir, 'MASAN_TOOLKIT_FINAL.zip')

    # Clean up
    shutil.rmtree(temp_dir)

    print("[+] Build complete! Toolkit saved as MASAN_TOOLKIT_FINAL.zip.")

if __name__ == "__main__":
    build_toolkit()
