import psutil
import subprocess
import tkinter as tk
from tkinter import ttk, scrolledtext

def get_open_ports():
    connections = psutil.net_connections(kind='inet')
    open_ports = []
    for conn in connections:
        if conn.status == 'LISTEN':
            open_ports.append((conn.laddr.port, conn.pid))
    return open_ports

def get_firewall_ports():
    command = 'netsh advfirewall firewall show rule name=all'
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout

def get_process_name(pid):
    try:
        process = psutil.Process(pid)
        return process.name()
    except psutil.NoSuchProcess:
        return None

def display_info():
    open_ports = get_open_ports()
    firewall_ports = get_firewall_ports()

    open_ports_text.delete(1.0, tk.END)
    firewall_ports_text.delete(1.0, tk.END)

    open_ports_text.insert(tk.END, "Open Ports and Applications:\n")
    for port, pid in open_ports:
        process_name = get_process_name(pid)
        open_ports_text.insert(tk.END, f"Port: {port}, Process ID: {pid}, Application: {process_name}\n")

    firewall_ports_text.insert(tk.END, "Firewall Rules:\n")
    firewall_ports_text.insert(tk.END, firewall_ports)

def search_port():
    port_to_search = int(port_entry.get())
    open_ports = get_open_ports()
    result = "Port not found or not open."
    for port, pid in open_ports:
        if port == port_to_search:
            process_name = get_process_name(pid)
            result = f"Port: {port}, Process ID: {pid}, Application: {process_name}"
            break
    search_result_label.config(text=result)

root = tk.Tk()
root.title("Firewall open ports")

open_ports_frame = ttk.LabelFrame(root, text="Open Ports")
open_ports_frame.pack(fill="both", expand="yes", padx=10, pady=10)

open_ports_text = scrolledtext.ScrolledText(open_ports_frame, wrap=tk.WORD, width=80, height=10)
open_ports_text.pack(padx=10, pady=10)

firewall_ports_frame = ttk.LabelFrame(root, text="Firewall Rules")
firewall_ports_frame.pack(fill="both", expand="yes", padx=10, pady=10)

firewall_ports_text = scrolledtext.ScrolledText(firewall_ports_frame, wrap=tk.WORD, width=80, height=10)
firewall_ports_text.pack(padx=10, pady=10)

search_frame = ttk.LabelFrame(root, text="Search Port")
search_frame.pack(fill="both", expand="yes", padx=10, pady=10)

port_entry = ttk.Entry(search_frame, width=20)
port_entry.pack(side=tk.LEFT, padx=10, pady=10)

search_button = ttk.Button(search_frame, text="Search", command=search_port)
search_button.pack(side=tk.LEFT, padx=10, pady=10)

search_result_label = ttk.Label(search_frame, text="")
search_result_label.pack(side=tk.LEFT, padx=10, pady=10)

refresh_button = ttk.Button(root, text="Refresh", command=display_info)
refresh_button.pack(pady=10)

display_info()

root.mainloop()