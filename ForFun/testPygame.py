import pygame

pygame.init()

window = pygame.display.set_mode((800,600))
pygame.display.set_caption('Game')
main_loop = True

while main_loop:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      main_loop = False

pygame.quit()