from gui_components.defines import *
from gui_components.utils import Button


class InstructionsScreen:

    def __init__(self):
        pg.init()
        pg.display.set_caption(WINDOW_TITLE)

        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()
        self.buttons = []
        self.texts = []

    def add_button(self, font_name, font_size, button_name, text_color, center_location):
        font = pg.font.Font(font_name, font_size)
        text_surface = font.render(button_name, True, text_color)
        text_location = text_surface.get_rect()
        text_location.center = center_location
        self.buttons.append(Button(button_name, text_surface, text_location, border_width=5))

    def init_buttons(self):
        self.add_button(FONT_NAME, 20, EXIT_BUTTON_NAME, pg.color.THECOLORS['black'], (730, 570))
        self.add_button(FONT_NAME, 20, BACK_BUTTON_NAME, pg.color.THECOLORS['black'], (110, 570))

    def init_texts(self):
        text_surface = pg.font.Font(FONT_NAME, 40).render('How to use PlotMaster', True, pg.color.THECOLORS['black'])
        text_rect = text_surface.get_rect()
        text_rect.center = (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 6)
        self.texts.append((text_surface, text_rect))

        text_surface = pg.font.Font(FONT_NAME, 18).render('* the function law supports basic mathematical operations,',
                                                          True, pg.color.THECOLORS['black'])
        text_rect = text_surface.get_rect()
        text_rect.topleft = (50, 170)
        self.texts.append((text_surface, text_rect))

        text_surface = pg.font.Font(FONT_NAME, 18).render('trigonometric functions and an integral function',
                                                          True, pg.color.THECOLORS['black'])
        text_rect = text_surface.get_rect()
        text_rect.topleft = (50, 200)
        self.texts.append((text_surface, text_rect))

        text_surface = pg.font.Font(FONT_NAME, 18).render('* the minimum, maximum and step values should be float '
                                                          'numbers',
                                                          True, pg.color.THECOLORS['black'])
        text_rect = text_surface.get_rect()
        text_rect.topleft = (50, 230)
        self.texts.append((text_surface, text_rect))

        text_surface = pg.font.Font(FONT_NAME, 18).render('Examples:',
                                                          True, pg.color.THECOLORS['black'])
        text_rect = text_surface.get_rect()
        text_rect.topleft = (50, 300)
        self.texts.append((text_surface, text_rect))
        self.texts.append((text_surface, text_rect))    # double append for bold effect

        text_surface = pg.font.Font(TEXTBOX_FONT_NAME, 18).render('* Function: cos(x) , Min: -7, Max: -2.3, Step: 0.5',
                                                                  True, pg.color.THECOLORS['black'])
        text_rect = text_surface.get_rect()
        text_rect.topleft = (50, 350)
        self.texts.append((text_surface, text_rect))
        self.texts.append((text_surface, text_rect))

        text_surface = pg.font.Font(TEXTBOX_FONT_NAME, 18).render('* Function: integrala(sin(x)), Min: 1, Max: 10, Step: 1',
                                                                  True, pg.color.THECOLORS['black'])
        text_rect = text_surface.get_rect()
        text_rect.topleft = (50, 400)
        self.texts.append((text_surface, text_rect))
        self.texts.append((text_surface, text_rect))

        text_surface = pg.font.Font(TEXTBOX_FONT_NAME, 18).render('* Function: x**x+2, Min: -10, Max: 10, Step: 2',
                                                                  True, pg.color.THECOLORS['black'])
        text_rect = text_surface.get_rect()
        text_rect.topleft = (50, 450)
        self.texts.append((text_surface, text_rect))
        self.texts.append((text_surface, text_rect))

    def draw_buttons(self):
        for button in self.buttons:
            self.screen.blit(button.surface, button.rect)
            if button.border_width:
                button.draw_border(self.screen, pg.color.THECOLORS['black'])

    def run(self):
        self.init_buttons()
        self.init_texts()
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
                            elif button.name == BACK_BUTTON_NAME:
                                return
            for text in self.texts:
                self.screen.blit(text[0], text[1])
            self.draw_buttons()

            pg.display.update()
            self.clock.tick(30)
