#4. IMC – Índice de Massa Corporal
    # Solicite peso e altura do usuário.
    # Calcule o IMC e classifique como “Abaixo do peso”, “Normal”, “Sobrepeso” ou “Obeso”.

peso = float (input ("Peso (kg):"))
altura = float (input ("Altura (m):"))
imc = peso / (altura ** 2)

if imc < 18.5:
    status = "Abaixo do peso"
elif imc < 25:
    status = "Normal"
elif imc < 30:
    status = "Sobrepeso"
else:
    status = "Obeso"

print(f"IMC: {imc:.2f} - {status}")
