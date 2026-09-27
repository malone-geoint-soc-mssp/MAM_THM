# 🛡️ MAM_THM: Threat Hunting & Cybersecurity Lab (Desktop Edition)

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![OS](https://img.shields.io/badge/Environment-Windows%2011%20%7C%20WSL2%20Ubuntu-orange.svg)
![Stack](https://img.shields.io/badge/Stack-Docker%20%7C%20Python3%20%7C%20OpenVPN%20%7C%20Nmap-green.svg)
![Scope](https://img.shields.io/badge/Focus-SOC%20%7C%20TryHackMe%20%7C%20Red%20%26%20Blue%20Team-red.svg)

---

## 🎯 Scope & Purpose
The **MAM_THM** repository is an enterprise-grade, lightweight cybersecurity laboratorial framework designed by **Eng. Malone Manuel**. 

Engineered strictly for execution within an integrated **Windows 11 / WSL2 (Ubuntu) / VSCode / Docker Engine** desktop architecture, this project eliminates high-overhead hypervisors (VMware/VirtualBox) while upholding rigorous technical methodology for Offensive Reconnaissance, Web Application Security, and SOC/MSS Detection operations.

---

## 🏗️ Architecture Stack

| Component | Technical Specification | Operational Purpose |
| :--- | :--- | :--- |
| **Host System** | Windows 11 Desktop (Bare-Metal) | Physical Host, Hardware Virtualization (Hyper-V backend) |
| **Subsystem** | WSL2 (Ubuntu Linux Kernel) | Native Linux CLI execution layer, Networking & Tools Host |
| **IDE** | VSCode + Remote-WSL Extension | Workspace Control, Code Development, Live Debugging |
| **Container Engine**| Docker Engine & Compose | Isolated Vulnerable Targets & SOC Monitoring Instances |
| **Tunneling** | OpenVPN Client | Secure Bridge to External Cyber Ranges (TryHackMe) |

---

## ⚡ Quick Start

### 1. Prerequisites Check
Ensure WSL2 and Docker Engine are operational within your Linux subsystem:
```bash
wsl --status
docker --version