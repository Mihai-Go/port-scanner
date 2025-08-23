# Python Port Scanner

A simple Python tool for scanning open TCP ports on a target host.  
Perfect for beginners in cybersecurity to learn the basics of networking and Python scripting.

## Features

- Scan any IP address or domain name
- Specify any set of ports to scan
- Shows which ports are OPEN or CLOSED

## How to Use

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Mihai-Go/port-scanner.git
    cd port-scanner
    ```

2. **Run the script:**
    ```bash
    python3 port_scanner.py
    ```

3. **Follow the prompts:**
    - Enter the IP or domain you want to scan (e.g., `scanme.nmap.org`)
    - Enter the ports to scan, separated by commas (e.g., `22,80,443`)

## Example Output

```
Enter IP or domain to scan: scanme.nmap.org
Enter ports to scan (comma-separated, e.g. 22,80,443): 22,80,443
Scanning scanme.nmap.org...
Port 22: OPEN
Port 80: OPEN
Port 443: CLOSED
```

## Learning Outcomes

- Basic socket programming in Python
- Understanding how TCP connections work
- User input and output formatting

## Next Steps

- Automatically scan a range of ports (e.g., 1-1024)
- Show service names for common ports
- Save results to a file


**Made by Mihai-Go**
