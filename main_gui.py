import pickle as pkl

from gui_components.defines import *
from gui_components.PlotMenu import PlotMenu
from gui_components.DrawScreen import DrawScreen


class MainGui:

    def __init__(self):
        self.intro = True
        self.graph_drawing = False

    def init_screen(self):
        screen = pg.display.set_mode(SCREEN_SIZE)
        pg.display.set_caption(WINDOW_TITLE)
        icon = pg.image.load(ICON_PATH)
        pg.display.set_icon(icon)

        menu = PlotMenu(SCREEN_SIZE, screen)
        menu.add_element(MENU_TITLE, 60, (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 6))
        menu.add_button(DRAW_BUTTON_NAME, 30, (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] - 150))
        menu.add_button(EXIT_BUTTON_NAME, 30, (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] - 75))
        return menu

    def start_gui(self):
        pg.init()
        menu = self.init_screen()

        while True:
            events_list = list()
            while self.intro:
                for event in pg.event.get():
                    events_list.append([event.type, event.dict])
                    if event.type == pg.QUIT:
                        exit()
                    elif event.type == pg.KEYDOWN:
                        if event.key == pg.K_ESCAPE:
                            exit()
                    elif event.type == pg.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos
                        for button in menu.buttons:
                            if button.rect.collidepoint(mouse_pos):
                                if button.name == EXIT_BUTTON_NAME:
                                    exit()
                                elif button.name == DRAW_BUTTON_NAME:
                                    self.intro = False
                                    self.graph_drawing = True
                menu.draw()
            if self.graph_drawing:
                DrawScreen().run()
            self.intro = True
            self.graph_drawing = False


if __name__ == '__main__':
    main_gui = MainGui()
    main_gui.start_gui()
