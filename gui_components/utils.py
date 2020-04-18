import pygame.locals as pl

from gui_components.defines import *


class Button:

    def __init__(self, name, surface, rect, border_width=None):
        self.name = name
        self.surface = surface
        self.rect = rect
        self.border_width = border_width

    def draw_border(self, surface, color):
        distancing = self.border_width + self.border_width // 2
        # top line
        pg.draw.rect(surface, color, [self.rect.left - distancing, self.rect.top - distancing,
                                      self.rect.width + distancing * 2, self.border_width])
        # bottom line
        pg.draw.rect(surface, color, [self.rect.left - distancing, self.rect.bottom,
                                      self.rect.width + distancing * 2, self.border_width])
        # left line
        pg.draw.rect(surface, color, [self.rect.left - distancing, self.rect.top - distancing,
                                      self.border_width, self.rect.height + distancing])
        # right line
        pg.draw.rect(surface, color, [self.rect.right + self.border_width / 2, self.rect.top - distancing / 2,
                                      self.border_width, self.rect.height + distancing])


class InputBox:

    def __init__(self, screen, x, y, w, h, text='', text_color=pg.color.THECOLORS['black'],
                 font_size=20, max_string_length=-1):
        self.screen = screen
        self.rect = pg.Rect(x, y, w, h)
        self.color = TEXTBOX_INACTIVE_COLOR
        self.text = text
        self.text_color = text_color
        self.font_size = font_size
        self.font = pg.font.Font(TEXTBOX_FONT_NAME, self.font_size)
        self.text_surface = self.font.render(text, True, pg.color.THECOLORS['black'])
        self.max_string_length = max_string_length
        self.active = False

        self.cursor_surface = pg.Surface((int(self.font_size / 20 + 1), self.font_size))
        self.cursor_surface.fill(pg.color.THECOLORS['black'])
        self.cursor_position = len(self.text)  # Inside text

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(*event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = TEXTBOX_ACTIVE_COLOR if self.active else TEXTBOX_INACTIVE_COLOR
        if self.active:
            if event.type == pg.KEYDOWN:
                if event.key == pl.K_BACKSPACE:
                    self.text = self.text[:max(self.cursor_position - 1, 0)] + self.text[self.cursor_position:]

                    # Subtract one from cursor_pos, but do not go below zero:
                    self.cursor_position = max(self.cursor_position - 1, 0)
                elif event.key == pl.K_DELETE:
                    self.text = self.text[:self.cursor_position] + self.text[self.cursor_position + 1:]
                elif event.key == pl.K_RETURN:
                    return True
                elif event.key == pl.K_RIGHT:
                    # Add one to cursor_pos, but do not exceed len(input_string)
                    self.cursor_position = min(self.cursor_position + 1, len(self.text))
                elif event.key == pl.K_LEFT:
                    # Subtract one from cursor_pos, but do not go below zero:
                    self.cursor_position = max(self.cursor_position - 1, 0)
                elif event.key == pl.K_END:
                    self.cursor_position = len(self.text)
                elif event.key == pl.K_HOME:
                    self.cursor_position = 0
                elif len(self.text) < self.max_string_length or self.max_string_length == -1:
                    # If no special key is pressed, add unicode of key to input_string
                    self.text = self.text[:self.cursor_position] + event.unicode + self.text[self.cursor_position:]
                    self.cursor_position += len(event.unicode)  # Some are empty, e.g. K_UP

            self.text_surface = self.font.render(self.text, True, self.text_color)
            cursor_y_pos = self.font.size(self.text[:self.cursor_position])[0]
            # Without this, the cursor is invisible when self.cursor_position > 0:
            if self.cursor_position > 0:
                cursor_y_pos -= self.cursor_surface.get_width()
            self.text_surface.blit(self.cursor_surface, (cursor_y_pos, 0))
            return False

    def update(self):
        # Resize the box if the text is too long.
        self.rect.w = max(self.rect.w, self.text_surface.get_width() + 10)

    def draw(self):
        # Blit the text.
        self.screen.blit(self.text_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pg.draw.rect(self.screen, self.color, self.rect, 2)

    def get_surface(self):
        return self.text_surface

    def get_text(self):
        return self.text

    def get_cursor_position(self):
        return self.cursor_position

    def set_text_color(self, color):
        self.text_color = color

    def set_cursor_color(self, color):
        self.cursor_surface.fill(color)

    def clear_text(self):
        self.text = ""
        self.cursor_position = 0
