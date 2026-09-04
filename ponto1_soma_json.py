import json

def somar_valores_json(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    
    soma_total = sum(int(item) for item in dados)
    return soma_total

if __name__ == "__main__":
    resultado = somar_valores_json('test1.json')
    print(f"A soma total é: {resultado}")
