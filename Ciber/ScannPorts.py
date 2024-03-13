import sys
import socket

objetive = socket.gethostbyname(input("Inserte una dirección IP: "))

print("Escaneando objetivo..." + objetive)

try:
    for port in range (1,150):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        resultado = s.connect_ex((objetive, port))

        if resultado == 0:
            print("El puerto {} esta abierto".format(port))
        s.close()
except:
    print("\n saliendo...")
    sys.exit(0)
