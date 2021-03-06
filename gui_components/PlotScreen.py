from gui_components.defines import *
from gui_components.utils import Button
from gui_components import parser
from math_functions.math_functions import integral
from export.export import Export


class PlotScreen:

    def __init__(self, inputs):
        assert isinstance(inputs, dict)
        assert all(k in inputs for k in ['min', 'max', 'step', 'func'])
        assert all(isinstance(inputs[k], float) for k in ['min', 'max', 'step'])
        assert isinstance(inputs['func'], str)

        pg.init()
        pg.display.set_caption(WINDOW_TITLE)

        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()
        self.buttons = []
        self.texts = []
        self.min_v = inputs['min']
        self.max_v = inputs['max']
        self.step = inputs['step']
        self.func = inputs['func']
        w, h = self.screen.get_width(), self.screen.get_height()
        self.plot_x = 210
        self.plot_y = 100
        self.plot_w = w // 2
        self.plot_h = h // 2
        # Post-codition
        assert self.plot_w >= 0 and self.plot_h >= 0
        self.plot_surface = pg.Surface((self.plot_w, self.plot_h))
        self.error = False

    def add_button(self, font_name, font_size, button_name, text_color, center_location):
        assert font_size >= 0
        assert isinstance(button_name, str)
        assert text_color in pg.color.THECOLORS.values()
        assert isinstance(center_location, tuple)
        assert len(center_location) == 2
        assert center_location[0] >= 0 and center_location[1] >= 0

        font = pg.font.Font(font_name, font_size)
        text_surface = font.render(button_name, True, text_color)
        text_location = text_surface.get_rect()
        text_location.center = center_location
        self.buttons.append(Button(button_name, text_surface, text_location, border_width=5))

    def init_buttons(self):
        self.add_button(FONT_NAME, 20, EXIT_BUTTON_NAME, pg.color.THECOLORS['black'], (730, 570))
        self.add_button(FONT_NAME, 20, BACK_BUTTON_NAME, pg.color.THECOLORS['black'], (110, 570))
        self.add_button(FONT_NAME, 20, EXPORT_TXT_BUTTON_NAME, pg.color.THECOLORS['black'], (110, 370))
        self.add_button(FONT_NAME, 20, EXPORT_PNG_BUTTON_NAME, pg.color.THECOLORS['black'], (110, 320))

    def init_texts(self):
        assert SCREEN_SIZE[0] >= 0 and SCREEN_SIZE[1] >= 0

        text_surface = pg.font.Font(FONT_NAME, 30).render('Plotting function f(x)', True, pg.color.THECOLORS['black'])
        text_rect = text_surface.get_rect()
        text_rect.center = (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 7)
        self.texts.append((text_surface, text_rect))

        # text_surface = pg.font.Font(FONT_NAME, 15).render('for x in [<min>, <max>]',
        #                                                   True, pg.color.THECOLORS['black'])
        # text_rect = text_surface.get_rect()
        # text_rect.topleft = (50, 120)
        # self.texts.append((text_surface, text_rect))

    def draw_buttons(self):
        for button in self.buttons:
            self.screen.blit(button.surface, button.rect)
            if button.border_width:
                button.draw_border(self.screen, pg.color.THECOLORS['black'])

    def get_points(self):
        xs = []
        ys = []

        assert self.max_v > self.min_v
        assert self.step >= 0

        minimum_input = self.min_v
        maximum_input = self.max_v
        steps_input = self.step
        function_input = self.func
        integral_inside = parser.get_integral_inside_expression(function_input)
        step = self.step

        if integral_inside != '':
            x = minimum_input
            integrated_func = parser.expr_to_lamda(integral_inside)
            assert callable(integrated_func)
            while x + step <= maximum_input:
                y = integral(integrated_func, minimum_input, x + step,
                             nr_rectangles=NR_RECTANGLES)
                xs.append(x)
                ys.append(y)
                x += step
        else:
            lambda_exp = parser.expr_to_lamda(function_input)
            assert callable(lambda_exp)
            x = minimum_input
            while x < maximum_input:
                y = lambda_exp(x)
                xs.append(x)
                ys.append(y)
                x += step
        return list(zip(xs, ys))

    def draw_axes(self, points):
        assert isinstance(points, list)
        # assert list not empty
        assert points

        self.plot_surface.fill((255, 255, 255))
        min_x, min_y = map(min, zip(*points))
        max_x, max_y = map(max, zip(*points))
        surface_w, surface_h = self.plot_surface.get_size()
        diff_x, diff_y = max_x - min_x, max_y - min_y
        if min_y < 0 < max_y:
            # draw x axis
            y_start = (abs(min_y) / diff_y) * surface_h
            # invert y axis
            y_start = surface_h - y_start
            pg.draw.line(self.plot_surface, pg.color.THECOLORS['black'],
                         (0, y_start),
                         (surface_w, y_start),
                         2)
        if min_x < 0 < max_x:
            # draw y axis
            x_start = (abs(min_x) / diff_x) * surface_w
            pg.draw.line(self.plot_surface, pg.color.THECOLORS['black'],
                         (x_start, 0),
                         (x_start, surface_h),
                         2)
        self.screen.blit(self.plot_surface, (self.plot_x, self.plot_y))

    def plot_function(self, points):
        assert isinstance(points, list)
        # assert list not empty
        assert points

        surface_x, surface_y = self.plot_surface.get_offset()
        surface_w, surface_h = self.plot_surface.get_size()
        min_x, min_y = map(min, zip(*points))
        max_x, max_y = map(max, zip(*points))
        diff_x, diff_y = max_x - min_x, max_y - min_y
        for i in range(len(points) - 1):
            # adjust points
            # first, scale to surface width and height
            x_start, y_start = points[i]
            x_start -= min_x
            y_start -= min_y
            adj_x_start = (x_start / diff_x) * surface_w
            adj_y_start = (y_start / diff_y) * surface_h
            x_end, y_end = points[i + 1]
            x_end -= min_x
            y_end -= min_y
            adj_x_end = (x_end / diff_x) * surface_w
            adj_y_end = (y_end / diff_y) * surface_h
            # invert y axis
            adj_y_start = surface_h - adj_y_start
            adj_y_end = surface_h - adj_y_end
            # draw line
            pg.draw.line(self.plot_surface, pg.color.THECOLORS['red'],
                         (adj_x_start, adj_y_start),
                         (adj_x_end, adj_y_end),
                         3)
        self.screen.blit(self.plot_surface, (self.plot_x, self.plot_y))

    def draw(self):
        self.screen.fill(pg.color.THECOLORS['aquamarine3'])
        points = self.get_points()
        assert points
        self.draw_axes(points)
        self.plot_function(points)
        for text in self.texts:
            self.screen.blit(text[0], text[1])
        self.draw_buttons()

    def zoom(self, button):
        assert button in [4, 5]
        assert self.max_v > self.min_v
        assert self.step >= 0

        # compute step based on current interval length
        diff = (self.max_v - self.min_v) / 2
        interval_step = ZOOM_PROPORTION * diff
        direction = 1 if button == 4 else -1
        if ((direction == 1 and 2 * diff < MIN_INTERVAL_LENGTH) or
                (direction == -1 and 2 * diff > MAX_INTERVAL_LENGTH)):
            direction = 0
        self.max_v -= interval_step * direction
        self.min_v += interval_step * direction
        self.step -= ZOOM_PROPORTION * self.step * direction

        assert self.max_v > self.min_v
        assert self.step >= 0.0

    def set_err_msg(self, err_msg):
        assert isinstance(err_msg, str)

        self.error = True
        self.err_msg = err_msg

    def draw_err_msg(self):
        assert SCREEN_SIZE[0] >= 0 and SCREEN_SIZE[1] >= 0
        assert (ERROR_SURFACE_SIZE[0] < SCREEN_SIZE[0] and
                ERROR_SURFACE_SIZE[1] < SCREEN_SIZE[1])

        error_surface = pg.Surface(ERROR_SURFACE_SIZE)
        error_surface.fill(pg.color.THECOLORS['darkslategray'])
        error_surface_position = (
            SCREEN_SIZE[0] // 2 - ERROR_SURFACE_SIZE[0] // 2, SCREEN_SIZE[1] // 2 - ERROR_SURFACE_SIZE[1] // 2)
        self.screen.blit(error_surface, error_surface_position)

        assert error_surface_position[0] > 0 and error_surface_position[1] > 0
        assert error_surface_position[0] + ERROR_SURFACE_SIZE[0] < SCREEN_SIZE[0]
        assert error_surface_position[1] + ERROR_SURFACE_SIZE[1] < SCREEN_SIZE[1]

        text_surface = pg.font.Font(FONT_NAME, 23).render(self.err_msg, True, pg.color.THECOLORS['white'])
        text_rect = text_surface.get_rect()
        text_rect.center = (
            error_surface_position[0] + ERROR_SURFACE_SIZE[0] // 2,
            error_surface_position[1] + ERROR_SURFACE_SIZE[1] // 6)
        self.screen.blit(text_surface, text_rect)

        font = pg.font.Font(FONT_NAME, 20)
        text_surface = font.render("OK", True, pg.color.THECOLORS['white'])
        text_location = text_surface.get_rect()
        text_location.center = (error_surface_position[0] + ERROR_SURFACE_SIZE[0] // 2,
                                error_surface_position[1] + int(ERROR_SURFACE_SIZE[1] * 80 / 100))

        self.ok_button = Button(OK_BUTTON_NAME, text_surface, text_location, border_width=5)
        self.ok_button.draw_border(self.screen, pg.color.THECOLORS['white'])
        text_location = text_surface.get_rect()
        text_location.center = (error_surface_position[0] + ERROR_SURFACE_SIZE[0] // 2,
                                error_surface_position[1] + int(ERROR_SURFACE_SIZE[1] * 80 / 100))

        self.ok_button = Button(OK_BUTTON_NAME, text_surface, text_location, border_width=5)
        self.ok_button.draw_border(self.screen, pg.color.THECOLORS['white'])
        self.screen.blit(self.ok_button.surface, self.ok_button.rect)

    def run(self):
        self.init_buttons()
        assert len(self.buttons) == 4
        self.init_texts()
        assert len(self.texts) == 1
        self.draw()
        while True:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        exit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if not self.error:
                        if event.button in [4, 5]:
                            # 4 and 5 are mousewheel up and down
                            self.zoom(event.button)
                            self.draw()
                        else:
                            for button in self.buttons:
                                if button.rect.collidepoint(mouse_pos):
                                    if button.name == EXIT_BUTTON_NAME:
                                        exit()
                                    elif button.name == BACK_BUTTON_NAME:
                                        return
                                    elif button.name == EXPORT_PNG_BUTTON_NAME:
                                        export_success = Export.export_image(self.plot_surface)
                                        if not export_success:
                                            self.set_err_msg("Please choose a valid file path!")
                                    elif button.name == EXPORT_TXT_BUTTON_NAME:
                                        points = self.get_points()
                                        x_list = [x[0] for x in points]
                                        y_list = [y[0] for y in points]

                                        export_success = Export.export_txt(x_list, y_list)
                                        if not export_success:
                                            self.set_err_msg("Please choose a valid file path!")
                    else:
                        if self.ok_button.rect.collidepoint(mouse_pos):
                            self.error = False
                            self.draw()

            if self.error:
                self.draw_err_msg()
            pg.display.update()
            self.clock.tick(30)
