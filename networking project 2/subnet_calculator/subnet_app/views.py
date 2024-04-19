# subnet_calculator/subnet_app/views.py
from django.shortcuts import render
from .utils import calculate_subnet, validate_ip_address

def subnet_calculator(request):
    error = None
    subnet_details = None
    
    if request.method == 'POST':
        ip_address = request.POST.get('ip_address')
        subnet_bits = int(request.POST.get('subnet_bits', 0))

        if not validate_ip_address(ip_address):
            error = 'Invalid IP address format'
        elif subnet_bits <= 0 or subnet_bits >= 32:
            error = 'Invalid subnet bits'

        if not error:
            subnet_details = calculate_subnet(ip_address, subnet_bits)
            if subnet_details is None:
                error = 'Invalid IP address or subnet bits'
    
    return render(request, 'subnet_app/index.html', {'error': error, 'subnet_details': subnet_details})
