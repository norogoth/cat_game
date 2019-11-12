import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()

fps=30
fps_clock=pygame.time.Clock()

DISPLAYSURF=pygame.display.set_mode((800,500))
pygame.display.set_caption('This is fun game ha ha.')

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
meow1=pygame.mixer.Sound('meow1.wav')
meow2=pygame.mixer.Sound('meow2.wav')

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
you_lose_text=fontObj.render('You Loose! :(',True,black,teal)
lose_rect=you_lose_text.get_rect()
lose_rect.center=(400,200)

while True:
    DISPLAYSURF.fill(white)

    #pygame.draw.rect(DISPLAYSURF, teal, cat_rect, 1)
#food bowl hitbox
    cat_rect = cat_img.get_rect()
    cat_rect.topleft = ((catx, caty))
    food_rect=food_img.get_rect()
    food_rect.topleft=((foodx,foody))
    #pygame.draw.rect(DISPLAYSURF, teal, food_rect,1)

#collision detection
    #dog chase
    if dogx<=catx:
        dogx+=2
    if dogx>=catx:
        dogx-=2
    if dogy<=caty:
        dogy+=2
    if dogy >= caty:
        dogy-=2
    if cat_rect.colliderect(dog_rect):
        DISPLAYSURF.blit(you_lose_text,lose_rect)
    cat_rect.colliderect(food_rect)
    DISPLAYSURF.blit(cat_img,(catx,caty))
    DISPLAYSURF.blit(food_img,(foodx,foody))
    DISPLAYSURF.blit(dog_img,(dogx,dogy))
    DISPLAYSURF.blit(dog_img,(dogx,dogy))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                catx += 5
                pressed_left=True
            if event.key == pygame.K_RIGHT:
                catx -= 5
                pressed_right=True
            if event.key==pygame.K_UP:
                caty-=5
                pressed_up=True
            if event.key==pygame.K_DOWN:
                caty+=5
                pressed_down=True
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                pressed_left=False
            if event.key==pygame.K_RIGHT:
                pressed_right=False
            if event.key==pygame.K_UP:
                pressed_up=False
            if event.key==pygame.K_DOWN:
                pressed_down=False
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    if pressed_left:
        catx-=5
    if pressed_right:
        catx +=5
    if pressed_up:
        caty-=5
    if pressed_down:
        caty+=5
    if cat_rect.colliderect(food_rect)==True:
        foodx = randint(0, 700)
        foody = randint(0, 400)
        meow()
    pygame.display.update()
    fps_clock.tick(fps)