import unittest

from unittest.mock import MagicMock
from gui_components.defines import *
import main_gui

EVENTS = []


def side_effect():
    return EVENTS


class MainGuiTestCase(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_main_gui_escape(self):
        global EVENTS
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.KEYDOWN, {'key': pg.K_ESCAPE, 'mod': 0}))
        self.assertRaises(SystemExit, main_gui.start_gui)

    def test_main_gui_exit_button(self):
        global EVENTS
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN,
                                     {'pos': (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] - 75), 'button': 1}))
        self.assertRaises(SystemExit, main_gui.start_gui)

    def test_main_gui_quit_event(self):
        global EVENTS
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.QUIT, {}))
        self.assertRaises(SystemExit, main_gui.start_gui)

    def test_main_gui_draw_button(self):
        global EVENTS
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN,
                                     {'pos': (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] - 150), 'button': 1}))
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN,
                                     {'pos': (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] - 75), 'button': 1}))
        try:
            main_gui.start_gui()
        except SystemExit:
            self.assertEquals(main_gui.graph_drawing, True)
        else:
            self.fail("Draw Button test failed!")


if __name__ == '__main__':
    unittest.main()
