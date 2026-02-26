# Gera um relatório em PDF (mini-laudo) a partir do arquivo dados.csv
# Autor: Anderson Torres

import csv
from datetime import date

# Você vai instalar: pip3 install reportlab
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

MARGENS = [0.20, 0.25, 0.30, 0.35]


def moeda(valor: float) -> str:
    s = f"{valor:,.2f}"
    return "R$ " + s.replace(",", "X").replace(".", ",").replace("X", ".")


def ler_dados_csv(arquivo: str):
    with open(arquivo, newline="", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        linha = next(leitor, None)
        if not linha:
            raise ValueError("CSV vazio.")
        faturamento = float(str(linha["faturamento_mensal"]).replace(".", "").replace(",", "."))
        meses = int(linha["meses"])
        return faturamento, meses


def calcular(faturamento: float, meses: int):
    resultados = []
    for margem in MARGENS:
        lucro_mensal = faturamento * margem
        lucro_total = lucro_mensal * meses
        resultados.append((int(margem * 100), lucro_mensal, lucro_total))
    return resultados


def gerar_pdf(saida: str, faturamento: float, meses: int, resultados):
    c = canvas.Canvas(saida, pagesize=A4)
    largura, altura = A4

    y = altura - 60

    c.setFont("Helvetica-Bold", 16)
    c.drawString(60, y, "Relatório de Cálculo – Lucros Cessantes (Automatizado)")
    y -= 22

    c.setFont("Helvetica", 10)
    c.drawString(60, y, f"Data: {date.today().strftime('%d/%m/%Y')}")
    y -= 14
    c.drawString(60, y, "Autor: Anderson Torres – Contador Público e Perito Contábil")
    y -= 22

    c.setFont("Helvetica-Bold", 12)
    c.drawString(60, y, "Parâmetros de entrada")
    y -= 16

    c.setFont("Helvetica", 11)
    c.drawString(60, y, f"Faturamento mensal informado: {moeda(faturamento)}")
    y -= 14
    c.drawString(60, y, f"Período (meses): {meses}")
    y -= 22

    c.setFont("Helvetica-Bold", 12)
    c.drawString(60, y, "Cenários por margem de lucro")
    y -= 18

    # Cabeçalho tabela
    c.setFont("Helvetica-Bold", 11)
    c.drawString(60, y, "Margem")
    c.drawString(150, y, "Lucro mensal")
    c.drawString(320, y, "Lucro total (período)")
    y -= 12
    c.line(60, y, largura - 60, y)
    y -= 16

    c.setFont("Helvetica", 11)
    for margem_pct, lucro_mensal, lucro_total in resultados:
        c.drawString(60, y, f"{margem_pct}%")
        c.drawString(150, y, moeda(lucro_mensal))
        c.drawString(320, y, moeda(lucro_total))
        y -= 16
        if y < 80:
            c.showPage()
            y = altura - 60
            c.setFont("Helvetica", 11)

    y -= 10
    c.setFont("Helvetica-Oblique", 9)
    c.drawString(
        60,
        y,
        "Observação: Este relatório é gerado automaticamente a partir dos dados fornecidos no arquivo CSV.",
    )

    c.save()


def main():
    arquivo = "dados.csv"
    saida = "relatorio_lucros_cessantes.pdf"

    faturamento, meses = ler_dados_csv(arquivo)
    resultados = calcular(faturamento, meses)
    gerar_pdf(saida, faturamento, meses, resultados)

    print("PDF gerado com sucesso:", saida)


if __name__ == "__main__":
    main()
