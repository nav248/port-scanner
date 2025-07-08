Port Scanner using Python

Overview
The Port Scanner is a command-line tool developed in Python that allows users to scan ports on a given IP address or domain name. It helps identify open ports, which can be useful for basic network vulnerability assessments.

Features

Scans a range of ports (default or custom).

Detects open ports on the given host.

Automatically fetches IP for local scan.

Handles errors like network issues or invalid hosts.

Displays scan start and end time.

Technologies Used
Python: Main programming language.

socket module: Used for making network connections.

datetime module: For displaying the current time.

argparse module: For parsing command-line arguments.

How It Works
The program creates TCP socket connections to ports in the specified range on the target host. If the connection is successful, the port is open. The results are printed directly to the terminal.

How to Run
You can run this script using VS Code Terminal or Command Prompt.

Run with default (localhost):

python port_scanner.py
