import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
import sys
import math
import enum
from gui_components.PlotScreen import PlotScreen
from gui_components.defines import *
from gui_components import parser
from math_functions.math_functions import integral
from tkinter import *
from tkinter import filedialog

EVENTS = []


def side_effect():
    return EVENTS


def side_effect_png(initialdir, title, defaultextension, filetypes):
    return "surface.png"


def side_effect_txt(initialdir, title, defaultextension, filetypes):
    return "values.csv"


def side_effect_null_path(initialdir, title, defaultextension, filetypes):
    return ""


def allclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return all([math.isclose(ai, bi)
                for ai, bi in zip(a, b)])


class Buttons(enum.IntEnum):
    EXIT_BUTTON = 0
    BACK_BUTTON = 1
    EXPORT_TXT_BUTTON = 2
    EXPORT_PNG_BUTTON = 3


class PlotScreenTestCase(unittest.TestCase):

    def setUp(self):
        self.test_inputs = {
            'min': 0,
            'max': 1,
            'step': 0.01,
            'func': 'x'
        }
        self.plot_screen = PlotScreen(self.test_inputs)
        self.plot_screen.init_buttons()
        self.plot_screen.init_texts()

    def test_plot_screen_escape(self):
        global EVENTS
        EVENTS = []
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.KEYDOWN,
                                     {'key': pg.K_ESCAPE, 'mod': 0}))
        self.assertRaises(SystemExit, self.plot_screen.run)

    def test_plot_screen_quit_event(self):
        global EVENTS
        EVENTS = []
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.QUIT, {}))
        self.assertRaises(SystemExit, self.plot_screen.run)

    def test_plot_screen_exit_button(self):
        global EVENTS
        EVENTS = []
        pg.event.get = MagicMock(side_effect=side_effect)
        exit_button = self.plot_screen.buttons[Buttons.EXIT_BUTTON]
        x, y, _, _ = exit_button.rect
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN,
                                     {'pos': (x, y), 'button': 1}))
        self.assertRaises(SystemExit, self.plot_screen.run)

    def test_plot_screen_back_button(self):
        global EVENTS
        EVENTS = []
        pg.event.get = MagicMock(side_effect=side_effect)
        back_button = self.plot_screen.buttons[Buttons.BACK_BUTTON]
        x, y, _, _ = back_button.rect
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN,
                                     {'pos': (x, y), 'button': 1}))
        self.assertIsNone(self.plot_screen.run())

    def test_plot_screen_zoom_in(self):
        old_max_v = self.plot_screen.max_v
        old_min_v = self.plot_screen.min_v
        old_step = self.plot_screen.step
        self.plot_screen.zoom(4)
        new_max_v = self.plot_screen.max_v
        new_min_v = self.plot_screen.min_v
        new_step = self.plot_screen.step
        zoomed = (new_max_v < old_max_v and
                  new_min_v > old_min_v and
                  new_step < old_step)
        self.assertTrue(zoomed)

    def test_plot_screen_zoom_out(self):
        old_max_v = self.plot_screen.max_v
        old_min_v = self.plot_screen.min_v
        old_step = self.plot_screen.step
        self.plot_screen.zoom(5)
        new_max_v = self.plot_screen.max_v
        new_min_v = self.plot_screen.min_v
        new_step = self.plot_screen.step
        zoomed = (new_max_v > old_max_v and
                  new_min_v < old_min_v and
                  new_step > old_step)
        self.assertTrue(zoomed)

    @patch('gui_components.PlotScreen.PlotScreen.zoom')
    def test_plot_screen_scroll_zoom_in(self, mock):
        global EVENTS
        EVENTS = []
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN,
                                     {'pos': (0, 0), 'button': 4}))
        EVENTS.append(pg.event.Event(pg.QUIT, {}))
        try:
            self.plot_screen.run()
        except SystemExit:
            self.assertTrue(mock.called)

    @patch('gui_components.PlotScreen.PlotScreen.zoom')
    def test_plot_screen_scroll_zoom_in(self, mock):
        global EVENTS
        EVENTS = []
        pg.event.get = MagicMock(side_effect=side_effect)
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN,
                                     {'pos': (0, 0), 'button': 5}))
        EVENTS.append(pg.event.Event(pg.QUIT, {}))
        try:
            self.plot_screen.run()
        except SystemExit:
            self.assertTrue(mock.called)

    def test_plot_screen_set_err_msg(self):
        self.plot_screen.set_err_msg('error')
        self.assertEqual(self.plot_screen.err_msg, 'error')

    def test_plot_screen_draw_err_msg(self):
        self.plot_screen.set_err_msg('error')
        try:
            self.plot_screen.draw_err_msg()
        except Exception:
            self.fail('Draw error message failed!')

    def test_squared(self):
        inputs = {
            'min': -1,
            'max': 1,
            'step': 0.01,
            'func': 'x**2'
        }
        plot_window = PlotScreen(inputs)
        points = plot_window.get_points()
        x, y_test = list(zip(*points))
        y_true = list(map(lambda x: x ** 2, x))
        self.assertTrue(allclose(y_true, y_test))

    def test_log(self):
        inputs = {
            'min': 0,
            'max': 3.1415,
            'step': 0.01,
            'func': 'sin(x)'
        }
        plot_window = PlotScreen(inputs)
        points = plot_window.get_points()
        x, y_test = list(zip(*points))
        y_true = list(map(math.sin, x))
        self.assertTrue(allclose(y_true, y_test))

    def test_integral(self):
        inputs = {
            'min': -1,
            'max': 1,
            'step': 0.01,
            'func': 'integrala(x)'
        }
        plot_window = PlotScreen(inputs)
        points = plot_window.get_points()
        x, y_test = list(zip(*points))
        # recompute integral
        integral_inside = parser.get_integral_inside_expression(inputs['func'])
        integrated_func = parser.expr_to_lamda(integral_inside)
        y_true = []
        start = inputs['min']
        step = inputs['step']
        for x_current in x[1:]:
            y = integral(integrated_func, start, x_current,
                         nr_rectangles=NR_RECTANGLES)
            y_true.append(y)
        self.assertTrue(allclose(y_true, y_test))

    def test_export_image_button(self):
        global EVENTS
        EVENTS = []
        pg.event.get = MagicMock(side_effect=side_effect)
        filedialog.asksaveasfilename = MagicMock(side_effect=side_effect_png)
        inputs = {
            'min': -1,
            'max': 1,
            'step': 0.01,
            'func': 'sin(x)'
        }
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN,
                                     {'pos': (140, 319), 'button': 1}))
        EVENTS.append(pg.event.Event(pg.QUIT, {}))

        plot_screen = PlotScreen(inputs)
        try:
            plot_screen.run()
        except SystemExit:
            self.assertTrue(os.path.exists("surface.png"))

    def test_export_txt_button(self):
        global EVENTS
        EVENTS = []
        pg.event.get = MagicMock(side_effect=side_effect)
        filedialog.asksaveasfilename = MagicMock(side_effect=side_effect_txt)
        inputs = {
            'min': -1,
            'max': 1,
            'step': 0.01,
            'func': 'sin(x)'
        }
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN,
                                     {'pos': (131, 372), 'button': 1}))
        EVENTS.append(pg.event.Event(pg.QUIT, {}))

        plot_screen = PlotScreen(inputs)
        try:
            plot_screen.run()
        except SystemExit:
            self.assertTrue(os.path.exists("values.csv"))

    def test_export_image_path_warning(self):
        global EVENTS
        EVENTS = []
        pg.event.get = MagicMock(side_effect=side_effect)
        filedialog.asksaveasfilename = MagicMock(side_effect=side_effect_null_path)
        inputs = {
            'min': -1,
            'max': 1,
            'step': 0.01,
            'func': 'sin(x)'
        }
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN,
                                     {'pos': (140, 319), 'button': 1}))
        EVENTS.append(pg.event.Event(pg.QUIT, {}))

        plot_screen = PlotScreen(inputs)
        try:
            plot_screen.run()
        except SystemExit:
            self.assertTrue(plot_screen.error)

    def test_export_txt_path_warning(self):
        global EVENTS
        EVENTS = []
        pg.event.get = MagicMock(side_effect=side_effect)
        filedialog.asksaveasfilename = MagicMock(side_effect=side_effect_null_path)
        inputs = {
            'min': -1,
            'max': 1,
            'step': 0.01,
            'func': 'sin(x)'
        }
        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN,
                                     {'pos': (131, 372), 'button': 1}))
        EVENTS.append(pg.event.Event(pg.QUIT, {}))

        plot_screen = PlotScreen(inputs)
        try:
            plot_screen.run()
        except SystemExit:
            self.assertTrue(plot_screen.error)

    def test_export_path_warning_dissapear(self):
        global EVENTS
        EVENTS = []
        pg.event.get = MagicMock(side_effect=side_effect)
        filedialog.asksaveasfilename = MagicMock(side_effect=side_effect_null_path)
        inputs = {
            'min': -1,
            'max': 1,
            'step': 0.01,
            'func': 'sin(x)'
        }

        EVENTS.append(pg.event.Event(pg.MOUSEBUTTONDOWN,
                                     {'pos': (403, 332), 'button': 1}))
        EVENTS.append(pg.event.Event(pg.QUIT, {}))

        plot_screen = PlotScreen(inputs)
        plot_screen.set_err_msg("Error")
        plot_screen.draw_err_msg()
        try:
            plot_screen.run()
        except SystemExit:
            self.assertFalse(plot_screen.error)


if __name__ == '__main__':
    unittest.main()
