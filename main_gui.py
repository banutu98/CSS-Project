import pickle as pkl

from gui_components.defines import *
from gui_components.PlotMenu import PlotMenu
from gui_components.DrawScreen import DrawScreen


def init_screen():
    screen = pg.display.set_mode(SCREEN_SIZE)
    pg.display.set_caption(WINDOW_TITLE)
    icon = pg.image.load(ICON_PATH)
    pg.display.set_icon(icon)

    menu = PlotMenu(SCREEN_SIZE, screen)
    menu.add_element(MENU_TITLE, 60, (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 6))
    menu.add_button(DRAW_BUTTON_NAME, 30, (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] - 150))
    menu.add_button(EXIT_BUTTON_NAME, 30, (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] - 75))
    return menu


def start_gui():
    pg.init()
    menu = init_screen()

    intro = True
    graph_drawing = False
    while True:
        events_list = list()
        while intro:
            for event in pg.event.get():
                events_list.append([event.type, event.dict])
                if event.type == pg.QUIT:
                    exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        with open(os.path.join('pygame_events', 'events_main_gui.pkl'), 'wb') as f:
                            pkl.dump(events_list, f)
                        exit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for button in menu.buttons:
                        if button.rect.collidepoint(mouse_pos):
                            if button.name == EXIT_BUTTON_NAME:
                                exit()
                            elif button.name == DRAW_BUTTON_NAME:
                                intro = False
                                graph_drawing = True
            menu.draw()
        if graph_drawing:
            DrawScreen().run()
        intro = True
        graph_drawing = False


if __name__ == '__main__':
    start_gui()
