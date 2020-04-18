import os
import pygame as pg

SCREEN_SIZE = (800, 600)
WINDOW_TITLE = 'Plot Master v1.1'
MENU_TITLE = 'Plot Master'
EXIT_BUTTON_NAME = 'Exit'
DRAW_BUTTON_NAME = 'Draw graph!'
EXPORT_TXT_BUTTON_NAME = 'Export txt'
EXPORT_PNG_BUTTON_NAME = 'Export png'
GENERATE_GRAPH_BUTTON_NAME = 'Generate Graph'
FONT_NAME = os.path.join(os.getcwd(), 'resources', 'handwriting.ttf')
TEXTBOX_FONT_NAME = os.path.join(os.getcwd(), 'resources', 'NixieOne.ttf')
TEXTBOX_INACTIVE_COLOR = pg.color.THECOLORS['black']
TEXTBOX_ACTIVE_COLOR = pg.color.THECOLORS['darkcyan']
