import os
import pygame as pg
from tkinter import *
from tkinter import filedialog



class Export:
    @staticmethod
    def save_plot_as_image(path, surface):
        assert isinstance(path, str)
        assert isinstance(surface, pg.Surface)

        pg.image.save(surface, path)

    @staticmethod
    def save_plot_as_text(path, x_values, y_values):
        assert isinstance(path, str)
        assert isinstance(x_values, list)
        assert isinstance(y_values, list)
        assert len(x_values) != 0
        assert len(y_values) != 0

        coords_file = open(path, "w")
        coords_file.write("X,Y\n")

        for i in range(len(x_values)):
            coords_file.write("{},{}\n".format(x_values[i], y_values[i]))

        coords_file.close()

    @staticmethod
    def export_image(surface):
        assert isinstance(surface, pg.Surface)

        root = Tk()
        root.withdraw()
        root.filename = filedialog.asksaveasfilename(initialdir="/", title="Select file", defaultextension="*.*",
                                                     filetypes=(("JPEG", ".jpg"), ("PNG", "*.png")))

        assert isinstance(root.filename, str)
        if root.filename:
            Export.save_plot_as_image(root.filename, surface)
            assert os.path.exists(root.filename)
            return True
        return False

    @staticmethod
    def export_txt(x_values, y_values):
        root = Tk()
        root.withdraw()
        root.filename = filedialog.asksaveasfilename(initialdir="/", title="Select file", defaultextension="*.*",
                                                     filetypes=(("CSV", ".csv"),))

        assert isinstance(root.filename, str)
        if root.filename:
            Export.save_plot_as_text(root.filename, x_values, y_values)
            assert os.path.exists(root.filename)
            return True

        return False


if __name__ == "__main__":
    pass
