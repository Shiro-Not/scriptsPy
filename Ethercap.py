from scapy.all import Ether, ARP, srp

faixa = input("Digite a sua faixa de IP: ")

respondido, nao_respondido = srp (
    Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=faixa),
    timeout=1,
    verbose=0
)

print("IPs encontrados na rede!")

for IP, scaneados in respondido:
    print(scaneados[ARP].psrc, scaneados[Ether].src)
