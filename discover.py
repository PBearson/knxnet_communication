import socket

ip = "224.0.23.12"
port = 3671

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Search request extended - discovery
payload1 = bytearray.fromhex("0610020b00160801e000170c0e570884020806070100")

# Search request - discovery
payload2 = bytearray.fromhex("06100201000e0801e000170c0e57")

s.connect((ip, port))
# s.send(payload1)
s.send(payload2)

s.close()