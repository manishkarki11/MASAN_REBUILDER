#!/bin/bash

clear
echo -e "\e[91m"
cat << "EOF"
███    ███  █████  ███████  █████  ███    ██ 
████  ████ ██   ██ ██      ██   ██ ████   ██ 
██ ████ ██ ███████ ███████ ███████ ██ ██  ██ 
██  ██  ██ ██   ██      ██ ██   ██ ██  ██ ██ 
██      ██ ██   ██ ███████ ██   ██ ██   ████ 
       MASAN TOOLKIT - Linux Launcher
EOF
echo -e "\e[0m"

echo "[*] Launching MASAN Toolkit..."
sleep 1

python3 core/core.py
