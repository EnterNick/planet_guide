from dataclasses import dataclass
import datetime

import pygame.surface


def shere(r):
    res = pygame.surface.Surface((r, r))
    res.fill((43, 43, 43))
    for i in range(9):
        pygame.draw.ellipse(res, (255, 255, 255), (0 + i * r // 16, 0, r - r // 8 * i, r), width=1)
        pygame.draw.ellipse(res, (255, 255, 255), (0, 0 + i * r // 16, r, r - r // 8 * i), width=1)
    return res


@dataclass
class Planet:
    radius: float
    diameter: float
    mass: float
    surface: float
    year_duration: float
    day_duration: float
    type: str
    distance_to_sun: float
    ancient_god: str
    description: str
    satellites: list[str]
    wiki: str
    image: pygame.surface.Surface


class Earth(Planet):
    radius = 6371.004
    diameter = radius * 2
    surface = 509494365.0
    day_duration = datetime.time(23, 56, 4, 99)
    distance_to_sun = 149.6 * 10 ** 6
    mass = 5.9726 * 10 ** 24
    year_duration = '365 дней, 6 часов, 9 минут, 10 секунд'
    type = 'Земная группа'
    ancient_god = None
    satellites = ['Луна']
    description = ('Земля́ — третья по удалённости от Солнца планета Солнечной системы. Самая плотная, пятая по '
                   'диаметру'
                   ' и массе среди всех планет Солнечной системы и крупнейшая среди планет земной группы, в которую'
                   ' входят также Меркурий, Венера и Марс. Единственное известное человеку в настоящее время тело во'
                   ' Вселенной, населённое живыми организмами. В публицистике и научно-популярной литературе могут'
                   ' использоваться синонимические термины — мир, голубая планета, Терра (от лат. Terra).')
    wiki = 'https://ru.wikipedia.org/wiki/Земля'
    image = shere(250)


class Mercury(Planet):
    radius = 6371.004
    diameter = radius * 2
    surface = 509494365.0
    day_duration = '176 земных суток'
    distance_to_sun = 149.6 * 10 ** 6
    mass = 5.9726 * 10 ** 24
    year_duration = '87 дней, 23 часов, 15 минут, 21 секунда'
    type = 'Земная группа'
    ancient_god = 'Древнеримскй бог торговли'
    satellites = []
    description = ('''Мерку́рий — наименьшая планета Солнечной системы и самая близкая к Солнцу. Названа в честь
     древнеримского бога торговли — быстрого Меркурия, поскольку она движется по небу быстрее других планет. 
     Видимое расстояние Меркурия от Солнца, если смотреть с Земли, никогда не превышает 28°. Эта близость к 
     Солнцу означает, что планету можно увидеть только в течение небольшого времени после захода или до восхода 
     солнца, обычно в сумерках. В телескоп у Меркурия можно увидеть фазы, изменяющиеся от тонкого серпа до почти 
     полного диска, как у Венеры и Луны, а иногда он проходит по диску Солнца.''')
    wiki = 'https://ru.wikipedia.org/wiki/Меркурий'
    image = shere(200)


class Venus(Planet):
    pass


class Mars(Planet):
    pass


class Jupiter(Planet):
    pass


class Saturn(Planet):
    pass


class Neptun(Planet):
    pass


class Uran(Planet):
    pass
