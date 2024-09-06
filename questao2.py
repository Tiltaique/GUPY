""" Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

"""

import unicodedata


def encontrar(palavra:str):
    # tira os espaços e deixa a str em minusculo
    palavra_format = palavra.lower().replace(" ", "")
    
    # funcao que tira os acentos da palavra formatada
    def normalizar_texto(texto):
        texto_normalizado = unicodedata.normalize('NFD', texto)
    
        texto_sem_acento = ''.join(caracter for caracter in texto_normalizado if not unicodedata.combining(caracter))
        return texto_sem_acento
    
    # ond eu chamo a funcao anterior e armazeno na variavel
    format_final = normalizar_texto(palavra_format)
    
    if 'a' in format_final:
       n_vezes = format_final.count('a')
       return f'A letra "a" existe na string "{palavra}" e aparece {n_vezes} vez(es)'
    return f'A letra "a" não existe na string {palavra}'

print(encontrar('O rápido desenvolvimento da tecnologia traz novas oportunidades e desafios todos os dias.'))

