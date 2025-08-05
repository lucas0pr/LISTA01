#7. Gerador de Tabuada Personalizada
    # Solicite um número e um intervalo (por exemplo, até 15).
    # Exiba a tabuada do número até o limite informado.

numero = int (input ("Digite o número para a tabuda:"))
limite = int (input ("Digite até qual o número multiplicar:"))

for i in range (1, limite + 1):
    print(f"{numero} x {i} = {numero * i}")
    