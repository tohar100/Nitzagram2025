from Post import Post
from constants import *
from helpers import *
import pygame
class TextPost(Post):
    def __init__(self, username, location, description, text, text_color, background_color):
        super().__init__(username, location, description)
        self.text = from_text_to_array(text)
        self.text_color = text_color
        self.background_color = background_color
    def display_content(self):
        square = pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT)
        pygame.draw.rect(screen, self.background_color, square)
        for i in range(len(self.text)):
            font = pygame.font.SysFont('chalkduster.ttf', TEXT_POST_FONT_SIZE)
            text = font.render(self.text[i], True, self.text_color)
            text_pos = center_text(len(self.text), text, i)
            screen.blit(text, text_pos)
