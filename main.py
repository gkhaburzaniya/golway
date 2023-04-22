import pygame

from player import Player

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True

pygame.display.set_caption("Golway")

font = pygame.font.SysFont("Arial", 20)

# Create a new surface for the player attributes
attributes_surface = pygame.Surface((200, 200))

# Render the player attributes onto the surface
player = Player()
intelligence_text = font.render(f"INT: {player.intelligence}", True, "white")
strength_text = font.render(f"STR: {player.strength}", True, "white")
dexterity_text = font.render(f"DEX: {player.dexterity}", True, "white")
stamina_text = font.render(f"STA: {player.stamina}", True, "white")

# Blit the player attributes onto the screen
attributes_surface.blit(intelligence_text, (0, 0))
attributes_surface.blit(strength_text, (0, 30))
attributes_surface.blit(dexterity_text, (0, 60))
attributes_surface.blit(stamina_text, (0, 90))
screen.blit(attributes_surface, (0, 0))

# Update the display
pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
