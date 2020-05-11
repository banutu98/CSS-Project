import unittest
import os
import pygame as pg
from export.export import Export
from tkinter import *
from tkinter import filedialog
from unittest.mock import MagicMock

def side_effect_png(initialdir, title, defaultextension, filetypes):
    return "surface.png"

def side_effect_csv(initialdir, title, defaultextension, filetypes):
    return "values.csv"

def side_effect_null_path(initialdir, title, defaultextension, filetypes):
    return ""

class TestExport(unittest.TestCase):
    def test_surface_save_path(self):
        surface = pg.Surface((100, 100))
        Export.save_plot_as_image("surface.png", surface)
        self.assertEqual(os.path.exists("surface.png"), True)

    def test_values_save_path(self):
        x_values = [i for i in range(10)]
        y_values = [i for i in range(10)]

        Export.save_plot_as_text("values.txt", x_values, y_values)
        self.assertEqual(os.path.exists("values.txt"), True)

    def test_surface_save_missing_path(self):
        surface = pg.Surface((100, 100))
        self.assertRaises(FileNotFoundError, Export.save_plot_as_image, "", surface)

    def test_values_save_missing_path(self):
        x_values = [i for i in range(10)]
        y_values = [i for i in range(10)]

        self.assertRaises(FileNotFoundError, Export.save_plot_as_text, "", x_values, y_values)

    def test_image_export(self):
        filedialog.asksaveasfilename = MagicMock(side_effect=side_effect_png)
        surface = pg.Surface((100, 100))
        self.assertEqual(Export.export_image(surface), True)

    def test_values_export(self):
        filedialog.asksaveasfilename = MagicMock(side_effect=side_effect_csv)
        x_values = [i for i in range(10)]
        y_values = [i for i in range(10)]

        self.assertEqual(Export.export_txt(x_values, y_values), True)

    def test_image_export_missing_path(self):
        filedialog.asksaveasfilename = MagicMock(side_effect=side_effect_null_path)
        surface = pg.Surface((100, 100))
        self.assertEqual(Export.export_image(surface), False)

    def test_values_export_missing_path(self):
        filedialog.asksaveasfilename = MagicMock(side_effect=side_effect_null_path)
        x_values = [i for i in range(10)]
        y_values = [i for i in range(10)]

        self.assertEqual(Export.export_txt(x_values, y_values), False)


if __name__ == '__main__':
    unittest.main()