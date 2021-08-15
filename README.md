# PyShell

## What is it?

A semi-interactive reverse shell for **Windows**, written in python.

## How does it work?

PyShell uses sockets to connect over TCP to the IP address and port specified. When commands are received, PyShell interprets those commands and either uses the ```os``` module or the ```subprocess``` module to perform operations.
