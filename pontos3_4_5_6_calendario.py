from datetime import date

def calcular_dias_entre_datas(ano):
    data_inicio = date(ano, 2, 15)
    data_fim = date(ano, 10, 15)
    diferenca = data_fim - data_inicio
    return diferenca.days

if __name__ == "__main__":
    anos = [2000, 2001, 1900, 1582]

    for ano in anos:
        dias = calcular_dias_entre_datas(ano)
        print(f"Ano {ano}: {dias} dias entre 15 de fevereiro e 15 de outubro.")
