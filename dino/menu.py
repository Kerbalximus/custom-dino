import pygame


pygame.init();
screen = pygame.display.set_mode((800,600));
pygame.display.set_caption("menu");
menuAtivo = True;

start_button = pygame.draw.rect(screen,(0,0,240),(150,90,100,50));
continue_button = pygame.draw.rect(screen,(0,244,0),(150,160,100,50));
quit_button = pygame.draw.rect(screen,(244,0,0),(150,230,100,50));


pygame.display.flip()

def startGame():
       screen.fill((0,0,0));
       pygame.display.flip();
       import dino.py

while menuAtivo:
       for evento in pygame.event.get():
           print(evento);
           if evento.type == pygame.MOUSEBUTTONDOWN:
               if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 230:
                   if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 280:
                           pygame.quit();
               if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 90:
                   if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 140:
                           startGame();