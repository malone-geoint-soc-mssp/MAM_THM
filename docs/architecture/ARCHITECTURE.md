# 🏛️ Master Architecture & Roadmap Document: MAM_THM

* **Project Identifier:** MAM_THM
* **Architect & Instructor:** Eng. Malone Manuel
* **Target Deployment:** Local Bare-Metal WSL2 Subsystem / Docker Engine
* **Compliance Level:** Enterprise Technical Training

---

## 1. Executive Summary & Design Principles

The **MAM_THM** architecture provides a deterministic, repeatable, and non-conflicting laboratorial ecosystem for hands-on cybersecurity instruction.

### Core Architectural Directives:
1. **Zero Hypervisor Overhead:** Elimination of heavy Virtual Machines; reliance on Linux kernel namespaces via WSL2 and OCI-compliant containers via Docker.
2. **Deterministic Port Binding:** Strict mapping strategy preventing conflicts with existing host services (Nginx, PostgreSQL, Kubernetes/k3s).
3. **Dual-Range Capability:** Seamless transition between local containerized targets and remote cyber ranges (TryHackMe via OpenVPN tunneling).
4. **Pedagogical Rigor:** Every practical exercise maps strictly to real-world SOC Operations (Blue Team) and Ethical Hacking/Pentesting (Red Team).

---

## 2. Network Isolation & Port Assignment Matrix

To maintain isolation from host-level daemons, the `MAM_THM` lab environment utilizes the reserved internal bridge network `mam_thm_net` (`172.29.0.0/16`).

```text
[ Windows 11 Host ]
  │
  ├──► OpenVPN Client ───► [ TryHackMe Network (10.10.0.0/16) ]
  │
  └──► [ WSL2 Subsystem (Ubuntu) ]
         │
         ├──► Local Offensive Tools (Nmap, Gobuster, Netcat, Python3)
         │
         └──► [ Docker Engine Bridge: mam_thm_net (172.29.0.0/16) ]
                ├──► Target 1: DVWA Target ───────► Host Binding: 8888 -> 80
                ├──► Target 2: Juice Shop Target ──► Host Binding: 8889 -> 3000
                └──► SOC Tool: Log Monitor ───────► Host Binding: 9091 -> 80

### Port Reservation Table:

| Service | Internal IP | Container Port | Host Bound Port | Protocol | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **DVWA Target** | `172.29.0.10` | 80 | `8888` | TCP | Planned |
| **Juice Shop Target** | `172.29.0.20` | 3000 | `8889` | TCP | Planned |
| **SOC Log Analyzer** | `172.29.0.30` | 80 | `9091` | TCP | Planned |

---

## 3. Pedagogical Matrix & Implementation Roadmap

### 📍 Module 1: Desktop Environment & Subsystem Hardening
* **1.1:** Verification and optimization of WSL2 Linux Kernel parameters (`/etc/wsl.conf`).
* **1.2:** VSCode Integration using `Remote-WSL` IPC sockets.
* **1.3:** Deployment of `docker-compose.yml` with explicit IPAM network definitions.
* **1.4:** Native toolchain installation (`nmap`, `gobuster`, `netcat-traditional`, `curl`, `tshark`).

### 📍 Module 2: Network Engineering & VPN Routing (TryHackMe Bridge)
* **2.1:** OSI vs TCP/IP operational analysis in Linux socket layers.
* **2.2:** Tunneling via OpenVPN inside WSL2 vs Windows Host routing.
* **2.3:** DNS resolution troubleshooting (`/etc/resolv.conf`) and routing tables (`ip route`).

### 📍 Module 3: Reconnaissance, Enumeration & Network Inspection
* **3.1:** Scan methodology using Nmap (TCP SYN `-sS`, Service Detection `-sV`, Script Scanning `-sC`).
* **3.2:** Web Directory Fuzzing via Gobuster/ffuf with custom wordlists.
* **3.3:** Packet Analysis using `tshark` / `tcpdump` directly from the WSL2 interface.

### 📍 Module 4: Web Application Exploitation & Post-Exploitation
* **4.1:** OWASP Top 10 analysis (SQLi, XSS, Broken Access Control) on local Docker targets.
* **4.2:** Execution of practical TryHackMe rooms using local attack suite.
* **4.3:** Evidence capture, artifact hashing (`sha256sum`), and technical reporting.

### 📍 Module 5: Security Automation (Python) & SOC Telemetry
* **5.1:** Python socket programming: Developing a custom multi-threaded Port Scanner (`scanner.py`).
* **5.2:** HTTP Header Parser & Banner Grabber implementation.
* **5.3:** Centralized container log auditing using Docker logging drivers.

---

## 4. Scalability & Cloud Migration Plan

To ensure the repository scales from a local desktop workstation to cloud environments without architectural modification:

1. **Phase 1 (Bare-Metal Local):** WSL2 + Docker Desktop (Current Phase).
2. **Phase 2 (Cloud Workspace):** Deployment to **GitHub Codespaces** using `.devcontainer` configuration.
3. **Phase 3 (Remote Cyber Range):** Deployment of targets on AWS EC2 / DigitalOcean Droplet via `docker-compose`.
