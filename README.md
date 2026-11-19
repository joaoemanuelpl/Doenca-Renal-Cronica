# Classificação de Doença Renal Crônica com Aprendizagem de Máquina

**Projeto acadêmico — Aprendizagem de Máquina (ADS033)**  
**Curso:** Análise e Desenvolvimento de Sistemas — IESB  
**Semestre:** 2026/2

## Sobre o projeto

Este projeto tem como objetivo desenvolver um fluxo de aprendizagem de máquina aplicado à classificação de registros relacionados à doença renal crônica (DRC).

São utilizados dados clínicos e laboratoriais para analisar, preparar e desenvolver modelos capazes de classificar os registros nas categorias `ckd` e `notckd`.

O trabalho está organizado em dois marcos, abrangendo desde a obtenção e análise dos dados até o treinamento e a avaliação comparativa dos algoritmos.

## Base de dados

- **Conjunto:** Chronic Kidney Disease (CKD).
- **Fonte:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease).
- **Registros:** 400.
- **Atributos:** 24 variáveis preditoras e uma variável-alvo.
- **Licença:** CC BY 4.0.

A utilização da base com 400 registros foi autorizada pelo professor responsável pela disciplina.

## Organização do projeto

### Notebooks

**Marco 1 — Dados, análise exploratória e baseline**

[![Abrir no Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/joaoemanuelpl/Doenca-Renal-Cronica/blob/main/notebooks/Marco1_Doenca_Renal_Cronica_Colab.ipynb)

Arquivo: `notebooks/Marco1_Doenca_Renal_Cronica_Colab.ipynb`

Contempla a descrição da base, limpeza e auditoria dos dados, análise exploratória, pré-processamento e desenvolvimento do modelo de referência (*baseline*).

**Marco 2 — Modelos e avaliação comparativa**

Em desenvolvimento.

Arquivo previsto: `notebooks/Marco2_Doenca_Renal_Cronica_Colab.ipynb`

Contemplará o desenvolvimento dos modelos supervisionados e não supervisionados, validação cruzada e comparação dos resultados.

### Scripts

- `scripts/obter_base.py` — realiza o download da base de dados e verifica sua integridade por meio do algoritmo SHA-256.

### Outros arquivos

- `data/` — armazenamento local da base de dados.
- `AUTORES.md` — identificação dos integrantes e suas respectivas responsabilidades.
- `requirements.txt` — dependências necessárias para executar o projeto.
- `.gitignore` — define arquivos e diretórios que não devem ser enviados ao GitHub.

## Tecnologias utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- SciPy
- IPython
- Google Colab

## Autores

- João Emanuel Pinheiro
- Gabriel Santana
- Iago Rodrigues
- Nithielly Tamily

## Situação do projeto

Projeto acadêmico desenvolvido para a disciplina de Aprendizagem de Máquina (ADS033), no semestre 2026/2.

O desenvolvimento está organizado em dois marcos, acompanhando as etapas e os requisitos estabelecidos na proposta da disciplina.
