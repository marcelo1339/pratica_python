"""Todas as palavras que estão no arquivo -palavras.txt- foram retiradas do perfil Python Pro:
https://github.com/pythonprobr/palavras"""
from random import choice

palavras = list()

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

with open('palavras.txt', 'r', encoding='utf-8') as plv:
    for letra in alfabeto:
        for c in range(0, 1000):


print(palavras)
