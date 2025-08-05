#5. Classificação de Idade
    # Peça a idade do usuário.
    # Classifique como “Criança” (0-12), “Adolescente” (13-17), “Adulto” (18-59) ou “Idoso” (60+).

idade = int (input ("Digite sua idade:"))

if idade <= 12:
    grupo = "Criança"
elif idade <=17:
    grupo = "Adolescente"
elif idade <= 59:
    grupo = "Adulto"
else:
    grupo = "Idoso"

print (f"Você é classificado como: {grupo}")
