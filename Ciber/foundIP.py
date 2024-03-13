import socket

def obtener_ip_publica():
    # Utiliza un servicio externo para obtener la dirección IP pública
    direccion_ip = socket.gethostbyname(socket.gethostname())
    return direccion_ip

def obtener_ip_privada():
    # Crea un socket y obtén la dirección IP privada
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    direccion_ip = s.getsockname()[0]
    s.close()
    return direccion_ip

# Obtén y muestra la dirección IP pública
ip_publica = obtener_ip_publica()
print("Tu dirección IP pública es:", ip_publica)

# Obtén y muestra la dirección IP privada
ip_privada = obtener_ip_privada()
print("Tu dirección IP privada es:", ip_privada)
