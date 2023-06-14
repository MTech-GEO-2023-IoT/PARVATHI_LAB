from bluetooth import *

# Bluetooth device address of the terminal
target_address = '7c:d6:61:1d:39:c6'  # Replace with the target device's address

# UUID of the RFCOMM service
service_uuid = '00001101-0000-1000-8000-00805F9B34FB'

# Create a Bluetooth socket
sock = BluetoothSocket(RFCOMM)

# Connect to the Bluetooth terminal
sock.connect((target_address, 1))

# Send a message
message = "Hello, Bluetooth Terminal!"
sock.send(message)

# Close the Bluetooth socket
sock.close()
