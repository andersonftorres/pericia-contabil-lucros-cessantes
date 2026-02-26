# Sistema de Cálculo de Lucros Cessantes via Planilha CSV
# Autor: Anderson Torres
# Contador Público e Perito Contábil

import csv

print("=== SISTEMA DE CÁLCULO DE LUCROS CESSANTES VIA PLANILHA ===")

arquivo = "dados.csv"

try:

    with open(arquivo, newline='', encoding='utf-8') as csvfile:

        leitor = csv.DictReader(csvfile)

        for linha in leitor:

            faturamento = float(linha["faturamento_mensal"])
            meses = int(linha["meses"])

            margens = [0.20, 0.25, 0.30, 0.35]

            print(f"\nFaturamento mensal: R$ {faturamento:,.2f}")
            print(f"Quantidade de meses: {meses}")

            print("\nRESULTADOS:")

            for margem in margens:

                lucro_mensal = faturamento * margem
                lucro_total = lucro_mensal * meses

                print(f"\nMargem de {int(margem*100)}%")
                print(f"Lucro mensal: R$ {lucro_mensal:,.2f}")
                print(f"Lucro total: R$ {lucro_total:,.2f}")

except FileNotFoundError:

    print("\nERRO: Arquivo dados.csv não encontrado.")
    print("Crie um arquivo chamado dados.csv com este conteúdo:")
    print("faturamento_mensal,meses")
    print("120000,9")
