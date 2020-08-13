import os
import pygame
import random
import time



pygame.init()
######Load image and music######
icon = pygame.image.load('icon.png')

bg = pygame.image.load('bg.png')
earth = pygame.image.load('earth.png')

player = [pygame.image.load('Dino0.png'), pygame.image.load('Dino1.png'), pygame.image.load('Dino2.png'),
pygame.image.load('Dino3.png'), pygame.image.load('Dino4.png')] 

dino_lose = pygame.image.load('Dino2_0.png')

cactus = [pygame.image.load('Cactus0.png'),
    pygame.image.load('Cactus1.png'),
    pygame.image.load('Cactus2.png')]

music_bg = pygame.mixer.music.load('background.mp3')

cloud = [pygame.image.load('Cloud0.png'), pygame.image.load('Cloud1.png')]

ruby = pygame.image.load('Ruby.png')

menu_img = [pygame.image.load('menu_1.png')]

clock = pygame.time.Clock()
speed_cactus = 4


make_jump = False
jump_counter = 20
usr_x = 100
usr_y = 402

bg_x = 0
bg_y = 0

cactus_all = [[937, 51, 'cactus_small', cactus[0]], [1213, 90, 'cactus_big1', cactus[1]],
 [1378, 80, 'cactus_big2', cactus[2]],  [1563, 90, 'cactus_big1', cactus[1]],
 [1700, 51, 'cactus_small', cactus[0]],
 [1878, 80, 'cactus_big2', cactus[2]],
 [2100, 90, 'cactus_big1', cactus[1]]]    

cloud_all = [[900, 100, 'cloud_0', cloud[0]], [1300, 100, 'cloud_1', cloud[1]]]

ruby_all = [[1050, 50, 'ruby', ruby]]

len_cactus_all = (len(cactus_all))

player_count = 0 
run_count = 0







ruby_sound = pygame.mixer.Sound('ruby sound.ogg')

ttf_ruby = pygame.font.Font('PingPong.ttf', 36)

def jump():
  global jump_counter, make_jump, usr_y, usr_x, bg_y

  if jump_counter >= -20:
    usr_y -= jump_counter
    jump_counter -= 1
  else:
    jump_counter = 20
    make_jump = False
    bg_y = 2




display_x = 800
display_y = 600
now_game = True
speed_cloud = 2


isplay = pygame.display.set_mode((display_x, display_y))
pygame.display.set_caption('Dino: Main')
pygame.display.set_icon(icon)
menuWhile = True
window = True


while menuWhile:
  isplay.blit(menu_img[0], (0, 0))
  for event in pygame.event.get():
    if event.type==pygame.KEYDOWN:
      if event.key==pygame.K_SPACE:
        print('start game')
        menuWhile = False
        os.startfile('dino.py')
  if event.type == pygame.QUIT:
    pygame.quit()
    quit()      
  pygame.display.update()
  clock.tick(60)
pygame.mixer.music.play(0)