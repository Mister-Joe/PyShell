# PyShell

## What is it?

A semi-interactive reverse shell for **Windows**, written with Python.

## How does it work?

PyShell uses the ```socket``` module to connect over TCP to the IP address and port specified. When commands are received, PyShell interprets those commands and either uses the ```os``` module or the ```subprocess``` module to perform operations.
