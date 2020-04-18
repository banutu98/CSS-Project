from gui_components.defines import *
from gui_components.utils import Button, InputBox


class DrawScreen:

    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode(SCREEN_SIZE)
        pg.display.set_caption(WINDOW_TITLE)

        self.clock = pg.time.Clock()
        self.buttons = []
        self.text_box = InputBox(self.screen, 10, 10, 100, 32, max_string_length=70)

    def add_button(self, font_name, font_size, button_name, text_color, center_location):
        font = pg.font.Font(font_name, font_size)
        text_surface = font.render(button_name, True, text_color)
        text_location = text_surface.get_rect()
        text_location.center = center_location
        self.buttons.append(Button(button_name, text_surface, text_location, border_width=5))

    def draw_graph(self, points):
        for i in range(len(points) - 1):
            pg.draw.line(self.screen, pg.color.THECOLORS['red'], points[i], points[i + 1])

    def init_buttons(self):
        self.add_button(FONT_NAME, 20, EXIT_BUTTON_NAME, pg.color.THECOLORS['black'], (730, 570))
        self.add_button(FONT_NAME, 20, EXPORT_TXT_BUTTON_NAME, pg.color.THECOLORS['black'], (100, 570))
        self.add_button(FONT_NAME, 20, EXPORT_PNG_BUTTON_NAME, pg.color.THECOLORS['black'], (300, 570))
        self.add_button(FONT_NAME, 20, GENERATE_GRAPH_BUTTON_NAME, pg.color.THECOLORS['black'], (530, 570))

    def draw_buttons(self):
        for button in self.buttons:
            self.screen.blit(button.surface, button.rect)
            if button.border_width:
                button.draw_border(self.screen, pg.color.THECOLORS['black'])

    def run(self):
        self.init_buttons()
        while True:
            self.screen.fill(pg.color.THECOLORS['aquamarine3'])

            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        exit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for button in self.buttons:
                        if button.rect.collidepoint(mouse_pos):
                            if button.name == EXIT_BUTTON_NAME:
                                exit()
                            elif button.name == GENERATE_GRAPH_BUTTON_NAME:
                                print('Generate graph!')
                            elif button.name == EXPORT_TXT_BUTTON_NAME:
                                print('Export txt!')
                            elif button.name == EXPORT_PNG_BUTTON_NAME:
                                print('Export png!')
                self.text_box.handle_event(event)

            self.text_box.update()
            self.text_box.draw()
            self.draw_buttons()
            # self.draw_graph([(10, 32), (50, 60), (78, 80)])

            pg.display.update()
            self.clock.tick(30)
