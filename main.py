import pygame as pg

from player import Player


def main():
    pg.init()
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    clock = pg.time.Clock()
    running = True

    pg.display.set_caption("Golway")
    surface = pg.Surface((640, 480))
    player = Player()
    player.started = False

    while running:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False

        if not player.type:
            player.create_character(surface)

        screen.blit(surface, (0, 0))
        pg.display.flip()
        clock.tick(60)


# call the "main" function if running this script
if __name__ == "__main__":
    main()
    pg.quit()
