import socket

ip = "localhost"
port = 3671

fixed_header = bytearray.fromhex("0610")
service_id = bytearray.fromhex("0205")
total_length = bytearray.fromhex("0000") # Update later
kip_header = fixed_header + service_id + total_length

hpai_control_length = bytearray.fromhex("08")
hpai_control_protocol = bytearray.fromhex("01") # UDP
hpai_control_address = bytearray.fromhex("e000170c") # Address
hpai_control_port = bytearray.fromhex("0e57") # Port
kip_hpai_control = hpai_control_length + hpai_control_protocol + hpai_control_address + hpai_control_port

hpai_data_length = bytearray.fromhex("08")
hpai_data_protocol = bytearray.fromhex("01") # UDP
hpai_data_address = bytearray.fromhex("e000170c") # Address
hpai_data_port = bytearray.fromhex("0e57") # Port
kip_hpai_data = hpai_data_length + hpai_data_protocol + hpai_data_address + hpai_data_port

cri_length = bytearray.fromhex("02")
cri_code = bytearray.fromhex("03") # DEVICE_MGMT_CONNECTION
kip_cri = cri_length + cri_code

# Fix total length field
total_length_int = len(kip_header + kip_hpai_control + kip_hpai_data + kip_cri)
total_length = bytearray.fromhex("%.4x" % total_length_int)

# Fix header
kip_header = fixed_header + service_id + total_length

# Craft final payload
kip_payload = kip_header + kip_hpai_control + kip_hpai_data + kip_cri

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((ip, port))
s.send(kip_payload)
s.close()
