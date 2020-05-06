import unittest
import pygame as pg
from main_gui import MainScreen

class TestMainGUI(unittest.TestCase):
    def setUp(self):
        pg.init()
        self.main_screen = MainScreen()
        self.main_screen.init_screen()

    def test_draw_transition(self):
        mouse_event = pg.event.Event(pg.MOUSEBUTTONDOWN, {'pos': (478, 440), 'button': 1})
        self.main_screen.runIntroScreen()
        pg.event.post(mouse_event)
        self.main_screen.runIntroScreen()

        self.assertEqual(self.main_screen.getGraphDrawingState(), True)


if __name__ == '__main__':
    unittest.main()