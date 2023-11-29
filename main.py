import pygame as pg

from player import Player


def main():
    pg.init()
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    clock = pg.time.Clock()
    running = True

    pg.display.set_caption("Golway")

    font = pg.font.SysFont("Arial", 20)

    surface = pg.Surface((640, 480))

    player = Player()

    surface.blit(font.render("What Kind of Character are You?", True, "white"),
                 (0, 0))

    magus_text = font.render("Magus", True, "blue")
    magus_button = pg.draw.rect(
        surface,
        "dark grey",
        (0, 30, magus_text.get_width() + 5, magus_text.get_height() + 5),
    )
    magus_text_rect = magus_text.get_rect(center=magus_button.center)

    companion_text = font.render("Companion", True, "red")
    companion_button = pg.draw.rect(
        surface,
        "dark grey",
        (magus_button.right + 25, 30,
         companion_text.get_width() + 5, companion_text.get_height() + 5),
    )
    companion_text_rect = companion_text.get_rect(
        center=companion_button.center)

    grog_text = font.render("Grog", True, "white")
    grog_button = pg.draw.rect(
        surface,
        "dark grey",
        (companion_button.right + 25, 30,
         grog_text.get_width() + 5, grog_text.get_height() + 5),
    )
    grog_text_rect = grog_text.get_rect(center=grog_button.center)

    surface.blit(magus_text, magus_text_rect)
    surface.blit(companion_text, companion_text_rect)
    surface.blit(grog_text, grog_text_rect)

    screen.blit(surface, (0, 0))

    while running:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False

        mouse_x, mouse_y = pg.mouse.get_pos()
        if pg.mouse.get_pressed()[0] == 1:
            if magus_button.collidepoint(mouse_x, mouse_y):
                player.type = "Magus"

                surface.fill("black")
                surface.blit(
                    font.render("You are a Magus", True, "white"),
                    (60, 0))
                screen.blit(surface, (0, 0))

        pg.display.flip()
        clock.tick(60)


# call the "main" function if running this script
if __name__ == "__main__":
    main()
    pg.quit()
