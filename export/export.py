import pygame as pg
from tkinter import *
from tkinter import filedialog


class Export:
    @staticmethod
    def save_plot_as_image(path, surface):
        pg.image.save(surface, path)

    @staticmethod
    def save_plot_as_text(path, x_values, y_values):
        coords_file = open(path, "w")
        coords_file.write("X,Y\n")

        for i in range(len(x_values)):
            coords_file.write("{},{}\n".format(x_values[i], y_values[i]))

        coords_file.close()

    @staticmethod
    def export_image(surface):
        root = Tk()
        root.withdraw()
        root.filename = filedialog.asksaveasfilename(initialdir="/", title="Select file", defaultextension="*.*",
                                                     filetypes=(("JPEG", ".jpg"), ("PNG", "*.png")))

        if root.filename:
            Export.save_plot_as_image(root.filename, surface)
            return True
        print(root.filename)
        return False

    @staticmethod
    def export_txt(x_values, y_values):
        root = Tk()
        root.withdraw()
        root.filename = filedialog.asksaveasfilename(initialdir="/", title="Select file", defaultextension="*.*",
                                                     filetypes=(("CSV", ".csv"),))

        if root.filename:
            Export.save_plot_as_text(root.filename, x_values, y_values)
            return True

        return False


if __name__ == "__main__":
    pass
