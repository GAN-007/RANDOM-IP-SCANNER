import socket

def check_ip(ip):
    """check if given IP is raechable"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, 80))
        return True
    except:
        return False 
