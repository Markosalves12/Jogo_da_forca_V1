from random import randint
from Classes import Forca
from Tabuleiro import Board

#importando o tabuleiro criado em Tabuleiro>Board
#a cada erro uma nova posição do tabuleiro será invocada até o jogador perder ou acabar o jogo

#variável responsável por contar os erros do jogador para encerrar após as tentativas se encerrarem
erro = 0

#Função responsável por selecionar uma palavra aleatóriamente do banco de palavras criado
def palavra_secreta():
    with open("Palavrasreservadas", "rt") as file:
        bancodepalavras = file.readlines()
    #a função randint seleciona um numero de 0(primeiro indice/linha) até o tamanho do arquivo(Quantiaade de linhas)
    palavra = bancodepalavras[randint(0, len(bancodepalavras))].strip()
    return palavra

#pos = variável de controle de chamada do tabuleir
pos = 2
#O tabuleiro do jogo, dentro do arquivo Board.py
tabuleiro = Board.board

Game = Forca.Forca(palavra_secreta().lower())
#secrets = lista com o tamanho da palavra da palavra secreta (a ser advinhada)
secrets = []
erros = []
#iterador que adicionará "*"s em secrets, para dar dinamismo no jogo
for num in range(0, len(Game.palavrasecreta)):
    secrets.append('*')

#posicçoes iniciais do tabuleiro sendo exibidas da tela antes do inicio do game
print(tabuleiro[0])
print(tabuleiro[1])
print()
print(secrets)

while True:
    #letra igual variavel que será processada no arquivo main e de acordo com a classe
    letra = Game.adivinha_letra()
    #verificando se a letra ja foi adicionada aos acertos do usuario para ele não perder chances atoa
    #e ser lembrado das letras jogadas
    if letra in secrets:
        print(f"a letra {letra} já foi citada")
        #posicionamento do comando continue para pular para a próxima iteração e não prosseguir no restante
        #do código
        continue

    #verificando se a letra ja foi adicionada aos erros do usuario para ele não perder chances atoa
    #e ser lembrado das letras jogadas
    if letra in erros:
        print(f"a letra {letra} já foi citada")
        continue

    #métodos da classe estarão comentados na classe
    if Game.verifica_letra(letra) == False:
        print("não existe esssa letra na palavra secreta")
        #após o erro o tabuleiro sera impresso
        print(tabuleiro[pos])
        #faz a impressação do tabuleiro avançar para a próxima posição
        pos += 1
        #adiciona mais um erro
        erro += 1
        erros.append(letra)
        #caso o usuario erre 6 vezes o jogo encerra
        if erro == 6:
            Game.game_over()
            break
    else:
        print(f"existe a letra {letra} na palavra secreta")
        #cont = variavel que representa os indices de cada letra na palavra secreta e altera na variável secrets
        cont = 0
        #iterações que substituem os "*" dentro de secrets por letras da palavra secreta
        for Variavel in Game.palavrasecreta:
            if Variavel == letra:
                secrets[cont] = letra
            #atualização do indice verificado pela variável cont
            cont += 1

        # métodos da classe estarão comentados na classe
        if Game.game_win(secrets) == None:
            break

    #com as continuas alterações de "secrets" a variável é exibida de maneira a se parecer com a palavra secreta
    #combinando "*" e letras acertadas
    print(secrets)








