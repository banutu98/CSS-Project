import unittest

from unittest.mock import MagicMock
from gui_components.defines import *
from gui_components.DrawScreen import DrawScreen

EVENTS = []


def side_effect():
    return EVENTS


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.draw_screen = DrawScreen()

    def test_draw_screen_escape(self):
        global EVENTS
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.KEYDOWN, {'key': pg.K_ESCAPE, 'mod': 0}))
        self.assertRaises(SystemExit, self.draw_screen.run)

    def test_draw_screen_quit_event(self):
        global EVENTS
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.QUIT, {}))
        self.assertRaises(SystemExit, self.draw_screen.run)

    def test_draw_screen_exit_button(self):
        global EVENTS
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN, {'pos': (730, 570), 'button': 1}))
        self.assertRaises(SystemExit, self.draw_screen.run)

    def test_draw_screen_instructions_button(self):
        global EVENTS
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN, {'pos': (110, 570), 'button': 1}))
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN, {'pos': (730, 570), 'button': 1}))
        try:
            self.draw_screen.run()
        except SystemExit:
            self.assertEqual(self.draw_screen.instructions, True)
        else:
            self.fail("Draw Button test failed!")


if __name__ == '__main__':
    unittest.main()
