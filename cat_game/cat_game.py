import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()

fps=30
fps_clock=pygame.time.Clock()

DISPLAYSURF=pygame.display.set_mode((800,500))
pygame.display.set_caption('This is fun game ha ha.')
score=1

#colors
white=(255,255,255)
black=(0,0,0)
teal=(0,150,80)

#load images
dog_img=pygame.image.load('doggo.png')
dog_rect=dog_img.get_rect()
cat_img=pygame.image.load('cat.png')
food_img=pygame.image.load('food.png')
food_img=pygame.transform.scale(food_img, (50,30))
#load sounds
meow1=pygame.mixer.Sound('meow1.wav')
meow2=pygame.mixer.Sound('meow2.wav')
yip=pygame.mixer.Sound('yip.wav')

def meow():
    rand_meow=randint(1,2)
    if rand_meow==1:
        meow1.play()
    if rand_meow==2:
        meow2.play()

#coordinates of cat, the later, dog
catx=randint(0,700)
caty=randint(0,400)

#cat hitbox
cat_rect = cat_img.get_rect()
cat_rect.topleft=((catx,caty))
def dog():
    global dogx
    global dogy
    dogx=randint(0,700)
    dogy=randint(0,400)
    while True:
        if cat_rect.colliderect(dog_rect):
            dogx = randint(0,700)
            dogy=randint(0,400)
        else:
            break
dog()
foodx=randint(0,700)
foody=randint(0,400)

direction='right'

pressed_left=False
pressed_right=False
pressed_down=False
pressed_up=False

#Lose message
fontObj = pygame.font.Font('freesansbold.ttf', 32)
you_lose_text=fontObj.render('You Lose! :( Your score was {}'.format(score),True,black,teal)
lose_rect=you_lose_text.get_rect()
lose_rect.center=(400,200)
lose=0
#score message
score_text=fontObj.render(str(score),True,black,white)
score_rect=score_text.get_rect()
score_rect.topleft=(0,0)
bg=pygame.image.load("background.png")

running=True
while running:
    if lose==0:
        DISPLAYSURF.fill(white)
        # pygame.draw.rect(DISPLAYSURF, teal, cat_rect, 1)
        # food bowl hitbox
        cat_rect = cat_img.get_rect()
        cat_rect.topleft = ((catx, caty))
        dog_rect.topleft = ((dogx, dogy))
        food_rect = food_img.get_rect()
        food_rect.topleft = ((foodx, foody))
        # pygame.draw.rect(DISPLAYSURF, teal, food_rect,1)

        # collision detection
        # dog chase
        if dogx <= catx:
            dogx += 3
        if dogx >= catx:
            dogx -= 3
        if dogy <= caty:
            dogy += 3
        if dogy >= caty:
            dogy -= 3
        if cat_rect.colliderect(dog_rect):
            yip.play()
            DISPLAYSURF.blit(you_lose_text, lose_rect)
            lose = 1
        cat_rect.colliderect(food_rect)
        DISPLAYSURF.blit(bg,(0, 0))
        DISPLAYSURF.blit(cat_img, (catx, caty))
        DISPLAYSURF.blit(food_img, (foodx, foody))
        DISPLAYSURF.blit(dog_img, (dogx, dogy))
        DISPLAYSURF.blit(dog_img, (dogx, dogy))
        score_text = fontObj.render(str(score), True, black, white)
        DISPLAYSURF.blit(score_text,score_rect)
        if lose==1:
            you_lose_text = fontObj.render('You Lose! :( Your score was {}'.format(score), True, black, teal)
            DISPLAYSURF.blit(you_lose_text, lose_rect)
    else: #player has lost game
        pass
    for event in pygame.event.get():
        if lose==0:
            g_rect = dog_img.get_rect()
            speed=8
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    catx -= speed
                    pressed_left=True
                if event.key == pygame.K_RIGHT:
                    catx += speed
                    pressed_right=True
                if event.key==pygame.K_UP:
                    caty-=speed
                    pressed_up=True
                if event.key==pygame.K_DOWN:
                    caty+=speed
                    pressed_down=True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    pressed_left = False
                if event.key == pygame.K_RIGHT:
                    pressed_right = False
                if event.key == pygame.K_UP:
                    pressed_up = False
                if event.key == pygame.K_DOWN:
                    pressed_down = False
    if pressed_left:
        catx-=speed
    if pressed_right:
        catx +=speed
    if pressed_up:
        caty-=speed
    if pressed_down:
        caty+=speed

    if cat_rect.colliderect(food_rect)==True:
        foodx = randint(0, 700)
        foody = randint(0, 400)
        score+=1
        meow()
    if event.type==pygame.QUIT:
        running=False
    else: #player has lost game
        pass
    pygame.display.update()
    fps_clock.tick(fps)