import pygame
import fontgradient

pygame.init()

pygame.mixer.music.load("crono.mp3")

screenw = 640
screenh = 480

win = pygame.display.set_mode((screenw, screenh))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

x = 250
y = 250
width = 64
height = 64
vel = 5

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0


font = pygame.font.Font("Font/start.ttf", 30)

def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    win.blit(screen_text, [screenw/2 - screen_text.get_rect().width/2, screenh/2])

def redrawGameWindow():
    global walkCount
    win.blit(bg,(0,0))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount // 3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount // 3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
        walkCount = 0

    def draw():
        win.draw.text("Font, size, outline, color", (55, 80), color="blue", fontname="start", fontsize=50,owidth=1.5, ocolor="yellow")
        win.draw.text("Shadow, Shadow color", (75, 120), color="blue", fontname="start", fontsize=50, shadow=(1, 5),scolor="gray")
        win.draw.text("Color gradient", (85, 150), color="white", fontname="start", fontsize=80, gcolor="green")


    message_to_screen("You Loseão", (255,0,0))
    draw()
    pygame.display.update()

#mainloop

pygame.mixer.music.play(1)

run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #pygame.mixer.music.play(1)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False

    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
        left = False
        right = True

    else:
        right = False
        left = False
        walkCount = 0
    if not (isJump):
        #if keys[pygame.K_DOWN] and y < 500 - height - vel:
            #y += vel
        #if keys[pygame.K_UP] and y > vel:
            #y -= vel
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10


    redrawGameWindow()

pygame.quit()
