import unittest

from unittest.mock import MagicMock
from gui_components.defines import *
from gui_components.DrawScreen import DrawScreen, TextBoxesIDs

EVENTS = []


def side_effect():
    return EVENTS


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.draw_screen = DrawScreen()

    def test_draw_screen_escape(self):
        global EVENTS
        EVENTS = list()
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.KEYDOWN, {'key': pg.K_ESCAPE, 'mod': 0}))
        self.assertRaises(SystemExit, self.draw_screen.run)

    def test_draw_screen_quit_event(self):
        global EVENTS
        EVENTS = list()
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.QUIT, {}))
        self.assertRaises(SystemExit, self.draw_screen.run)

    def test_draw_screen_exit_button(self):
        global EVENTS
        EVENTS = list()
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN, {'pos': (730, 570), 'button': 1}))
        self.assertRaises(SystemExit, self.draw_screen.run)

    def test_draw_screen_instructions_button(self):
        global EVENTS
        EVENTS = list()
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN, {'pos': (110, 570), 'button': 1}))
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN, {'pos': (730, 570), 'button': 1}))
        try:
            self.draw_screen.run()
        except SystemExit:
            self.assertEqual(self.draw_screen.instructions, True)
        else:
            self.fail("Draw Button test failed!")

    def test_draw_screen_set_err_msg(self):
        self.draw_screen.set_err_msg('error')
        self.assertEqual(self.draw_screen.err_msg, 'error')

    def test_draw_screen_draw_err_msg(self):
        self.draw_screen.set_err_msg('error')
        try:
            self.draw_screen.draw_err_msg()
        except Exception:
            self.fail('Draw error message failed!')

    def test_draw_screen_draw_buttons(self):
        try:
            self.draw_screen.init_buttons()
            self.draw_screen.draw_buttons()
        except Exception:
            self.fail('Draw Buttons failed!')

    def test_draw_screen_input_boxes(self):
        self.draw_screen.init_text_boxes()
        self.draw_screen.text_boxes[TextBoxesIDs.minimum_id_tb.value].text = '1'
        self.draw_screen.text_boxes[TextBoxesIDs.maximum_id_tb.value].text = '10'
        self.draw_screen.text_boxes[TextBoxesIDs.step_id_tb.value].text = '0.1'
        self.draw_screen.text_boxes[TextBoxesIDs.function_id_tb.value].text = 'sin(x)'
        my_input = {'min': 1.0, 'max': 10.0, 'step': 0.1, 'func': 'sin(x)'}
        result = self.draw_screen.get_input()
        self.assertDictEqual(result, my_input)

    def test_draw_screen_input_box_validate(self):
        self.draw_screen.init_text_boxes()
        self.draw_screen.text_boxes[TextBoxesIDs.minimum_id_tb.value].text = '1'
        self.draw_screen.text_boxes[TextBoxesIDs.maximum_id_tb.value].text = '10'
        self.draw_screen.text_boxes[TextBoxesIDs.step_id_tb.value].text = '0.1'
        self.draw_screen.text_boxes[TextBoxesIDs.function_id_tb.value].text = 'sin(x)'
        self.assertEqual(self.draw_screen.check_valid_input(), True)
        self.draw_screen.text_boxes[TextBoxesIDs.minimum_id_tb.value].text = 'fff'
        self.assertEqual(self.draw_screen.check_valid_input(), False)
        self.draw_screen.text_boxes[TextBoxesIDs.minimum_id_tb.value].text = '100'
        self.assertEqual(self.draw_screen.check_valid_input(), False)
        self.draw_screen.text_boxes[TextBoxesIDs.minimum_id_tb.value].text = '1'
        self.draw_screen.text_boxes[TextBoxesIDs.step_id_tb.value].text = '-0.1'
        self.assertEqual(self.draw_screen.check_valid_input(), False)
        self.draw_screen.text_boxes[TextBoxesIDs.step_id_tb.value].text = '0.1'
        self.draw_screen.text_boxes[TextBoxesIDs.function_id_tb.value].text = ' '
        self.assertEqual(self.draw_screen.check_valid_input(), False)

    def test_draw_screen_generate_graph_no_error(self):
        global EVENTS
        EVENTS = list()
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN, {'pos': (110, 270), 'button': 1}))
        try:
            self.draw_screen.run()
        except AttributeError:
            self.assertEqual(self.draw_screen.graph_drawing, True)
        else:
            self.fail("Generate Graph Button test failed!")

    def test_draw_screen_generate_graph_error(self):
        global EVENTS
        EVENTS = list()
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN, {'pos': (110, 270), 'button': 1}))
        try:
            self.draw_screen.error = True
            self.draw_screen.run()
        except AttributeError:
            self.assertEqual(self.draw_screen.graph_drawing, True)
        else:
            self.fail("Generate Graph Button test failed!")

    def test_draw_screen_go_to_instructions(self):
        global EVENTS
        EVENTS = list()
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.QUIT, {}))
        self.draw_screen.graph_drawing = False
        self.draw_screen.instructions = True
        self.assertRaises(SystemExit, self.draw_screen.run)

    def test_draw_screen_go_to_plot(self):
        global EVENTS
        EVENTS = list()
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN, {'pos': (10, 50), 'button': 1}))
        for key, value in {pg.K_x: 'x', pg.K_MINUS: '-', pg.K_7: '7'}.items():
            EVENTS.append(pg.event.Event(pg.KEYDOWN, {'key': key, 'unicode': value, 'mod': 0}))

        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN, {'pos': (140, 90), 'button': 1}))
        EVENTS.append(pg.event.Event(pg.KEYDOWN, {'key': pg.K_1, 'unicode': '1', 'mod': 0}))

        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN, {'pos': (140, 130), 'button': 1}))
        for key, value in {pg.K_1: '1', pg.K_0: '0'}.items():
            EVENTS.append(pg.event.Event(pg.KEYDOWN, {'key': key, 'unicode': value, 'mod': 0}))

        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN, {'pos': (140, 170), 'button': 1}))
        for key, value in {pg.K_0: '0', pg.K_PERIOD: '.', pg.K_1: '1'}.items():
            EVENTS.append(pg.event.Event(pg.KEYDOWN, {'key': key, 'unicode': value, 'mod': 0}))

        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN, {'pos': (110, 270), 'button': 1}))
        EVENTS.append(pg.event.Event(pg.QUIT, {}))
        self.assertRaises(SystemExit, self.draw_screen.run)


if __name__ == '__main__':
    unittest.main()
