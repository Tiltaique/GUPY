"""3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA?
"""

k =1
i = 12
soma = 0
while k < i:
    k = k+1
    soma += k
print(soma)
# resultado 77