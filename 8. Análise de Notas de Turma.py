#8. Análise de Notas de Turma
    # Peça ao usuário a quantidade de alunos.
    # Solicite as notas e calcule a média geral da turma, maior e menor nota.

quantidade = int (input ("Quantos alunos?"))
notas = []

for i in range (quantidade):
    nota = float (input (f"Nota do aluno {i + 1}:"))
    notas.append(nota)

media = sum (notas) / quantidade
print(f"Média: {media:.2f}")
print(f"Maior nota: {max(notas)}")
print(f"Menor nota: {min(notas)}")

