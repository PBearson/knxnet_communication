import socket

ip = "localhost"
port = 3671

fixed_header = bytearray.fromhex("0610")
service_id = bytearray.fromhex("0209")
total_length = bytearray.fromhex("0000") # Update later
kip_header = fixed_header + service_id + total_length

kip_channel_id = bytearray.fromhex("01")
kip_reserved = bytearray.fromhex("00")

hpai_control_length = bytearray.fromhex("08")
hpai_control_protocol = bytearray.fromhex("01") # UDP
hpai_control_address = bytearray.fromhex("e000170c") # Address
hpai_control_port = bytearray.fromhex("0e57") # Port
kip_hpai_control = hpai_control_length + hpai_control_protocol + hpai_control_address + hpai_control_port

# Fix total length field
total_length_int = len(kip_header + kip_channel_id + kip_reserved + kip_hpai_control)
total_length = bytearray.fromhex("%.4x" % total_length_int)

# Fix header
kip_header = fixed_header + service_id + total_length

# Craft final payload
kip_payload = kip_header + kip_channel_id + kip_reserved + kip_hpai_control

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((ip, port))
s.send(kip_payload)
s.close()
