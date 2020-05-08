from gui_components.defines import *
from gui_components.utils import Button, InputBox
from enum import Enum
from gui_components import parser
from gui_components.InstructionsScreen import InstructionsScreen
from gui_components.PlotScreen import PlotScreen


class TextBoxesIDs(Enum):
    function_id_tb = 0
    minimum_id_tb = 1
    maximum_id_tb = 2
    step_id_tb = 3


class DrawScreen:

    def __init__(self):
        pg.init()
        pg.display.set_caption(WINDOW_TITLE)

        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()
        self.buttons = []
        self.text_boxes = []
        self.texts = []

        self.error = False

    def add_button(self, font_name, font_size, button_name, text_color, center_location):
        font = pg.font.Font(font_name, font_size)
        text_surface = font.render(button_name, True, text_color)
        text_location = text_surface.get_rect()
        text_location.center = center_location
        self.buttons.append(Button(button_name, text_surface, text_location, border_width=5))

    def draw_graph(self, points):
        for i in range(len(points) - 1):
            pg.draw.line(self.screen, pg.color.THECOLORS['red'], points[i], points[i + 1])

    def init_buttons(self):
        self.add_button(FONT_NAME, 20, EXIT_BUTTON_NAME, pg.color.THECOLORS['black'], (730, 570))
        self.add_button(FONT_NAME, 20, INSTRUCTIONS_BUTTON_NAME, pg.color.THECOLORS['black'], (110, 570))
        self.add_button(FONT_NAME, 20, GENERATE_GRAPH_BUTTON_NAME, pg.color.THECOLORS['black'], (110, 270))

    def init_text_boxes(self):
        self.text_boxes.append(InputBox('Function', self.screen, 10, 50, 250, 32, max_string_length=70))
        self.text_boxes.append(InputBox('Minimum', self.screen, 140, 90, 100, 32, max_string_length=30))
        self.text_boxes.append(InputBox('Maximum', self.screen, 140, 130, 100, 32, max_string_length=30))
        self.text_boxes.append(InputBox('Step', self.screen, 140, 170, 100, 32, max_string_length=30))

    def init_texts(self):
        text_surface = pg.font.Font(FONT_NAME, 20).render('Function law: ', True, pg.color.THECOLORS['black'])
        text_rect = text_surface.get_rect()
        text_rect.topleft = (10, 10)
        self.texts.append((text_surface, text_rect))

        text_surface = pg.font.Font(FONT_NAME, 20).render('Minimum: ', True, pg.color.THECOLORS['black'])
        text_rect = text_surface.get_rect()
        text_rect.topleft = (10, 95)
        self.texts.append((text_surface, text_rect))

        text_surface = pg.font.Font(FONT_NAME, 20).render('Maximum: ', True, pg.color.THECOLORS['black'])
        text_rect = text_surface.get_rect()
        text_rect.topleft = (10, 135)
        self.texts.append((text_surface, text_rect))

        text_surface = pg.font.Font(FONT_NAME, 20).render('Step: ', True, pg.color.THECOLORS['black'])
        text_rect = text_surface.get_rect()
        text_rect.topleft = (10, 175)
        self.texts.append((text_surface, text_rect))

    def check_valid_input(self) -> bool:
        should_be_numbers_id = [TextBoxesIDs.minimum_id_tb, TextBoxesIDs.maximum_id_tb,
                                TextBoxesIDs.step_id_tb]
        for textbox_id in should_be_numbers_id:
            if not parser.check_expression_is_number(self.text_boxes[textbox_id.value].text):
                self.set_err_msg(textbox_id.name.replace('_id_tb', ' field') + ' is invalid!')
                return False
        function_input = self.text_boxes[TextBoxesIDs.function_id_tb.value].text
        minimum_value = float(self.text_boxes[TextBoxesIDs.minimum_id_tb.value].text)
        maximum_value = float(self.text_boxes[TextBoxesIDs.maximum_id_tb.value].text)
        step_value = float(self.text_boxes[TextBoxesIDs.step_id_tb.value].text)

        if minimum_value >= maximum_value:
            self.set_err_msg('Minimum should be lower than maximum!')
            return False

        if minimum_value + step_value < minimum_value:
            self.set_err_msg('Minimum should be bigger than maximum + step!')
            return False

        is_ok = parser.check_expression_validity(function_input)
        if not is_ok:
            self.set_err_msg('The mathematical expression is invalid!')
            return False
        return True

    def get_input(self):
        minimum_input = float(self.text_boxes[TextBoxesIDs.minimum_id_tb.value].text)
        maximum_input = float(self.text_boxes[TextBoxesIDs.maximum_id_tb.value].text)
        step_input = float(self.text_boxes[TextBoxesIDs.step_id_tb.value].text)
        function_input = self.text_boxes[TextBoxesIDs.function_id_tb.value].text
        return {
            'min': minimum_input,
            'max': maximum_input,
            'step': step_input,
            'func': function_input
        }

    def set_err_msg(self, err_msg):
        self.error = True
        self.err_msg = err_msg

    def draw_err_msg(self):
        error_surface = pg.Surface(ERROR_SURFACE_SIZE)
        error_surface.fill(pg.color.THECOLORS['darkslategray'])
        error_surface_position = (
        SCREEN_SIZE[0] // 2 - ERROR_SURFACE_SIZE[0] // 2, SCREEN_SIZE[1] // 2 - ERROR_SURFACE_SIZE[1] // 2)
        self.screen.blit(error_surface, error_surface_position)

        text_surface = pg.font.Font(FONT_NAME, 23).render(self.err_msg, True, pg.color.THECOLORS['white'])
        text_rect = text_surface.get_rect()
        text_rect.center = (
        error_surface_position[0] + ERROR_SURFACE_SIZE[0] // 2, error_surface_position[1] + ERROR_SURFACE_SIZE[1] // 6)
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

    def draw_buttons(self):
        for button in self.buttons:
            self.screen.blit(button.surface, button.rect)
            if button.border_width:
                button.draw_border(self.screen, pg.color.THECOLORS['black'])

    def run(self):
        self.init_buttons()
        self.init_texts()
        self.init_text_boxes()

        graph_drawing = True
        instructions = False
        plot_mode = False
        while True:
            while graph_drawing:
                self.screen.fill(pg.color.THECOLORS['aquamarine3'])

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
                            for button in self.buttons:
                                if button.rect.collidepoint(mouse_pos):
                                    if button.name == EXIT_BUTTON_NAME:
                                        exit()
                                    elif button.name == GENERATE_GRAPH_BUTTON_NAME:
                                        graph_drawing = False
                                        plot_mode = True
                                        if self.error:
                                            graph_drawing = False
                                            instructions = False
                                    elif button.name == INSTRUCTIONS_BUTTON_NAME:
                                        graph_drawing = False
                                        instructions = True
                        else:
                            if self.ok_button.rect.collidepoint(mouse_pos):
                                self.error = False

                        # print(mouse_pos)
                    if not self.error:
                        for text_box in self.text_boxes:
                            text_box.handle_event(event)
                for text in self.texts:
                    self.screen.blit(text[0], text[1])
                for text_box in self.text_boxes:
                    text_box.update()
                    text_box.draw()
                self.draw_buttons()

                if self.error:
                    self.draw_err_msg()

                # self.draw_graph([(10, 32), (50, 60), (78, 80)])

                pg.display.update()
                self.clock.tick(30)

            if instructions:
                InstructionsScreen().run()

            if plot_mode:
                if self.check_valid_input():
                    inputs = self.get_input()
                    PlotScreen(inputs).run()

            graph_drawing = True
            instructions = False
            plot_mode = False
