""") Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

"""

def fibonacci(numero_verificação:int, contador:int):
    sequencia = [0,1]
    soma = 0
    numero_encontrado = False
    laco = 1
    while contador > 0:
        laco +=1

        n1 = sequencia[-2]
        n2= sequencia[-1]
        

        soma = n1+n2
        sequencia.append(soma)
        
        if soma == numero_verificação or numero_verificação in sequencia:
            numero_encontrado = True
            break



        contador -=1
        
    if numero_encontrado:
            return f'O número {numero_verificação} pertence à sequência de Fibonacci, ele aparece no laço de número {laco} \n{sequencia}'
    
    return f'O número {numero_verificação} não pertence à sequência de Fibonnaci'

print(fibonacci(21,10))

