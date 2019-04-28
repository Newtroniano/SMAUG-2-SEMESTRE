import pygame





pygame.init ()

JanelaTestes = pygame.display.set_mode ( (640 , 448) )

pygame.display.set_caption ( "Claaaaase" )

AndarDireita = [pygame.image.load ( 'images\Personagem_Sprites\Personagem__Andando_1.png' ) , pygame.image.load ( 'images\Personagem_Sprites\Personagem__Andando_2.png' ) , pygame.image.load ( 'images\Personagem_Sprites\Personagem__Andando_3.png' ) ,
             pygame.image.load ( 'images\Personagem_Sprites\Personagem__Andando_4.png' ) , pygame.image.load ( 'images\Personagem_Sprites\Personagem__Andando_5.png' ) , pygame.image.load ( 'images\Personagem_Sprites\Personagem__Andando_6.png' ) ,
            ]
AndarEsquerda = [pygame.image.load ( 'images\Personagem_Sprites\Personagem__Andando_1.png' ) , pygame.image.load ( 'images\Personagem_Sprites\Personagem__Andando_2.png' ) , pygame.image.load ( 'images\Personagem_Sprites\Personagem__Andando_3.png' ) ,
            pygame.image.load ( 'images\Personagem_Sprites\Personagem__Andando_4.png' ) , pygame.image.load ( 'images\Personagem_Sprites\Personagem__Andando_5.png' ) , pygame.image.load ( 'images\Personagem_Sprites\Personagem__Andando_6.png' ) ,
            ]


Soco = [pygame.image.load ( 'images\Personagem_Sprites\Personagem__Soco_0.png' ) , pygame.image.load ( 'images\Personagem_Sprites\Personagem__Soco_1.png' ) , pygame.image.load ( 'images\Personagem_Sprites\Personagem__Soco_3.png' ) ,
            pygame.image.load ( 'images\Personagem_Sprites\Personagem__Soco_4.png' )
            ]


bg = pygame.image.load ( 'images/Background_Fase.png' )
char = pygame.image.load ( 'images\Personagem_Sprites\Personagem__Parado_0.png' )

clock = pygame.time.Clock ()


class player ( object ):
    def __init__(self , x , y , largura , altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.vel = 5
        self.esquerda = False
        self.direita = False
        self.baixo = False
        self.cima = False
        self.soco=False
        self.ContarPassos = 0
        self.hitbox = (self.x + 17 , self.y + 11 , 29 , 52)


    def draw(self , JanelaTestes):
        if self.ContarPassos + 1 >= 27:
            self.ContarPassos = 0

        if self.esquerda:
            JanelaTestes.blit ( AndarEsquerda[self.ContarPassos // 5] , (self.x , self.y) )
            self.ContarPassos += 1
        elif self.direita:
            JanelaTestes.blit ( AndarDireita[self.ContarPassos // 5] , (self.x , self.y) )
            self.ContarPassos += 1
        elif self.cima:
            JanelaTestes.blit ( AndarDireita[self.ContarPassos // 5] , (self.x , self.y) )
            self.ContarPassos += 1
        elif self.baixo:
            JanelaTestes.blit ( AndarDireita[self.ContarPassos // 5] , (self.x , self.y) )
            self.ContarPassos += 1

        elif self.soco:
            JanelaTestes.blit ( Soco[self.ContarPassos // 50] , (self.x , self.y) )
            self.ContarPassos += 1

        else:
            if self.direita:
                JanelaTestes.blit ( AndarDireita[0] , (self.x , self.y) )
            else:
                JanelaTestes.blit ( AndarDireita[0] , (self.x , self.y) )
        self.hitbox = (self.x + 17 , self.y + 11 , 70 , 90)
        pygame.draw.rect ( JanelaTestes , (255 , 0 , 0) , self.hitbox , 2 )


def redrawGameWindow():
    JanelaTestes.blit ( bg , (0 , 0) )
    Classe.draw ( JanelaTestes )
    for soco in socobala:
        socobala.draw ( JanelaTestes )


    pygame.display.update ()


# mainloop
Classe = player ( 200 , 410 , 64 , 64 )
run = True
loop = 0
socobala = []
while run:
    clock.tick ( 27 )

    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed ()

    if keys[pygame.K_LEFT] and Classe.x > Classe.vel:
        Classe.x -= Classe.vel
        Classe.esquerda = True
        Classe.direita = False

    elif keys[pygame.K_RIGHT] and Classe.x :
        Classe.x += Classe.vel
        Classe.direita = True
        Classe.esquerda = False

    elif keys[pygame.K_UP] and Classe.x:
        Classe.y -= Classe.vel
        Classe.baixo = False
        Classe.cima = True

    elif keys[pygame.K_DOWN] and Classe.x :
        Classe.y += Classe.vel
        Classe.baixo = True
        Classe.cima = False

    elif keys[pygame.K_a] and Classe.x:
        Classe.soco+= Classe.vel
        Classe.soco = True





    else:
        Classe.direita = False
        Classe.esquerda = False
        Classe.baixo = False
        Classe.cima = False
        Classe.soco = False

        Classe.ContarPassos = 0



    redrawGameWindow ()

pygame.quit ()