import pygame_widgets
from constants import *
from buttons import Group_of_buttons
import pygame
import webbrowser
import time


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SIZE)
    all_sprites = pygame.sprite.Group()
    running = True

    planet_buttons = Group_of_buttons(screen, 0, 25, 150, 390, PLANETS, len(PLANETS), 'Times New Roman')
    mode_buttons = Group_of_buttons(screen, 200, 15, 300, 50, ['Описание', 'Физ. характеристики'], 2, FONT,
                                    False)
    planet = CLASSES_OF_PLANETS[planet_buttons.actual_button]
    all_sprites.add(planet_buttons)

    while running:
        screen.fill((43, 43, 43))
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False
        if (pygame.mouse.get_pressed() and
                pygame.rect.Rect(700, 406, 20, 200).collidepoint(pygame.mouse.get_pos())):
            webbrowser.open(planet.wiki)
            time.sleep(1)
        pygame_widgets.update(events)
        planet = CLASSES_OF_PLANETS[planet_buttons.actual_button]

        if mode_buttons.actual_button == 'Физ. характеристики':
            img = planet.image
            text = pygame.font.SysFont(FONT, 14).render(f'''Имя: {planet.name} \n
Тип: {planet.type} \n
Радиус: {planet.radius} \n
Диаметр: {planet.diameter}\n
Масса: {planet.mass}\n
Длительность года: {planet.year_duration}\n
Длительность дня: {planet.day_duration}\n
Божество: {planet.ancient_god}\n
Спутники: {", ".join(planet.satellites)}\n
Ссылка на википедию: {planet.wiki}''', True, (255, 255, 255))
        else:
            img = CLASSES_OF_PLANETS[planet_buttons.actual_button].gif.blit_ready()
            img.set_colorkey(planet.backcolor)
            text = pygame.font.SysFont(FONT, 14).render(planet.description, True, (255, 255, 255))

        screen.blit(img, (200, 100))
        screen.blit(text, (675, 100))
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
