#12. Um sistema recebe dados do usuário sempre em formato de texto (string). Para cálculos, é 
#necessário converter os valores para números decimais.

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

media = (valor1 + valor2) / 2
print(f"Média: {media:.2f}")

#Por que usar float()?
#Porque input() retorna texto (string), e precisamos de números reais para fazer operações matemáticas.

#E se somássemos strings?
#Seria uma concatenação. Exemplo: "3" + "4" resulta em "34", e não na soma 7.

