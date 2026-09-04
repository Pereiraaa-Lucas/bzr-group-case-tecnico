# Processo Seletivo | Estágio em Tecnologia - BZR Group

Repositório dedicado à entrega do desafio técnico do processo seletivo para a vaga de Estágio em Tecnologia da **BZR Group**. O desafio foi integralmente resolvido utilizando a linguagem **Python**, com foco em boas práticas de programação, legibilidade, tratamento de tipos e precisão lógica.

---

## 🛠️ Estrutura da Solução e Arquivos

O projeto está dividido nos três módulos exigidos pelo desafio:

### 1. Ponto 1: Soma de Valores em JSON (`ponto1_soma_json.py`)
* **Objetivo:** Ler um arquivo estruturado em JSON (`test1.json`) contendo um array com números inteiros misturados a representações em string (`[1, "2", 3, "4"]`) e retornar a soma total[span_0](start_span)[span_0](end_span).
* **Abordagem:** O script realiza a leitura do arquivo, desserializa os dados e aplica uma conversão explícita de cada elemento para inteiro antes de efetuar a somatória acumulada, evitando erros de tipagem.

### 2. Ponto 2: Verificação de Caracteres (`ponto2_comparacao_textos.py`)
* **Objetivo:** Ler dois arquivos de texto (`test2_text1.txt` e `test2_text2.txt`) e verificar se ambos contêm exatamente os mesmos caracteres[span_1](start_span)[span_1](end_span).
* **Abordagem:** Utiliza estruturas de conjuntos (`set`) em Python para isolar os caracteres únicos de cada arquivo e realizar a validação de igualdade de forma eficiente, independente de ordem.

### 3. Pontos 3, 4, 5 e 6: Cálculo de Dias entre Datas (`pontos3_4_5_6_calendario.py`)
* **Objetivo:** Calcular a quantidade exata de dias transcorridos entre **15 de fevereiro e 15 de outubro** para quatro anos distintos: **2000, 2001, 1900 e 1582**[span_2](start_span)[span_2](end_span).
* **Abordagem:** Utiliza o módulo nativo `datetime.date` para lidar com a aritmética de datas e o comportamento correto de anos bissextos e regras centenárias.

---

## 🚀 Como Executar os Códigos

Certifique-se de ter o **Python 3** instalado em sua máquina.

1. Clone este repositório ou baixe os arquivos para a mesma pasta onde se encontram os arquivos de teste (`.json` e `.txt`).
2. Abra o terminal na pasta do projeto e execute os scripts individualmente:

```bash
# Executar o Ponto 1 (Soma do JSON)
python ponto1_soma_json.py

# Executar o Ponto 2 (Comparação de Textos)
python ponto2_comparacao_textos.py

# Executar os Pontos 3 a 6 (Cálculo de Datas)
python pontos3_4_5_6_calendario.py
# bzr-group-case-tecnico