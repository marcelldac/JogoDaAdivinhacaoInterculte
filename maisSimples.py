import random

print('#### Iniciando IntercultGame ####')

""" A função gera() puxa o randint da biblioteca random a faz com que puxe numeros aleatórios de 1 a 100 """
def gera(): 
    return random.randint(1,100)


""" A função game() é o jogo em si """
def game():

    """ Ini Declaração de variáveis do jogo """
    resposta = gera()
    tentativa = 0
    chute=0
    """ Fim Declaração de variáveis do jogo """

    """ Ini Enquanto não for a resposta: """
    while chute is not resposta:
        tentativa +=1
        chute = int(input("Qual seu chute: "))
        if chute > resposta:
            print("Errou! É um valor menor que ", chute)
        elif chute < resposta:
            print("Errou! É um valor maior que ", chute)
            """ Fim Enquanto não for a resposta: """
            """ Acertou a resposta: """
        else:
            print("Parabéns! O número gerado foi ",resposta, \
                  "Acertou em ",tentativa," tentativas!")
    """ Puxando a função """
while True:
    game()
