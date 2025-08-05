#6. Caixa Eletrônico Simples
    # Simule saques de um caixa eletrônico.
    # O programa deve solicitar o valor do saque e calcular a quantidade de cédulas de 100, 50, 20 e 10 necessárias.

valor = int (input ("Digite o valor do saque:"))
for cedula in [100,50,20,10]:
    qtd = valor // cedula
    valor = valor % cedula
    if qtd > 0:
        print(f"{qtd} cédula(s) de R$ {cedula}")
        