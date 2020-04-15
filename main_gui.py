import pygame as pg
import pygame.colordict as pg_colors

from gui_components.plot_menu import PlotMenu
from gui_components.draw_screen import DrawScreen

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
    menu.add_element('Plot Master', 60, (SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 6))
    menu.add_button('Draw graph!', 30, (SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] - 175))
    menu.add_button('Exit', 30, (SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] - 100))
    return menu


def start_gui():
    pg.init()
    menu = init_screen()

    intro = True
    graph_drawing = False
    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for button in menu.buttons:
                    if button.rect.collidepoint(mouse_pos):
                        if button.name == 'Exit':
                            exit()
                        else:
                            intro = False
                            graph_drawing = True
        menu.draw()
    if graph_drawing:
        DrawScreen().run()  # TODO: Needs implementation


if __name__ == '__main__':
    start_gui()
