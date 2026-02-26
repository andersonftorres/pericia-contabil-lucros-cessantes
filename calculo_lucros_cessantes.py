# Sistema de Cálculo de Lucros Cessantes
# Autor: Anderson Torres
# Contador Público e Perito Contábil

print("=== SISTEMA DE CÁLCULO DE LUCROS CESSANTES ===")

faturamento = float(input("Digite o faturamento mensal (R$): "))
meses = int(input("Digite a quantidade de meses: "))

margens = [0.20, 0.25, 0.30, 0.35]

print("\nRESULTADOS:\n")

for margem in margens:
    lucro_mensal = faturamento * margem
    lucro_total = lucro_mensal * meses
    
    print(f"Margem: {int(margem*100)}%")
    print(f"Lucro mensal: R$ {lucro_mensal:,.2f}")
    print(f"Lucro total: R$ {lucro_total:,.2f}")
    print("---------------------------")
