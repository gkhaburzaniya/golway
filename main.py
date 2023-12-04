import pygame as pg
import constants

from player import Player


def main():
    pg.init()
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    constants.SURFACE_X = screen.get_width()/2-320
    constants.SURFACE_Y = screen.get_height()/2-240
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

        screen.blit(surface, (constants.SURFACE_X, constants.SURFACE_Y))
        pg.display.flip()
        clock.tick(60)


# call the "main" function if running this script
if __name__ == "__main__":
    main()
    pg.quit()
