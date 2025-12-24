#Como testar portas simples e rapido sem esforço!

import socket

portas = 1000

HOST = input("DIgite o ip especifico: ")

for PORT in range(20, portas):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)

    resposta = s.connect_ex((HOST, PORT))

    if resposta == 0:
        SERVICE = socket.getservbyport(PORT)
        print(f"P0RT: {PORT} / SERVICE: {SERVICE}")
    
    
