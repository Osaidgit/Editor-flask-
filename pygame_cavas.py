import pygame

current_tool = 'brush'

def update_tool(tool):
    global current_tool
    current_tool = tool

def run():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pygame Canvas")

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        font = pygame.font.SysFont(None, 36)
        text = font.render(f'Tool: {current_tool}', True, (0, 0, 0))
        screen.blit(text, (20, 20))
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
