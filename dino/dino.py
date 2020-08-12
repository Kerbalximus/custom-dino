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


clock = pygame.time.Clock()
speed_cactus = 4


make_jump = False
jump_counter = 20
usr_x = 100
usr_y = 402

bg_x = 0

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

ruby_count_open = open('ruby_count.txt', 'r')


ruby_count = ruby_count_open.read()
if ruby_count == '':
	ruby_count = 0
else:
	ruby_count = int(ruby_count)

ruby_count_open.close

ruby_count_open_0 = open('ruby_count.txt', 'w')

ruby_sound = pygame.mixer.Sound('ruby sound.ogg')

ttf_ruby = pygame.font.Font('PingPong.ttf', 36)

def jump():
	global jump_counter, make_jump, usr_y, usr_x

	if jump_counter >= -20:
		usr_y -= jump_counter
		jump_counter -= 1
	else:
		jump_counter = 20
		make_jump = False



pygame.mixer.music.play(0)
display_x = 800
display_y = 600
now_game = True
speed_cloud = 2


isplay = pygame.display.set_mode((display_x, display_y))
pygame.display.set_caption('Dino')
pygame.display.set_icon(icon)







while now_game:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			ruby_count_open_0.write(str(ruby_count))
			ruby_count_open_0.close
			
			pygame.quit()
			quit()
	keys = pygame.key.get_pressed()

	

	if keys[pygame.K_SPACE]:
		make_jump = True

	if make_jump == True:
		jump()


	isplay.blit(bg, (bg_x, 0))	
	isplay.blit(earth, (0, 500))
	for i in range(len_cactus_all):
		cactus_all[i][0] = cactus_all[i][0] - speed_cactus
		if cactus_all[i][0] > 90 and cactus_all[i][0] < 125:
			if usr_y > 350:
				ruby_count_open_0.write(str(ruby_count))
				ruby_count_open_0.close
				pygame.quit()
				quit()
				now_game = True


				
		if cactus_all[i][0] < -1000:
			cactus_all[i][0] = 1000
		isplay.blit(cactus_all[i][3], (cactus_all[i][0], 500 - cactus_all[i][1]))
	for a in range(len(cloud_all)):
		cloud_all[a][0] = cloud_all[a][0] - speed_cloud
		if cloud_all[a][0] < -70:

			cloud_all[a][0] = 1000
		isplay.blit(cloud_all[a][3], (cloud_all[a][0], cloud_all[a][1]))

	for i in range(len(ruby_all)):
		ruby_all[i][0] = ruby_all[i][0] - speed_cactus
		if ruby_all[i][0] > 90 and ruby_all[i][0] < 125:
			if usr_y > 350:
				ruby_count += 1
				
				ruby_sound.play()
				
				ruby_all[i][0] = -100

				
		if ruby_all[i][0] < -100:
			ruby_all[i][0] = 1000
		isplay.blit(ruby_all[i][3], (ruby_all[i][0], 500 - ruby_all[i][1]))


	if bg_x == -800:
		bg_x = 0
	else:
		bg_x -= 0.1
	ruby_text = ttf_ruby.render('Ruby: ' + str(ruby_count), 1, (180, 0, 0))
	isplay.blit(ruby_text, (0, 0))



	run_count += 1
	if run_count % 4 == 0 and make_jump == False:
		player_count = player_count + 1
		if player_count >= 5:
			player_count = 0
	isplay.blit(player[player_count], (usr_x, usr_y))

	pygame.display.update()
	clock.tick(60)