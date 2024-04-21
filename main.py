import pygame_widgets

from constants import *
from buttons import Group_of_buttons
import pygame


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SIZE)
    all_sprites = pygame.sprite.Group()
    running = True

    planet_buttons = Group_of_buttons(screen, 0, 25, 150, 390, PLANETS, len(PLANETS), 'Times New Roman')
    mode_buttons = Group_of_buttons(screen, 200, 15, 300, 50, ['Описание', 'Физ. характеристики'], 2, 'Times New Roman',
                                    False)
    all_sprites.add(planet_buttons)
    while running:
        screen.fill((43, 43, 43))
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False

        pygame_widgets.update(events)
        planet_img = CLASSES_OF_PLANETS[planet_buttons.actual_button].image \
            if mode_buttons.actual_button == 'Физ. характеристики' \
            else CLASSES_OF_PLANETS[planet_buttons.actual_button].image
        screen.blit(planet_img, (200, 100))

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
