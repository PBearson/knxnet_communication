import socket

ip = "localhost"
port = 3671

fixed_header = bytearray.fromhex("0610")
service_id = bytearray.fromhex("0201")
total_length = bytearray.fromhex("0000") # Update later
kip_header = fixed_header + service_id + total_length

hpai_discovery_length = bytearray.fromhex("08")
hpai_discovery_protocol = bytearray.fromhex("01") # UDP
hpai_discovery_address = bytearray.fromhex("e000170c") # Address
hpai_discovery_port = bytearray.fromhex("0e57") # Port
kip_hpai_discovery = hpai_discovery_length + hpai_discovery_protocol + hpai_discovery_address + hpai_discovery_port


# Fix total length field
total_length_int = len(kip_header + kip_hpai_discovery)
total_length = bytearray.fromhex("%.4x" % total_length_int)

# Fix header
kip_header = fixed_header + service_id + total_length

# Craft final payload
kip_payload = kip_header + kip_hpai_discovery

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((ip, port))
s.send(kip_payload)
s.close()