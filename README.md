# Firewall Open Ports Scanner 🔥

A simple **Python GUI application** that lists open network ports, displays firewall rules, and allows you to search for specific ports on a Windows system.

# 🚀 Features

- **List Open Ports:** Retrieves ports in the **LISTEN** state along with the corresponding process ID (PID) and application name. ✅
- **Display Firewall Rules:** Uses Windows `netsh` command to fetch and show all firewall rules. ✅
- **Search Specific Port:** Enter a port number to see if it's open and which process is using it. ✅
- **User-friendly GUI:** Built with **Tkinter**, featuring scrollable text boxes for a clean display. ✅

# Prerequisites

- Python 3.x  
- [psutil](https://pypi.org/project/psutil/) module

Install the required dependency using:

```bash
pip install psutil
```

# How to Run
Clone the Repository:
```bash
git clone https://github.com/your-username/firewall-open-ports.git
cd firewall-open-ports
```

# Run the Application:

```bash
python firewall_scanner.py
```

# How It Works
- #### Open Ports: The script uses psutil to fetch all network connections in the LISTEN state and extract port numbers, PIDs, and process names.
- #### Firewall Rules: It runs the Windows netsh advfirewall firewall show rule name=all command via subprocess to retrieve firewall rules.
- #### GUI Display: Results are displayed in a Tkinter window with separate sections for open ports and firewall rules, including a search function for individual ports.

# Important Notes
- *Platform: This tool is designed for Windows due to the use of the netsh command.*
- *Permissions: Some operations (like viewing certain firewall rules) may require administrator privileges.*

# Security Disclaimer
This tool is intended for educational and administrative purposes only. Use responsibly and only on systems you own or have explicit permission to test.

# Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for improvements.
