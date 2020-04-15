import pygame as pg

from gui_components.defines import *
from gui_components.utils import Button


class DrawScreen:

    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode(SCREEN_SIZE)
        pg.display.set_caption(WINDOW_TITLE)

        self.clock = pg.time.Clock()
        self.buttons = []

    def init_buttons(self):
        font = pg.font.Font(FONT_NAME, 20)
        text_surface = font.render(EXIT_BUTTON_NAME, True, pg.color.THECOLORS['black'])
        text_location = text_surface.get_rect()
        text_location.center = (750, 570)
        self.buttons.append(Button(EXIT_BUTTON_NAME, text_surface, text_location))

        font = pg.font.Font(FONT_NAME, 20)
        text_surface = font.render(EXPORT_TXT_BUTTON_NAME, True, pg.color.THECOLORS['black'])
        text_location = text_surface.get_rect()
        text_location.center = (100, 570)
        self.buttons.append(Button(EXPORT_TXT_BUTTON_NAME, text_surface, text_location))

        font = pg.font.Font(FONT_NAME, 20)
        text_surface = font.render(EXPORT_PNG_BUTTON_NAME, True, pg.color.THECOLORS['black'])
        text_location = text_surface.get_rect()
        text_location.center = (300, 570)
        self.buttons.append(Button(EXPORT_PNG_BUTTON_NAME, text_surface, text_location))

    def draw_buttons(self):
        for button in self.buttons:
            self.screen.blit(button.surface, button.rect)

    def run(self):
        self.init_buttons()
        while True:
            self.screen.fill(pg.color.THECOLORS['white'])
            for event in pg.event.get():
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
                            elif button.name == EXPORT_TXT_BUTTON_NAME:
                                print('Export txt!')
                            elif button.name == EXPORT_PNG_BUTTON_NAME:
                                print('Export png!')

            self.draw_buttons()
            pg.display.update()
            self.clock.tick(30)
