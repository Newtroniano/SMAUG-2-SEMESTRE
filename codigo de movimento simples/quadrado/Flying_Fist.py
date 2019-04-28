import math, random , sys, time
import pygame
from pygame.locals import *
from operator import itemgetter
import pickle


import Personagem_Animacao
import Tela_Inicial

#Essa função define parametros da janela do windows que será aberta
def events():
    for event in pygame.event.get ():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit ()
            sys.exit ()



# Variaveis para classe
Andando = Personagem_Animacao.Andando
AndandoEsquerda = Personagem_Animacao.Andando
Batendo = Personagem_Animacao.Batendo
Parado = Personagem_Animacao.Parado

#class player
class player ( object ):
    def __init__(self , x , y , altura , largura):

        self.x = x
        self.y = y
        self.esquerda = False
        self.direita = False
        self.parado = True
        self.altura = altura
        self.largura = largura
        self.contatordepassos = 0
        self.vel = 5
        self.hitbox = (self.x + 17 , self.y + 11 , 29 , 52)

    def draw(self , Janela):
        if self.contatordepassos + 1 >= 27:
            self.contatordepassos = 0

        if not (self.parado):
            if self.esquerda:
                Janela.blit ( AndandoEsquerda[self.contatordepassos // 3] , (self.x , self.y) )
                self.contatordepassos += 1
            elif self.direita:
                Janela.blit ( Andando[self.contatordepassos // 3] , (self.x , self.y) )
                self.contatordepassos += 1
        else:
            if self.direita:
                Janela.blit ( AndandoEsquerda[0] , (self.x , self.y) )
            else:
                Janela.blit ( Andando[0] , (self.x , self.y) )
        self.hitbox = (self.x + 17 , self.y + 11 , 29 , 52)


# Propriedades da Janela a ser aberta
Largura , Altura = 640 , 448
HW , HH = Largura / 2 , Altura  / 2
Area = Largura * Altura
Nome_da_Janela = "FLYING FIST"

#Esse código inicializa a Janela com as propriedades definidas nas variaveis
pygame.init ()
CLOCK = pygame.time.Clock ()
Janela = pygame.display.set_mode ( (Largura , Altura) )
pygame.display.set_caption ( Nome_da_Janela )


#mainClock = FPS
mainClock = pygame.time.Clock()

#Esta variável controlará as telas do jogo
Controlador_Jogo = 1

#Essa variável define a pontuação do jogador, e o Timer da fase
Score = 0
Timer = 60
Nome_do_player = ("AKI")

#Scoreboard_Player = {'Nome':Nome_do_player, 'Pontos': Score}



Leaderboard = [
{'Nome':("AAA"), 'Pontos': 3000},
{'Nome':("AAA"), 'Pontos': 4000},
{'Nome':("AAA"), 'Pontos': 5000},
{'Nome':("AAA"), 'Pontos': 2000},
{'Nome':("AAA"), 'Pontos': 300},
]

#Leaderboard.insert(0, Scoreboard_Player)
#Leaderboard.sort(key=itemgetter('Pontos'), reverse=True)

#sorted(Leaderboard, key=itemgetter('Pontos'), reverse=True)


#pickle.dump(Leaderboard, open("top_scores", "wb"))
Load_Top_Scores = pickle.load(open("top_scores", "rb"))


for key in Load_Top_Scores:
    print (key)

#Essa carrega uma fonte para o projeto do jogo, definindo seu tamanho
fonte_small = pygame.font.Font("fontes/start.ttf", 18)
fonte_med = pygame.font.Font("fontes/start.ttf", 25)
fonte_big = pygame.font.Font("fontes/start.ttf", 35)


#Carrega as imagem do jogo em geral
Background_Fase = pygame.image.load ( "images/Background_Fase.png" ).convert ()
Background_Tela_Inicial = pygame.image.load ("images/Tela_Inicial/Tela_de_Titulo.png").convert ()
Personagem_HUD = pygame.image.load ("images/Personagem_Vida.png").convert_alpha()

#Define a Altura e Largura do background
Background_Largura , Background_Altura = Background_Fase.get_rect ().size

# Define o tamanho da fase
Fase_Largura = Background_Largura * 3
#Define a posicao do background da fase em relação a janela
Background_Fase_Posicao = 0
startScrollingPosX = HW

#Variaveis relacionadas ao Personagem
circleRadius = 25
circlePosX = circleRadius
playerPosX = circleRadius+50
playerPosY = 300
playerVelocityX = 0
playerVelocityY = 0
HP = 155


#Musica é tocada assim que executa o jogo, mas não em loop
#Musica_Fase = pygame.mixer.music.load('Musica_SFX\Musica_Fase.wav')
pygame.mixer.music.load('Musica_SFX\intro.mp3')
pygame.mixer.music.play(1)

SFX_Punch1 = pygame.mixer.Sound('Musica_SFX\SFX\Punch_1.wav')
SFX_Punch2 = pygame.mixer.Sound('Musica_SFX\SFX\Punch_2.wav')
SFX_Miss = pygame.mixer.Sound('Musica_SFX\SFX\Punch_miss.wav')
SFX_Death = pygame.mixer.Sound('Musica_SFX\SFX\Death.wav')

# main loop

#chama todos os parametros da classe Player
man = player(200, 410, 64,64)
run = True

man.vel=playerVelocityX
man.vel=playerVelocityY


while run:
    CLOCK.tick(0)

    events ()
    #A variável Botao_Pressionado coleta a tecla que você está apertando
    Botao_Pressionado = pygame.key.get_pressed()


    # Controlador_Jogo é igual a 0, você está na fase
    if Controlador_Jogo == 0:


        #Essa parte do código detecta o botão pressionado e adiciona valores as variaveis de velocidade do jogador e alteram a visibilidade das animações do personagem
        if Botao_Pressionado[K_RIGHT]:
            playerVelocityX = 0.2
            man.x += man.vel
            man.esquerda = True
            man.direita = False
            man.parado = False
            man.direita = True


        elif Botao_Pressionado[K_LEFT]:
            playerVelocityX = -0.2
            man.x -= man.vel
            man.esquerda = True
            man.direita = False
            man.parado = False
            man.parado=Andando
        else:

            playerVelocityX = 0
        if Botao_Pressionado[K_UP] and playerPosY > 250:
            playerVelocityY = -0.2
        elif Botao_Pressionado[K_DOWN] and playerPosY< 380:
            playerVelocityY = 0.2
        else:
            playerVelocityY = 0
            man.direita = False
            man.esquerda = False
            man.contatordepassos = 0
            man.parado = True

        #Essa parte do codigo deixa a animação correspondente visivel se tiver as condições certas
        if playerVelocityY == 0 and playerVelocityX == 0 :
            Personagem_Animacao.Parado.visibility= True
            Personagem_Animacao.Andando.visibility = False
            Personagem_Animacao.Batendo.visibility = False
        elif playerVelocityX != 0 or playerVelocityY != 0:
            Personagem_Animacao.Parado.visibility = False
            Personagem_Animacao.Andando.visibility = True
            Personagem_Animacao.Batendo.visibility = False
        if Botao_Pressionado[K_a]:
            SFX_Miss.play(0)
            Personagem_Animacao.Batendo.visibility = True
            Personagem_Animacao.Andando.visibility = False
            Personagem_Animacao.Parado.visibility = False

        #Teste de Leaderboards com valores atualizados

        if Botao_Pressionado[K_l]:
            Scoreboard_Player = {'Nome': Nome_do_player, 'Pontos': Score}
            Load_Top_Scores.insert(0, Scoreboard_Player)
            pickle.dump(Load_Top_Scores, open("top_scores", "wb"))
            Load_Top_Scores = pickle.load(open("top_scores", "rb"))
            Load_Top_Scores.sort(key=itemgetter('Pontos'), reverse=True)

            for key in Load_Top_Scores:
                print(key)




        #Essa parte do código da Play em TODAS as animações do personagem
        Personagem_Animacao.Parado.play()
        Personagem_Animacao.Andando.play()
        Personagem_Animacao.Batendo.play()

        #Essa parte do código incrementa a posição do jogador com a variavel de velocidade, relativa a X e Y
        playerPosX += playerVelocityX
        playerPosY += playerVelocityY

        #Essa parte do código é referente ao SideScrolling e posição do personagem na tela. Para entender, ver https://www.youtube.com/watch?v=AX8YU2hLBUg&t=478s
        if playerPosX > Fase_Largura:
            playerPosX = Fase_Largura
        if playerPosX < circleRadius:
            playerPosX = circleRadius
        if playerPosX < startScrollingPosX:
            playerPosX = playerPosX
        elif playerPosX > Fase_Largura - startScrollingPosX:
            playerPosX = playerPosX - Fase_Largura + Largura
        else:
            playerPosX = startScrollingPosX
            Background_Fase_Posicao += -playerVelocityX

        rel_x = Background_Fase_Posicao % Background_Largura

        Janela.blit ( Background_Fase , (rel_x - Background_Largura, 0) )

        if rel_x < Largura:
            Janela.blit ( Background_Fase , (rel_x , 0) )

        #Esta parte do código imprime na tela todas as imagens do jogo.
        Hitbox = (playerPosX, playerPosY, 100, 100)
        #hitbox
        Texto_Placar = fonte_small.render(str(Score), 1, (0, 0, 0))
        Janela.blit(Texto_Placar, (190, 30))


        seconds = int((pygame.time.get_ticks() - start_ticks)/1000)
        Texto_Timer = fonte_med.render(str(Timer-seconds), 1, (0, 0, 0))
        Janela.blit(Texto_Timer, ((Largura/2)-17, 10))



        pygame.draw.rect(Janela, (255,0,0), Hitbox,2 )

        #Teste para ver a barra de vida diminuindo
        if Botao_Pressionado[K_b] and HP >=0.9 :
            HP -= 0.2
            Score += 1

        Janela.blit(Personagem_HUD, (10, 10))
        pygame.draw.rect(Janela, (255, 255, 0), (78, 57, HP, 19), 0)
        Personagem_Animacao.Andando.blit(Janela, (playerPosX, playerPosY))
        Personagem_Animacao.Parado.blit(Janela, (playerPosX, playerPosY))
        Personagem_Animacao.Batendo.blit(Janela, (playerPosX, playerPosY))

    # Controlador_Jogo é igual a 1, você está na tela de título
    if Controlador_Jogo == 1:
        Janela.blit ( Background_Tela_Inicial , (0,-10))
        Tela_Inicial.Press_Start.blit(Janela,(110,320))
        Tela_Inicial.Tela_de_titulo_animacao.blit(Janela, (0,-10))
        Tela_Inicial.Press_Start.play()
        if Botao_Pressionado[K_RETURN]:
            Tela_Inicial.Tela_de_titulo_animacao.play()
        if Tela_Inicial.Tela_de_titulo_animacao.currentFrameNum == 9:
            Controlador_Jogo=0
            start_ticks = pygame.time.get_ticks()
            pygame.mixer.music.stop()
            pygame.mixer.music.load('Musica_SFX\Musica_Fase.wav')
            pygame.mixer.music.play(-1)




    pygame.display.update ()
    mainClock.tick(1000)