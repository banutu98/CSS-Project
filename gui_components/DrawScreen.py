from gui_components.defines import *
from gui_components.utils import Button, InputBox
from enum import Enum
from gui_components import parser
from gui_components.InstructionsScreen import InstructionsScreen


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
        self.add_button(FONT_NAME, 20, EXPORT_TXT_BUTTON_NAME, pg.color.THECOLORS['black'], (110, 370))
        self.add_button(FONT_NAME, 20, EXPORT_PNG_BUTTON_NAME, pg.color.THECOLORS['black'], (110, 320))
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
        should_be_numbers_id = [TextBoxesIDs.maximum_id_tb, TextBoxesIDs.minimum_id_tb,
                                TextBoxesIDs.step_id_tb]
        for textbox_id in should_be_numbers_id:
            if not parser.check_expression_is_number(self.text_boxes[textbox_id.value].text):
                self.draw_err_msg(textbox_id.name.replace('_id_tb', ' field') + ' is invalid!')
                return False
        function_input = self.text_boxes[TextBoxesIDs.function_id_tb.value].text
        minimum_input = self.text_boxes[TextBoxesIDs.minimum_id_tb.value].text
        minimum_value = float(minimum_input)

        is_ok, value = parser.check_expression_validity(function_input, minimum_value)
        if not is_ok:
            self.draw_err_msg('The mathematical expression is invalid!')
            return False
        print('ok: {}'.format(value))
        return True

    def start_drawing_graph(self):
        if not self.check_valid_input():
            return
        # we should draw from here
        # self.draw_graph([(272, 13), (766, 537)])

        pass

    def draw_err_msg(self, err_msg):
        print(err_msg)

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
                        for button in self.buttons:
                            if button.rect.collidepoint(mouse_pos):
                                if button.name == EXIT_BUTTON_NAME:
                                    exit()
                                elif button.name == GENERATE_GRAPH_BUTTON_NAME:
                                    self.start_drawing_graph()
                                elif button.name == EXPORT_TXT_BUTTON_NAME:
                                    print('Export txt!')
                                elif button.name == EXPORT_PNG_BUTTON_NAME:
                                    print('Export png!')
                                elif button.name == INSTRUCTIONS_BUTTON_NAME:
                                    graph_drawing = False
                                    instructions = True
                        # print(mouse_pos)
                    for text_box in self.text_boxes:
                        text_box.handle_event(event)
                for text in self.texts:
                    self.screen.blit(text[0], text[1])
                for text_box in self.text_boxes:
                    text_box.update()
                    text_box.draw()
                self.draw_buttons()
                # self.draw_graph([(10, 32), (50, 60), (78, 80)])

                pg.display.update()
                self.clock.tick(30)
            if instructions:
                InstructionsScreen().run()
            graph_drawing = True
            instructions = False
