import pygame

pygame.init()
screen = pygame.display.set_mode((590,200))
pygame.display.set_caption("PYGAME")
clock = pygame.time.Clock()

test_surface = pygame.Surface((700,400))
test_surface.fill('red')
while True:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
     pygame.register_quit(callable)
     pygame.quit()
     exit()
  clock.tick(60)
  screen.blit(test_surface, (0,0))
  pygame.display.update()
