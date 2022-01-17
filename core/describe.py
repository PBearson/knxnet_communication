import socket

multicast_ip = "224.0.23.12"
port = 3671

control_ip = "172.26.33.226"
control_port = 0


description_request = "06100203000e"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.connect((multicast_ip, port))
control_port = hex(s.getsockname()[1])[2:]
print(control_port)
control_ip = "".join([hex(int(x))[2:] for x in control_ip.split(".")])

hpai_control_endpoint = "0801" + control_ip + control_port

payload = bytearray.fromhex(description_request + hpai_control_endpoint)

s.send(payload)

recv = s.recv(1024)
print(recv)
s.close()