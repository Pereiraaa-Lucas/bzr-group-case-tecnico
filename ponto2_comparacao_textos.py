def contem_mesmos_caracteres(caminho_1, caminho_2):
    with open(caminho_1, 'r', encoding='utf-8') as f1:
        texto_1 = f1.read()
        
    with open(caminho_2, 'r', encoding='utf-8') as f2:
        texto_2 = f2.read()
        
    return set(texto_1) == set(texto_2)

if __name__ == "__main__":
    sao_iguais = contem_mesmos_caracteres('test2_text1.txt', 'test2_text2.txt')
    print(f"Os arquivos contêm os mesmos caracteres? {sao_iguais}")
