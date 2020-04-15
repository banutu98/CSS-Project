import pygame as pg

from gui_components.defines import *
from gui_components.utils import Button


class PlotMenu:
    def __init__(self, screen_size, plot_display=None):
        if plot_display:
            self.plot_display = plot_display
        else:
            self.plot_display = pg.display.set_mode(screen_size)
            self.plot_display.fill(pg.color.THECOLORS['darkslategray'])
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

    def add_element(self, text, font_size, center_location, font_name=FONT_NAME):
        c_elem_surface, c_elem_rect = self.get_text_objects(text, self.get_font(font_size, font_name))
        c_elem_rect.center = center_location
        self.__static_elements.append((c_elem_surface, c_elem_rect))

    def add_button(self, text, font_size, center_location, font_name=FONT_NAME):
        c_elem_surface, c_elem_rect = self.get_text_objects(text, self.get_font(font_size, font_name))
        c_elem_rect.center = center_location
        self.buttons.append(Button(text, c_elem_surface, c_elem_rect))

    def draw(self):
        self.plot_display.fill(pg.color.THECOLORS['darkslategray'])
        for c_elem_surface, c_elem_rect in self.__static_elements:
            self.plot_display.blit(c_elem_surface, c_elem_rect)
        for button in self.buttons:
            self.plot_display.blit(button.surface, button.rect)
        pg.display.update()
        self.clock.tick(30)
