import unittest

from unittest.mock import MagicMock
from gui_components.defines import *
from gui_components.main_gui import MainGui

EVENTS = []


def side_effect():
    return EVENTS


class MainGuiTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.main_gui = MainGui()

    def test_main_gui_escape(self):
        global EVENTS
        EVENTS = list()
        self.main_gui = MainGui()
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.KEYDOWN, {'key': pg.K_ESCAPE, 'mod': 0}))
        self.assertRaises(SystemExit, self.main_gui.start_gui)

    def test_main_gui_exit_button(self):
        global EVENTS
        EVENTS = list()
        self.main_gui = MainGui()
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN,
                                     {'pos': (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] - 75), 'button': 1}))
        self.assertRaises(SystemExit, self.main_gui.start_gui)

    def test_main_gui_quit_event(self):
        global EVENTS
        EVENTS = list()
        self.main_gui = MainGui()
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.QUIT, {}))
        self.assertRaises(SystemExit, self.main_gui.start_gui)

    def test_main_gui_draw_button(self):
        global EVENTS
        EVENTS = list()
        self.main_gui = MainGui()
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN,
                                     {'pos': (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] - 150), 'button': 1}))
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN,
                                     {'pos': (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] - 75), 'button': 1}))
        try:
            self.main_gui.start_gui()
        except SystemExit:
            self.assertEqual(self.main_gui.graph_drawing, True)
        else:
            self.fail("Draw Button test failed!")

    def test_main_gui_do_nothing(self):
        global EVENTS
        EVENTS = list()
        self.main_gui = MainGui()
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.KEYDOWN, {'key': pg.K_a, 'mod': 0}))
        EVENTS.append(pg.event.Event(pg.KEYDOWN, {'key': pg.K_ESCAPE, 'mod': 0}))
        try:
            self.main_gui.start_gui()
        except SystemExit:
            self.assertEqual(self.main_gui.intro, True)
        else:
            self.fail("Do nothing test failed!")

    def test_main_gui_menu_draw(self):
        global EVENTS
        EVENTS = [pg.event.Event(pg.QUIT, {})]
        pg.init()
        self.main_gui = MainGui()
        self.main_gui.init_screen()
        self.main_gui.menu.draw()
        self.assertEqual(self.main_gui.intro, True)


if __name__ == '__main__':
    unittest.main()
