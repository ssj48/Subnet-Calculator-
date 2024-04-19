# subnet_calculator/subnet_app/utils.py
def calculate_subnet(ip_address, subnet_bits):
    octets = ip_address.split('.')
    
    # Convert octets to binary
    binary_ip = ''.join([bin(int(octet)+256)[3:] for octet in octets])
    
    # Calculate subnet mask
    subnet_mask = '1' * subnet_bits + '0' * (32 - subnet_bits)
    subnet_mask_octets = [str(int(subnet_mask[i:i+8], 2)) for i in range(0, 32, 8)]
    
    # Calculate network address
    network_binary = binary_ip[:subnet_bits] + '0' * (32 - subnet_bits)
    network_octets = [str(int(network_binary[i:i+8], 2)) for i in range(0, 32, 8)]
    network_address = '.'.join(network_octets)
    
    # Calculate broadcast address
    broadcast_binary = binary_ip[:subnet_bits] + '1' * (32 - subnet_bits)
    broadcast_octets = [str(int(broadcast_binary[i:i+8], 2)) for i in range(0, 32, 8)]
    broadcast_address = '.'.join(broadcast_octets)
    
    # Calculate usable hosts
    usable_hosts = 2 ** (32 - subnet_bits) - 2
    
   # Calculate first host address
    first_host_octets = network_octets[:-1] + [str(int(network_octets[-1])+1)]
    first_host_address = '.'.join(first_host_octets)
    
    # Calculate last host address
    last_host_octets = broadcast_octets[:-1] + [str(int(broadcast_octets[-1])-1)]
    last_host_address = '.'.join(last_host_octets)

    return {
        'Entered_IP_Address': ip_address,
        'Entered_Subnet_Bits': subnet_bits,
        'Class_of_the_IPV4_address': get_ip_class(octets[0]),
        'Subnet_Mask': '.'.join(subnet_mask_octets),
        'Network_Address': network_address,
        'Broadcast_Address': broadcast_address,
        'Usable_Hosts': usable_hosts,
        'First_Host_Address': first_host_address,
        'Last_Host_Address': last_host_address,
        'Octet_1': octets[0],
        'Octet_2': octets[1],
        'Octet_3': octets[2],
        'Octet_4': octets[3]
    }

def validate_ip_address(ip_address):
    octets = ip_address.split('.')
    if len(octets) != 4:
        return False
    for octet in octets:
        if not octet.isdigit() or not 0 <= int(octet) <= 255:
            return False
    return True

def get_ip_class(first_octet):
    first_octet = int(first_octet)
    if 1 <= first_octet <= 126:
        return 'A'
    elif 128 <= first_octet <= 191:
        return 'B'
    elif 192 <= first_octet <= 223:
        return 'C'
    elif 224 <= first_octet <= 239:
        return 'D'
    elif 240 <= first_octet <= 255:
        return 'E'
    else:
        return 'Invalid'