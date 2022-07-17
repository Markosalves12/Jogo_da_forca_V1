class Forca:
    #construtor da classe Forca, a unica variável que as demais funções prescisam ver é a prórpia
    #palavra secreta
    def __init__(self, palavrasecreta):
        self.palavrasecreta = palavrasecreta
        #'Variável' que irá abrigar a palavra secreta

    def adivinha_letra(self):
        #essa função faz a  verificação da variável de entrada do usuário
        letra = input('Digite uma letra: ').lower()
        #veridicando se o usuário digitou mais de um caracter
        if len(letra) > 1:
            print("Apenas um elemento por vez por vez é válido")
            return False
        #verificando se o caracter é uma letra de fato
        try:
            letra = int(letra)
            print("Digite apenas letras")
            return False
        except:
            #caso a variável seja uma única letra a função retorna a própria letra
            #para verificação dentro do arquivo main
            return letra

    def verifica_letra(self, letra):
        #Faz a verificação da existencia ou não da letra dentro da palavra secreta
        if letra not in self.palavrasecreta:
            return False
        else:
            return True

    def game_over(self):
        print(f"FIM DE JOGO PRA VOCÊ\n"
              f"A palavra secreta era {self.palavrasecreta}")
        #declarando o fim do game por derrota


    def game_win(self, palavra):
        if list(palavra).count('*') != 0:
            return False
        else:
            print(f"Parabens você acertou a palavra secreta. [{self.palavrasecreta}]")
        # declarando o fim do game por vitória do jogador



