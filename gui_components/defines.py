import os
import pygame as pg

SCREEN_SIZE = (800, 600)
ERROR_SURFACE_SIZE = (550, 100)
WINDOW_TITLE = 'PlotMaster v1.1'
MENU_TITLE = 'PlotMaster'
OK_BUTTON_NAME = 'OK'
EXIT_BUTTON_NAME = 'Exit'
INSTRUCTIONS_BUTTON_NAME = 'Instructions'
BACK_BUTTON_NAME = 'Go back'
DRAW_BUTTON_NAME = 'Draw graph!'
EXPORT_TXT_BUTTON_NAME = 'Export txt'
EXPORT_PNG_BUTTON_NAME = 'Export png'
GENERATE_GRAPH_BUTTON_NAME = 'Generate Graph'
if 'test' not in os.getcwd():
    FONT_NAME = os.path.join(os.getcwd(), 'resources', 'handwriting.ttf')
    TEXTBOX_FONT_NAME = os.path.join(os.getcwd(), 'resources', 'NixieOne.ttf')
    ICON_PATH = os.path.join(os.getcwd(), 'resources', 'bar-chart.png')
else:
    FONT_NAME = os.path.join(os.getcwd(), '..', 'resources', 'handwriting.ttf')
    TEXTBOX_FONT_NAME = os.path.join(os.getcwd(), '..', 'resources', 'NixieOne.ttf')
    ICON_PATH = os.path.join(os.getcwd(), '..', 'resources', 'bar-chart.png')
TEXTBOX_INACTIVE_COLOR = pg.color.THECOLORS['black']
TEXTBOX_ACTIVE_COLOR = pg.color.THECOLORS['darkcyan']
ZOOM_PROPORTION = 0.1
MIN_INTERVAL_LENGTH = 1.0
MAX_INTERVAL_LENGTH = 10000.0
NR_RECTANGLES = 1000
