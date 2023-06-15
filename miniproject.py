
from bluetooth import *

# Bluetooth device address of the terminal
target_address = '7c:d6:61:1d:39:c6'  # Replace with the target device's address

# UUID of the RFCOMM service
service_uuid = '00001801-0000-1000-8000-00805f9b34fb'

# Create a Bluetooth socket
sock = BluetoothSocket(RFCOMM)

# Connect to the Bluetooth terminal
sock.connect((target_address, 1))

# Send a message
message = "Hello, Bluetooth Terminal!"
sock.send(message)

# Close the Bluetooth socket
sock.close()


##############################

import bluetooth

server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
port = 1
server_socket.bind(("",port))
server_socket.listen(1)
client_socket,address = server_socket.accept()
print("Accepted connection from ",address)

while True:
    res = self.client_socket.recv(1024)
    client_socket.send(res)
    if res == 'q':
        print ("Quit")
        break
    else:
        print("Received:",res)

client_socket.close()
server_socket.close()
