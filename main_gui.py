import pygame as pg
import pygame.colordict as pg_colors
from gui_components.plot_menu import PlotMenu

SCREEN_SIZE = (800, 600)


def draw_graph(screen, points):
    for i in range(len(points) - 1):
        pg.draw.line(screen, pg_colors.THECOLORS['red'], points[i], points[i + 1])


def init_screen():
    screen = pg.display.set_mode(SCREEN_SIZE)
    pg.display.set_caption('Plot Master v1.1')
    icon = pg.image.load('resources/bar-chart.png')
    pg.display.set_icon(icon)

    menu = PlotMenu(SCREEN_SIZE, screen)
    menu.add_alement('Plot Master', 60, ((SCREEN_SIZE[0] / 2), (SCREEN_SIZE[1] / 6)))
    return menu


def start_gui():
    pg.init()
    menu = init_screen()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    exit()
            elif event.type == pg.QUIT:
                exit()
        menu.draw()


if __name__ == '__main__':
    start_gui()
