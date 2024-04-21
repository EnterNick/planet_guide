import pygame.sprite
from pygame_widgets.button import Button

from constants import *


class Group_of_buttons(pygame.sprite.Sprite):
    def __init__(self, screen, x: int, y: int, width: int, height: int, names: list[str], number_of_buttons: int,
                 font: str, horizontal: bool = True):
        super().__init__()
        self.width: int = width
        self.height = height
        self.names_of_buttons = names
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont(font, 15)
        self.rect = pygame.rect.Rect(x, y, width, height)
        self.buttons = []
        for i, name in enumerate(names):
            if horizontal:
                self.buttons.append(Button(screen, x, y + height // number_of_buttons * i, self.width,
                                           height // number_of_buttons, font=self.font, text=name,
                                           onClick=self.update, onClickParams=[i], colour=(80, 80, 80)))
            else:
                self.buttons.append(Button(screen, x + width // number_of_buttons * i, y,
                                           self.width // number_of_buttons, self.height, font=self.font,
                                           text=name, onClick=self.update, onClickParams=[i], colour=(80, 80, 80)))
        self.actual_button = names[0]
        self.buttons[0].setInactiveColour((50, 50, 50))

    def update(self, n):
        for i in self.buttons:
            i.setInactiveColour((80, 80, 80))
        self.buttons[n].setInactiveColour((50, 50, 50))
        self.actual_button = self.names_of_buttons[n]
