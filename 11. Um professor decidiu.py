#11. Um professor decidiu que a nota mínima para aprovação será 6.0. Porém, se o aluno tiver frequência inferior a 75%, ele será reprovado, mesmo que a nota seja maior que 6. Pede-se
        # Desenvolva um código em Python que leia a nota e a frequência (%) do aluno e exiba se ele foi aprovado ou reprovado.
        # Explique teoricamente:

#1. Por que o uso do operador lógico and é necessário nessa situação?

#Resposta: Porque o aluno só será aprovado se ambos as condições forem verdadeiras: nota>= 6 e frequência >= 75%

#2. O que aconteceria se fosse usado or no lugar de and?

#Resposta: O aluno poderia ser aprovado mesmo com nota baixa, depois que a frequência fosse alta, ou vice e versa, o que não é objetivo.

nota = float (input ("Digite a nota do aluno:"))
frequencia = float (input ("Digite a frequencia (%):"))

if nota >= 6.0 and frequencia >= 75:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")
