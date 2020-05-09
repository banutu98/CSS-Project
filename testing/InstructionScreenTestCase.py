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
        # self.instruction_screen.run()

    def test_runScreen_escape(self) -> None:
        global EVENTS
        EVENTS = list()
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.KEYDOWN, {'key': pg.K_ESCAPE, 'mod': 0}))
        self.assertRaises(SystemExit, self.instruction_screen.run)

    def test_draw_screen_quit_event(self):
        global EVENTS
        EVENTS = list()
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.QUIT, {}))
        self.assertRaises(SystemExit, self.instruction_screen.run)

    def test_runScreen_draw_btn_exit(self) -> None:
        global EVENTS
        EVENTS = list()
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN, {'pos': (730, 570), 'button': 1}))
        EVENTS.append(pg.event.Event(pg.QUIT, {}))
        self.assertRaises(SystemExit, self.instruction_screen.run)

    def test_btn_down_somewhere_on_screen(self) -> None:
        global EVENTS
        EVENTS = list()
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN, {'pos': (1, 1), 'button': 1}))
        EVENTS.append(pg.event.Event(pg.QUIT, {}))
        # self.assertRaises(SystemExit, self.instruction_screen.run)

    def test_draw_buttons(self):
        try:
            self.instruction_screen.init_buttons()
            self.instruction_screen.init_texts()
            self.instruction_screen.draw_buttons()
            self.instruction_screen.update_texts_and_finish_loop()
        except Exception:
            self.fail('Draw Buttons failed!')

    def test_exit_button_click(self):
        global EVENTS
        EVENTS = list()
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN, {'pos': (729, 570), 'button': 1}))
        self.assertRaises(SystemExit, self.instruction_screen.run)

    def test_back_button_click(self):
        global EVENTS
        EVENTS = list()
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN, {'pos': (114, 572), 'button': 1}))
        self.instruction_screen.run()
        # self.assertRaises(SystemExit, self.instruction_screen.run)

    # def test_texts(self):
    #     global EVENTS
    #     pg.event.get = MagicMock(side_effect=side_effect)
    #     self.instruction_screen.run()
    #     EVENTS.append(pg.event.Event(pg.QUIT, {}))
