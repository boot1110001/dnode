#!/usr/bin/env python3
#cli
#by boot1110001

### IMPORTS ####################################################################
import sys
import socket

### NON EDITABLE VARIABLES #####################################################


### EDITABLE VARIABLES #########################################################
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

### FUNCTIONS ##################################################################


### MAIN #######################################################################
def main(argv):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hello, world')
        data = s.recv(1024)

    # print('Received', repr(data))
    print('Received: '+data.decode("utf-8"))

### EXEC #######################################################################
if __name__ == "__main__":
    main(sys.argv[1:])
