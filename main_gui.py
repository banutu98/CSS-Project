from gui_components.defines import *
from gui_components.PlotMenu import PlotMenu
from gui_components.DrawScreen import DrawScreen


class MainScreen:
    def __init__(self):
        self.intro = True
        self.graph_drawing = False

    def init_screen(self):
        screen = pg.display.set_mode(SCREEN_SIZE)
        pg.display.set_caption(WINDOW_TITLE)
        icon = pg.image.load('resources/bar-chart.png')
        pg.display.set_icon(icon)

        menu = PlotMenu(SCREEN_SIZE, screen)
        menu.add_element(MENU_TITLE, 60, (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 6))
        print((SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 6))
        menu.add_button(DRAW_BUTTON_NAME, 30, (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] - 150))
        menu.add_button(EXIT_BUTTON_NAME, 30, (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] - 75))

        self.menu = menu

    def getIntroState(self):
        return self.intro

    def getGraphDrawingState(self):
        return self.graph_drawing

    def runIntroScreen(self):
        for event in pg.event.get():
            print(event)
            if event.type == pg.QUIT:
                exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for button in self.menu.buttons:
                    if button.rect.collidepoint(mouse_pos):
                        if button.name == EXIT_BUTTON_NAME:
                            exit()
                        elif button.name == DRAW_BUTTON_NAME:
                            self.intro = False
                            self.graph_drawing = True

        self.menu.draw()

    def start_gui(self):
        pg.init()
        self.init_screen()

        while True:
            while self.intro:
                self.runIntroScreen()
            if self.graph_drawing:
                DrawScreen().run()
            self.intro = True
            self.graph_drawing = False


if __name__ == '__main__':
    main_screen = MainScreen()
    main_screen.start_gui()
