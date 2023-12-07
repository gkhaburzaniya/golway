from dataclasses import dataclass

import pygame as pg
import constants


@dataclass(eq=False)
class Player:

    creation_step = 0

    type: str = ""
    name: str = ""
    age: float = 0

    # characteristics
    intelligence: int = -10
    perception: int = -10
    strength: int = -10
    stamina: int = -10
    presence: int = -10
    communication: int = -10
    dexterity: int = -10
    quickness: int = -10

    def create_character(self, surface):
        font = pg.font.SysFont("Arial", 20)

        if self.creation_step == 0:
            magus_text = font.render("Magus", True, "blue")
            self.magus_button = pg.draw.rect(
                surface,
                "dark grey",
                (0, 30, magus_text.get_width() + 5,
                 magus_text.get_height() + 5),
            )
            magus_text_rect = magus_text.get_rect(
                center=self.magus_button.center)

            companion_text = font.render("Companion", True, "red")
            self.companion_button = pg.draw.rect(
                surface,
                "dark grey",
                (self.magus_button.right + 25, 30,
                 companion_text.get_width() + 5,
                 companion_text.get_height() + 5),
            )
            companion_text_rect = companion_text.get_rect(
                center=self.companion_button.center)

            grog_text = font.render("Grog", True, "white")
            self.grog_button = pg.draw.rect(
                surface,
                "dark grey",
                (self.companion_button.right + 25, 30,
                 grog_text.get_width() + 5, grog_text.get_height() + 5),
            )
            grog_text_rect = grog_text.get_rect(center=self.grog_button.center)
            surface.blit(font.render("What Kind of Character are You?", True,
                                     "white"), (0, 0))
            surface.blit(magus_text, magus_text_rect)
            surface.blit(companion_text, companion_text_rect)
            surface.blit(grog_text, grog_text_rect)
            self.creation_step += 1

        mouse_x, mouse_y = pg.mouse.get_pos()
        mouse_x, mouse_y = mouse_x - constants.SURFACE_X, mouse_y - constants.SURFACE_Y
        if pg.mouse.get_pressed()[0] == 1:
            if self.magus_button.collidepoint(mouse_x, mouse_y):
                self.type = "Magus"

                surface.fill("black")
                surface.blit(
                    font.render("You are a Magus", True, "white"),
                    (60, 0))
                return True
            if self.companion_button.collidepoint(mouse_x, mouse_y):
                self.type = "Companion"

                surface.fill("black")
                surface.blit(
                    font.render("You are a Companion", True, "white"),
                    (60, 0))
                return True
            if self.grog_button.collidepoint(mouse_x, mouse_y):
                self.type = "Grog"

                surface.fill("black")
                surface.blit(
                    font.render("You are a Grog", True, "white"),
                    (60, 0))
                return True

    def change_intelligence(self, change):
        self.intelligence += change
        return self._change_characteristic("Intelligence", change)

    def change_perception(self, change):
        self.perception += change
        return self._change_characteristic("Perception", change)

    def change_strength(self, change):
        self.strength += change
        return self._change_characteristic("Strength", change)

    def change_stamina(self, change):
        self.stamina += change
        return self._change_characteristic("Stamina", change)

    def change_presence(self, change):
        self.presence += change
        return self._change_characteristic("Presence", change)

    def change_communication(self, change):
        self.communication += change
        return self._change_characteristic("Communication", change)

    def change_dexterity(self, change):
        self.dexterity += change
        return self._change_characteristic("Dexterity", change)

    def change_quickness(self, change):
        self.quickness += change
        return self._change_characteristic("Quickness", change)

    def change_name(self, new_name):
        self.name = new_name
        return f"Your name is {new_name}"

    @staticmethod
    def _change_characteristic(characteristic, change):
        if change > 0:
            return f"+{change} {characteristic}"
        elif change < 0:
            return f"{change} {characteristic}"
        else:
            raise ValueError
