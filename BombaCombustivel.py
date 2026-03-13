#Bomba de combustivel
class BombaCombustivel:

    def __init__(self, gasolina, etanol, diesel, quantidadeCombustivel):
        self._quantidadeCombustivel = quantidadeCombustivel
        self._gasolina = gasolina
        self._etanol = etanol
        self._diesel = diesel

    @property
    def tipoCombustiveis(self):
        return (self._gasolina, self._etanol, self._diesel, self._quantidadeCombustivel)
    

    def abastecerPorLitro(self, litro, combustivel):
        
        if litro > self._quantidadeCombustivel:
            return "Combustível insuficiente na bomba"

        if combustivel == "GASOLINA":
            preco = self._gasolina
        
        elif combustivel == "ETANOL":
            preco = self._etanol

        
        elif combustivel == "DIESEL":
            preco = self._diesel

        else:
            return "Escolha uma das três opõçes"
        

        self._quantidadeCombustivel -= litro
        
        return litro*preco
        

    
    def abastecerPorValor(self, valor, combustivel):
        
        if combustivel == "GASOLINA" and valor >= 5.50:
            preco = self._gasolina
        
        elif combustivel == "ETANOL" and valor >= 4.00:
            preco = self._etanol
        
        elif combustivel == "DIESEL" and valor >= 6.00:
            preco = self._diesel
        
        else:
            return "saldo insuficiente ou pedido errado"
        
        litros = valor/preco

        if litros > self._quantidadeCombustivel:
            return "Combustível insuficiente na bomba"

        
        self._quantidadeCombustivel -= litros
        
        return litros
    

    def reabastecer(self, litros):

        if litros <= 0:
            return "Quantidade invalida"

        self._quantidadeCombustivel += litros

        return f"Bomba reabastecida! Agora tem {self._quantidadeCombustivel:.2f} litros"

print("1 - Litros")
print("2 - Dinheiro")
print("3 - reabastecer")

escolha = int(input("escolha uma formade abastecimento: "))
bomba = BombaCombustivel(5.50, 4.00, 6.00, 1000)

if escolha == 1:
    litro = float(input("Digite o litro: "))
    combustivel = str(input("escolha o combustivel: ")).upper()


    Total_em_dinheiro = bomba.abastecerPorLitro(litro, combustivel)

    print(f"\nO CLIENTE ESCOLHEU EM LITROS")
    print(f"TIPO DE COMBUSTIVEL: {combustivel}")
    print(f"O CLIENTE QUER: {litro} LITROS")
    print(f"TOTAL A PAGAR: R${Total_em_dinheiro:.2f}")

elif  escolha == 2:

    valor = float(input("escolha o valor: R$ "))
    combustivel = str(input("escolha o combustivel: ")).upper()

    Total_em_Litros = bomba.abastecerPorValor(valor, combustivel)

    print("\nO CLIENTE ESCOLHEU EM DINHEIRO")
    print(f"TIPO DE COMBUSTIVEL: {combustivel}")
    print(f"O CLIENTE PAGOU: R${valor}")
    print(f"TOTAL EM LITROS: {Total_em_Litros:.2f}")

elif escolha == 3:

    qtdLitros = float(input("Quanto vc quer abastecer?: "))
    print(bomba.reabastecer(qtdLitros))