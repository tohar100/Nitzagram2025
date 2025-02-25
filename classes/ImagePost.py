from Post import Post
from constants import *
from helpers import *
import pygame
class ImagePost(Post):
    def __init__(self, username, location, description, image_src):
        super().__init__(username, location, description)
        img = pygame.image.load(image_src)
        img = pygame.transform.scale(img, POST_WIDTH, POST_HEIGHT)
        self.img = img
    def display_content(self):
        screen.blit(self.img, (POST_X_POS, POST_Y_POS))