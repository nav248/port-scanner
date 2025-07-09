Port Scanner using Python

Overview:

The Port Scanner is a command-line tool developed in Python that allows users to scan ports on a given IP address or domain name. It helps identify open ports, which can be useful for basic network vulnerability assessments.

Features:

1.Scans a range of ports (default or custom).

2.Detects open ports on the given host.

3.Automatically fetches IP for local scan.

4.Handles errors like network issues or invalid hosts.

5.Displays scan start and end time.

Technologies Used:

1.Python - Main programming language.

2.socket module - Used for making network connections.

3.datetime module - For displaying the current time.

4.argparse module - For parsing command-line arguments.

How It Works:

The program creates TCP socket connections to ports in the specified range on the target host. If the connection is successful, the port is open. The results are printed directly to the terminal.

How to Run:

Run with default (localhost):

python port_scanner.py
