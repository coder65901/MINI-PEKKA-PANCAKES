import pygame

pygame.init()
screen = pygame.display.set_mode((590,200))
pygame.display.set_caption("PYGAME")
clock = pygame.time.Clock()

test_surface = pygame.Surface((10,10))
test_surface.fill('red')
moveRight = 10
while True:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
     pygame.register_quit(callable)
     pygame.quit()
     exit()
  clock.tick(60)
  screen.blit(test_surface, (moveRight,10))
  moveRight +=1
  pygame.display.update()
