import unittest
import pygame as pg
import pickle as pkl

from unittest.mock import MagicMock
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
        with open('main_events.json', 'rb') as f:
            events = pkl.load(f)
        for event in events:
            EVENTS.append(pg.event.Event(event[0], event[1]))
        EVENTS.append(pg.event.Event(pg.KEYDOWN, {'key': pg.K_ESCAPE, 'mod': 0}))
        self.assertRaises(SystemExit, main_gui.start_gui)


if __name__ == '__main__':
    unittest.main()
