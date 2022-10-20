# Author Bryce Woodard 
import pygame

class Window:
    def __init__(self, size, title):
        pygame.init()
        Window.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)

        Window.running = True

    def run(self):
        """Run the main event loop."""
        while Window.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Window.running = False

            Window.screen.fill(pygame.Color(0,0,0))
            pygame.display.update()

        pygame.quit()



        

