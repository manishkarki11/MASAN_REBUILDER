# core.py
import os
import time
import random
from playsound import playsound

def start_music():
    try:
        playsound("assets/startup.mp3")
    except:
        pass  # If sound module not available

def display_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    with open("banners/ascii_masan.txt", "r", encoding="utf-8") as f:
        banner = f.read()
    for line in banner.splitlines():
        print("\033[91m" + line + "\033[0m")
        time.sleep(0.01)

def main_menu():
    while True:
        print("\n[1] Website Scanner")
        print("[2] Cloudflare Bypass")
        print("[3] Proxy Scraper")
        print("[4] Reverse Shell Generator")
        print("[5] Vulnerability Scanner")
        print("[6] Mass Deface Tool")
        print("[7] Auto Exploiter")
        print("[8] IP Grabber")
        print("[9] Admin Panel")
        print("[0] Exit")
        
        choice = input("\nSelect an Option: ")

        if choice == "1":
            os.system("python3 core/modules/scanner.py")
        elif choice == "2":
            os.system("python3 core/modules/cloudflare_bypass.py")
        elif choice == "3":
            os.system("python3 core/modules/proxy_scraper.py")
        elif choice == "4":
            os.system("python3 core/modules/reverse_shell.py")
        elif choice == "5":
            os.system("python3 core/modules/vuln_scanner.py")
        elif choice == "6":
            os.system("python3 core/modules/mass_deface.py")
        elif choice == "7":
            os.system("python3 core/modules/auto_exploit.py")
        elif choice == "8":
            os.system("python3 core/modules/ip_grabber.py")
        elif choice == "9":
            os.system("python3 core/modules/admin_panel.py")
        elif choice == "0":
            print("Exiting MASAN Toolkit...")
            break
        else:
            print("Invalid Option. Try again!")

if __name__ == "__main__":
    start_music()
    display_banner()
    main_menu()
