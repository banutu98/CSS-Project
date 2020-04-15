import pygame as pg


class BoolMenuElement:
    def __init__(self, text, font_size, center_location, font_name='freesansbold.ttf', bool_name=None,
                 bool_value=None, game_display=None):
        self.text = text
        self.font_size = font_size
        self.center_location = center_location
        self.font_name = font_name
        self.bool_name = bool_name
        self.bool_value = bool_value
        self.game_display = game_display
        self.value = True

    def draw(self):
        c_text = self.text + self.bool_value[self.value]
        c_elem_surface, c_elem_rect = PlotMenu.get_text_objects(c_text,
                                                                PlotMenu.get_font(self.font_size, self.font_name))
        c_elem_rect.center = self.center_location
        self.game_display.blit(c_elem_surface, c_elem_rect)

    def change_bool_value(self, value):
        self.value = value


class PlotMenu:
    def __init__(self, screen_size, game_display=None):
        if game_display:
            self.game_display = game_display
        else:
            self.game_display = pg.display.set_mode(screen_size)
            self.game_display.fill(pg.color.THECOLORS['magenta'])
        self.__static_elements = []
        self.bool_element = None
        self.screen_size = screen_size
        self.clock = pg.time.Clock()

    @staticmethod
    def get_font(font_size, font_name):
        return pg.font.Font(font_name, font_size)

    @staticmethod
    def get_text_objects(text, font):
        text_surface = font.render(text, True, pg.color.THECOLORS['black'])
        return text_surface, text_surface.get_rect()

    def add_element(self, text, font_size, center_location, font_name='freesansbold.ttf', bool_name=None,
                    bool_value=None):
        if bool_name:
            self.bool_element = BoolMenuElement(text, font_size, center_location, font_name, bool_name, bool_value,
                                                self.game_display)
        else:
            c_elem_surface, c_elem_rect = self.get_text_objects(text, self.get_font(font_size, font_name))
            c_elem_rect.center = center_location
            self.__static_elements.append((c_elem_surface, c_elem_rect))

    def draw(self):
        self.game_display.fill(pg.color.THECOLORS['magenta'])
        for c_elem_surface, c_elem_rect in self.__static_elements:
            self.game_display.blit(c_elem_surface, c_elem_rect)
        if self.bool_element:
            self.bool_element.draw()
        pg.display.update()
        self.clock.tick(15)

    def update_bool(self, value):
        if self.bool_element:
            self.bool_element.change_bool_value(value)
