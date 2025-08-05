#1. Cálculo de Média e Aprovação
    # Peça o nome e duas notas de um aluno.
    # Calcule a média e informe se foi aprovado (nota ≥ 6).

nome = input ("Digite o nome do aluno:")
nota1 = float (input ("Digite a primeira nota:"))
nota2 = float (input ("Digite a segunda nota:"))

media = (nota1 + nota2) / 2

if media >= 6:
    print (f"{nome} foi aprovado com média {media:.2f}")
else:
    print (f"{nome} foi reprovado com média {media:.2f}")
