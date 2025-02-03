#jogo da forca
import random
# mensagem de saudações
print("Bem vinda ao jogo da forca!!!")
# lista de palavras
listap = ['gato', 'banana', 'carro', 'formula']
# escolher aleatoriamente uma das palavras
secret_palavra = random.choice(listap)
print("Possui 5 chances")
lista_vazia = []

for letras in secret_palavra:
    lista_vazia += "_"
# pedir para o user excolher uma letra     # colocar em minusculos
num = 0
game_over = False
while not game_over:
    palpite = input("Informe uma letra: ").lower()
# função para verificar se a letra esta na palavra
    for posicao in range(len(secret_palavra)):
        letra = secret_palavra[posicao]
        if letra == palpite:
            lista_vazia[posicao] = letra
    if palpite not in lista_vazia:
        num +=1
        palpites_restantes = 5 - num
        print(f'Possui apenas {palpites_restantes} restantes')
        if num >= 5:
            print("Você perdeu")
            game_over = True
    print(lista_vazia)
    
    if "_" not in lista_vazia:
        print("Você venceu!!")
        game_over = True

    


    