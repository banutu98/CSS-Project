import os
import pygame as pg

SCREEN_SIZE = (800, 600)
WINDOW_TITLE = 'PlotMaster v1.1'
MENU_TITLE = 'PlotMaster'
EXIT_BUTTON_NAME = 'Exit'
INSTRUCTIONS_BUTTON_NAME = 'Instructions'
BACK_BUTTON_NAME = 'Go back'
DRAW_BUTTON_NAME = 'Draw graph!'
EXPORT_TXT_BUTTON_NAME = 'Export txt'
EXPORT_PNG_BUTTON_NAME = 'Export png'
GENERATE_GRAPH_BUTTON_NAME = 'Generate Graph'
FONT_NAME = os.path.join(os.getcwd(), 'resources', 'handwriting.ttf')
TEXTBOX_FONT_NAME = os.path.join(os.getcwd(), 'resources', 'NixieOne.ttf')
TEXTBOX_INACTIVE_COLOR = pg.color.THECOLORS['black']
TEXTBOX_ACTIVE_COLOR = pg.color.THECOLORS['darkcyan']
ZOOM_PROPORTION = 0.05
