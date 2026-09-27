#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==============================================================================
PROJETO: MAM_THM
ARQUIVO: scripts/python/validate_env.py
AUTOR: Eng. Malone Manuel
DESCRIÇÃO: Script de auditoria e validação automatizada da Stack Python/WSL2.
==============================================================================
"""

import sys
import shutil

def check_imports():
    """Valida a importação de todas as bibliotecas necessárias no .venv."""
    print("[*] Testando importação de bibliotecas Python no .venv...")
    modules = [
        "requests",
        "urllib3",
        "scapy",
        "paramiko",
        "playwright",
        "bs4",
        "nmap",
        "netifaces"
    ]
    
    for mod in modules:
        try:
            __import__(mod)
            print(f"  [+] Módulo '{mod}': OK")
        except ImportError as err:
            print(f"  [-] FALHA ao importar '{mod}': {err}")

def check_system_binaries():
    """Verifica a presença dos binários nativos no PATH do Linux/WSL2."""
    print("\n[*] Testando binários nativos do sistema no PATH...")
    binaries = ["nmap", "gobuster", "nc", "curl", "git", "tshark", "tcpdump"]
    
    for binary in binaries:
        path = shutil.which(binary)
        if path:
            print(f"  [+] Binário '{binary}': Localizado em {path}")
        else:
            print(f"  [-] Binário '{binary}': NÃO ENCONTRADO no PATH")

if __name__ == "__main__":
    print("=" * 65)
    print("🛡️  MAM_THM - AUDITORIA DE AMBIENTE E TOOLCHAIN")
    print("=" * 65)
    print(f"📌 Interpretador Python Ativo: {sys.executable}\n")
    
    check_imports()
    check_system_binaries()
    
    print("\n" + "=" * 65)
    print("✅ Validação do Módulo 1 Concluída!")
    print("=" * 65)
