#3. Calculadora Simples
    # Peça dois números e exiba a soma, subtração, multiplicação e divisão.
    # Utilize condicionais para verificar divisão por zero.

a = float (input ("Digite o primeiro número:"))
b = float (input ("Digite o segundo número:"))

print(f"Soma: {a + b}")
print(f"Subtração {a - b}")
print(f"Multiplicação {a * b}")

if b !=0:
    print(f"Divisão por zero não é permitido.")