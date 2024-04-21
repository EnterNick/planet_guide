import pygame_widgets
import gif_pygame
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
    mode_buttons.actual_button = 'Физ. характеристики'
    all_sprites.add(planet_buttons)

    while running:
        screen.fill((43, 43, 43))
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False
        pygame_widgets.update(events)

        if mode_buttons.actual_button == 'Физ. характеристики':
            img = CLASSES_OF_PLANETS[planet_buttons.actual_button].image
        else:
            img = CLASSES_OF_PLANETS[planet_buttons.actual_button].gif.blit_ready()
            img.set_colorkey((255, 255, 255))

        screen.blit(img, (200, 100))
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
