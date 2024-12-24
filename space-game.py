import pygame 
import random
from pygame import mixer

pygame.init() #this is always needed at the start of the program to initialize pygame

#screen and caption
screen = pygame.display.set_mode((800,600)) #this sets the size of the window by using a variable called screen REMEMBER TO PUT 2 BRACKETS 
pygame.display.set_caption("first game") #this sets the title of the window

#icon
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#bg image
background = pygame.image.load("background.png")
background = pygame.transform.scale(background,(800,600))

#player
playerImage = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerImage = pygame.transform.scale(playerImage, (64, 64))
playerX_change = 0


#multiple enemies 
enemyImage = []
enemyX =[]
enemyY =[]
enemyX_change =[]
enemyY_change = []
number_of_enemies = 6


#enemy
for i in range(number_of_enemies):
    enemyImage.append(pygame.image.load("enemy.png"))
    enemyImage[i] = (pygame.transform.scale(enemyImage[i], (64, 64)))
    enemyX.append(random.randint(0,800-64))
    enemyY.append(random.randint(50,250))
    enemyX_change.append(1.5)
    enemyY_change.append(15)



#Bullet
#ready = you cant see the bullet on the screen 
#fire = the bullet is currently moving
BulletImage = pygame.image.load("Bullet.png")
BulletX = 0
BulletY = 480
BulletImage = pygame.transform.scale(BulletImage, (32, 32))
bullet_state = "ready" 
BulletX_change = 0
BulletY_change = 2

#score
score = 0

#text on screen
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

#background music
mixer.music.load("background.wav")
mixer.music.play(-1)  #-1 makes it play on loop


#game over text:
over_font = pygame.font.Font("freesansbold.ttf", 70)


def show_score(x,y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200,250))

# def player():
#     screen.blit(playerImage, (playerX, playerY))  

#so we make changes to the def player function 
def player(x,y):
    screen.blit(playerImage, (x, y))


def enemy(x,y):
    screen.blit(enemyImage[i], (x, y))


def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(BulletImage, (x+16, y+10))  #to make sure the bullet appears at the tip and at the centre of the spaceship 


def iscollision(enemyX, enemyY, BulletX, BulletY):
    distance = ((BulletX - enemyX)**2 + (BulletY - enemyY)**2)**0.5
    if distance < 27:
        return True
    else:
        return False

  
#while loop
running = True 
while running:      #now inside this loop we define all our events for the game
    screen.fill((0,0,0))
    #bg image
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False                  #this will end the loop
    
    #if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3

            #for bullet - keydown means pressing space key 
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":   #so that we dont get another bullet until the first one is out of the screen
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    BulletX = playerX     #gets the current x coord of spaceship 
                    fire_bullet(BulletX, BulletY)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0               
    
    #for enemy 
    #now we need to make sure program understands which enemy x we are talking about
    for i in range(number_of_enemies):

        #game over text:
        if enemyY[i] >440:
            for j in range(number_of_enemies):
                enemyY[j] = 2000   #to make enemy move out of the screen completely
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] >= 800 - 64 or enemyX[i] <= 0:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]
    
        enemy(enemyX[i], enemyY[i])

        #for collision - this is also inside the for loop of number of enemies
        collision = iscollision(enemyX[i], enemyY[i], BulletX, BulletY)
        if collision:
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            BulletY = 480
            bullet_state ="ready"
            score_value += 1 
            # print(score)
            enemyX[i] = random.randint(0,800-64)
            enemyY[i] = random.randint(50,250)

    #for bullet
    if bullet_state == "fire":
        fire_bullet(BulletX, BulletY)
        BulletY -= BulletY_change

    #for multiple bullets 
    if BulletY <= 0:
        BulletY = 480
        bullet_state = "ready"


#initial code when we werent considering keydown or keyup 
    # playerX += playerX_change
    # if playerX >= 800 - 64 or playerX <= 0:
    #     playerX_change *= -1   #this reverses the direction


#code when we considered keydown and keyup
    playerX += playerX_change
    if playerX >= 800 - 64 or playerX <= 0:
        playerX_change = 0 

    player(playerX, playerY)
    # player()

    show_score(textX, textY)
    
    pygame.display.update()
