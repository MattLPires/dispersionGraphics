# -*- coding: utf-8 -*-
"""P1_TEI_N_MatheusHenriqueDeLimaPires.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qH-KMSXIe_bbfp1dsDWrZMQf66nmuwER

1.Com o uso da linguagem de programação python versão 3.x elabore 3 programas separados. Utilize o botão texto  do  colab  para  identificar  cada  programa  em  uma  seção  de  texto  separada  dentro  de  um  mesmo notebook intitulado P1_TEI_N_seunomecompleto. Como arquivo de entrada dos seus 3 programas utilize do corpus book o text7: Wall Street Journalpara executar as seguintes tarefas

# Programa 1

a) O programa 1 deve gerar o gráfico de dispersão do text7 dos seguintes tokens: war, freedom, money, China e U.S.
"""

import nltk

nltk.download()

from nltk.book import text7

text7.dispersion_plot(["war", "freedom", "money", "China", "U.S."])

"""b) O programa 1 deve gerar em outra célula de código a lista dos 25 primeiros tokensdo text7 e também dos 25 últimos tokens."""

text7[0:25]

text7[len(text7)-25:len(text7)]

"""# Programa 2

c) O programa 2 deve gerar uma lista de distribuição de frequência e imprimir os 50 tokens mais comuns.
"""

from nltk import FreqDist

mhlp_list = FreqDist(text7)

mhlp_list.most_common(50)

"""d) O programa 2 deve gerar em outra célula um gráfico acumulativo com os 50 tokens mais comuns."""

mhlp_list.plot(50, cumulative=True)

"""e) Ainda  no  programa  2,  em  um  célula  separada,  implemente  uma  lista  com  as  palavras  que  aparecem apenas uma vez no text7."""

mhlp_list.hapaxes()

"""# Programa 3

f) O  programa  3  deverá  ser  dividido  em  3  células  para  tratar stopwords.  Na  primeira  célula  efetue  a importação do pacote de stopwords do nltk.
"""

from nltk.corpus import stopwords

"""g) Na segunda célula do programa 3 defina uma função para calcular o percentual de palavras que não são stopwords no text7."""

def mhlp_percentual (text7):
  mhlp_stopwordslist = nltk.corpus.stopwords.words('english')
  content = [w for w in text7 if w.lower() not in mhlp_stopwordslist]
  return len(content) /len(text7)

"""h) Na terceira célula do programa 3 faça a chamada da função da céluladefinida na atividade anterior(g)."""

mhlp_percentual(text7)