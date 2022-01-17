import socket

ip = "224.0.23.12"
port = 3671

# Send Search Request to Discovery Endpoint 224.0.23.12:3671
payload = bytearray.fromhex("06100201000e0801e000170c0e57")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((ip, port))
s.send(payload)
s.close()