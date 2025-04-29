# builder_premium.py
import os
import zipfile
import shutil
import time
import random
import string

ADMIN_PASSWORD = "masanadmin"  # Important!

def random_string(length=10):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def encrypt_file(filepath):
    try:
        with open(filepath, 'rb') as f:
            content = f.read()
        encrypted = bytearray(b ^ 0x42 for b in content)
        with open(filepath, 'wb') as f:
            f.write(encrypted)
    except Exception as e:
        print(f"[!] Failed to encrypt {filepath}: {e}")

def zip_folder(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if not file.endswith('.dummy'):
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, folder_path)
                    zipf.write(file_path, arcname)

def build_toolkit():
    print("[+] MASAN Premium Builder Starting...")
    
    password = input("Enter Admin Password to Build: ")
    if password != ADMIN_PASSWORD:
        print("[!] Unauthorized Access! Exiting...")
        return
    
    # Setup
    temp_dir = "MASAN_TOOLKIT_FINAL"
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)
    
    print("[+] Copying toolkit files...")
    shutil.copytree('toolkit_files', os.path.join(temp_dir, 'core'))
    shutil.copytree('launchers', os.path.join(temp_dir, 'launchers'))
    
    # Create dummy files
    print("[+] Creating dummy anti-scan files...")
    dummy_folder = os.path.join(temp_dir, 'decoys')
    os.makedirs(dummy_folder)
    for i in range(10):
        with open(os.path.join(dummy_folder, random_string(12)+'.dummy'), 'w') as f:
            f.write("This is a dummy harmless file. Ignore.")

    # Encrypt core scripts
    print("[+] Encrypting core scripts...")
    core_scripts = [
        os.path.join(temp_dir, 'core', 'core.py'),
        os.path.join(temp_dir, 'core', 'settings.py')
    ]
    for script in core_scripts:
        encrypt_file(script)

    # Obfuscate timestamps
    print("[+] Obfuscating timestamps...")
    current_time = time.time() - random.randint(100000, 10000000)
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            file_path = os.path.join(root, file)
            os.utime(file_path, (current_time, current_time))

    # Zip the final package
    print("[+] Creating final MASAN_TOOLKIT_FINAL.zip...")
    zip_folder(temp_dir, 'MASAN_TOOLKIT_FINAL.zip')

    # Self-clean
    shutil.rmtree(temp_dir)

    print("[+] MASAN PREMIUM TOOLKIT BUILT SUCCESSFULLY!")

if __name__ == "__main__":
    build_toolkit()
