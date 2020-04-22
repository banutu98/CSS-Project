import pygame as pg

class Export:
    @staticmethod
    def save_plot_as_image(path, surface):
        pg.image.save(surface, path)

    @staticmethod
    def save_plot_as_text(path, x_values, y_values):
        coords_file = open(path, "w")
        coords_file.write("X, Y")

        for i in range(len(x_values)):
            coords_file.write("{}, {}".format(x_values[i], y_values[i]))

        coords_file.close()


if __name__ == "__main__":
    pass