from django.shortcuts import render

# Create your views here.
from .utils import check_ip

def scan(request):
    if request.method == 'POST':
        start_ip = request.POST.get('start_ip')
        end_ip = request.POST.get('end_ip')
        # Split the start and end IPs by '.' to get the octets
        start_octets = start_ip.split('.')
        end_octets = end_ip.split('.')
        # Convert the octets to integers
        start_octets = [int(octet) for octet in start_octets]
        end_octets = [int(octet) for octet in end_octets]
        # Initialize the list of reachable IPs
        reachable_ips = []
        # Iterate over the range of IPs and check if they are reachable
        for i in range(start_octets[3], end_octets[3] + 1):
            ip = f"{start_octets[0]}.{start_octets[1]}.{start_octets[2]}.{i}"
            if check_ip(ip):
                reachable_ips.append(ip)
        context = {'reachable_ips': reachable_ips}
        return render(request, 'scanner/results.html', context)
    return render(request, 'scanner/form.html')
