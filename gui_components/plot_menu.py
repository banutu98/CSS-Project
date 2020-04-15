import pygame as pg


class Button:

    def __init__(self, name, surface, rect):
        self.name = name
        self.surface = surface
        self.rect = rect


class PlotMenu:
    def __init__(self, screen_size, game_display=None):
        if game_display:
            self.game_display = game_display
        else:
            self.game_display = pg.display.set_mode(screen_size)
            self.game_display.fill(pg.color.THECOLORS['magenta'])
        self.__static_elements = []
        self.buttons = []
        self.screen_size = screen_size
        self.clock = pg.time.Clock()

    @staticmethod
    def get_font(font_size, font_name):
        return pg.font.Font(font_name, font_size)

    @staticmethod
    def get_text_objects(text, font):
        text_surface = font.render(text, True, pg.color.THECOLORS['black'])
        return text_surface, text_surface.get_rect()

    def add_element(self, text, font_size, center_location, font_name='freesansbold.ttf'):
        c_elem_surface, c_elem_rect = self.get_text_objects(text, self.get_font(font_size, font_name))
        c_elem_rect.center = center_location
        self.__static_elements.append((c_elem_surface, c_elem_rect))

    def add_button(self, text, font_size, center_location, font_name='freesansbold.ttf'):
        c_elem_surface, c_elem_rect = self.get_text_objects(text, self.get_font(font_size, font_name))
        c_elem_rect.center = center_location
        self.buttons.append(Button(text, c_elem_surface, c_elem_rect))

    def draw(self):
        self.game_display.fill(pg.color.THECOLORS['magenta'])
        for c_elem_surface, c_elem_rect in self.__static_elements:
            self.game_display.blit(c_elem_surface, c_elem_rect)
        for button in self.buttons:
            self.game_display.blit(button.surface, button.rect)
        pg.display.update()
        self.clock.tick(30)
