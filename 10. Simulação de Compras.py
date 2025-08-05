#10. Simulação de Compras
    # Peça nome e preço de 3 produtos.
    # Calcule o total, aplique desconto de 10% se o valor ultrapassar R$ 100 e mostre o valor final.

total = 0
for i in range (1,4):
    nome = input (f"Produto {i}:")
    preço = float (input (f"Preço do produto {i}:"))
    total += preço

if total > 100:
    total *= 0.9 # 10% de desconto

print(f"Total final: R$ {total:.2f}")
