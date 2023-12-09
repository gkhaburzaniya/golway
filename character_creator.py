import pygame as pg

import constants


def step_1(player, surface, buttons):
    font = pg.font.SysFont("Arial", 20)

    magus_text = font.render("Magus", True, "blue")
    magus_button = pg.draw.rect(
        surface,
        "dark grey",
        (0, 30, magus_text.get_width() + 5,
         magus_text.get_height() + 5),
    )
    magus_text_rect = magus_text.get_rect(center=magus_button.center)

    companion_text = font.render("Companion", True, "red")
    companion_button = pg.draw.rect(
        surface,
        "dark grey",
        (magus_button.right + 25, 30,
         companion_text.get_width() + 5,
         companion_text.get_height() + 5),
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
    surface.blit(font.render("What Kind of Character are You?", True,
                             "white"), (0, 0))
    surface.blit(magus_text, magus_text_rect)
    surface.blit(companion_text, companion_text_rect)
    surface.blit(grog_text, grog_text_rect)
    return magus_button, companion_button, grog_button


def step_2(player, surface, buttons):
    font = pg.font.SysFont("Arial", 20)

    mouse_x, mouse_y = pg.mouse.get_pos()
    mouse_x = mouse_x - constants.SURFACE_X
    mouse_y = mouse_y - constants.SURFACE_Y
    if pg.mouse.get_pressed()[0] == 1:
        if buttons[0].collidepoint(mouse_x, mouse_y):
            player.type = "Magus"

            surface.fill("black")
            surface.blit(
                font.render("You are a Magus", True, "white"),
                (60, 0))
            return True
        if buttons[1].collidepoint(mouse_x, mouse_y):
            player.type = "Companion"

            surface.fill("black")
            surface.blit(
                font.render("You are a Companion", True, "white"),
                (60, 0))
            return True
        if buttons[2].collidepoint(mouse_x, mouse_y):
            player.type = "Grog"

            surface.fill("black")
            surface.blit(
                font.render("You are a Grog", True, "white"),
                (60, 0))
            return True


steps = [step_1, step_2]
