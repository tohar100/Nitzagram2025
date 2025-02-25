import pygame
from helpers import screen
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, LIGHT_GRAY
from classes.ImagePost import ImagePost
from classes.TextPost import TextPost
from classes.Comment import Comment
from classes.Button import Button

def main():
    # הגדר את תצוגת המשחק, השעון והכותרת
    pygame.init()

    # שנה את הכותרת של החלון
    pygame.display.set_caption('Nitzagram')
    clock = pygame.time.Clock()

    # הגדר תמונת רקע
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,(WINDOW_WIDTH, WINDOW_HEIGHT))

    # TODO: add a post here
    posts = [
        ImagePost("Noa Kirel", "Tel Aviv", "Hello from Noa", "Images/noa_kirel.jpg"),
        ImagePost("Ronaldo", "Madrid", "Hello from Ronaldo", "Images/ronaldo.jpg"),
        TextPost("Efrat", "Beer Sheva", "Hello from Efrat", "Coding is like magic—except the spells are written in Python.", BLACK, LIGHT_GRAY)
    ]
    post_display_index = 0
    running = True
    while running:
        # תופס אירועים כגון לחיצה על מקש, לחיצת עכבר וכדומה.
        # עוברים על כל האירועים שקרו בתקתק השעון האחרון
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        # הצג את הרקע, התמונה המוצגת, לייקים, הערות, תגים ומיקום (בתמונה)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        post_display_index[0]
        # תצוגת עדכון - ללא קלט עדכן הכל
        pygame.display.update()

        # הגדר את תקתוק השעון להיות 60 פעמים בשנייה. 60 פריימים לשנייה.
        clock.tick(60)
    pygame.quit()
    quit()


main()
