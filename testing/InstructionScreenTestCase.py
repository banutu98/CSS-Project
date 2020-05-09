import unittest
from gui_components.defines import *
from gui_components.InstructionsScreen import InstructionsScreen
from unittest.mock import MagicMock

EVENTS = []


def side_effect():
    return EVENTS


class InstructionScreenCase(unittest.TestCase):
    def setUp(self) -> None:
        self.instruction_screen = InstructionsScreen()
        self.instruction_screen.run()

    def test_runScreen(self) -> None:
        global EVENTS
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.KEYDOWN, {'key': pg.K_ESCAPE, 'mod': 0}))
        self.assertRaises(SystemExit, self.draw_screen.run)
