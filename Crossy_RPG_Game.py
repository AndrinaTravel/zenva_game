# Pygame development

# Gain access to pygame library
import pygame

# Screen size
SCREEN_TITLE = 'Crossy RPG'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
# Colors according to RGB codes
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
# Clock used to update game events and FPS
clock = pygame.time.Clock()


class Game:

    # 60 FPS rate
    TICK_RATE = 60
    # is_game_over = False

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # Create a window of specified size to display the game in
        self.game_screen = pygame.display.set_mode((height, width))
        # Set screen color to white
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

    # Main game loop, used to update all gameplay
    def run_game_loop(self):
        is_game_over = False
        while not is_game_over:
            # A loop to get all of the events occurring at any given time
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True

                print(event)

            # Update all game graphics
            pygame.display.update()
            # Tick the clock to update everything within the game
            clock.tick(self.TICK_RATE)


pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

# Quit pygame and the program
pygame.quit()
quit()

# Load the player image from the file directory
# player_image = pygame.image.load('player.png')
# Scale the image up
# player_image = pygame.transform.scale(player_image, (50, 50))

# Draw a rectangle on top of the game screen canvas(x,y,width,height)
            # pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
            # Draw a circle on top of the game screen(x,y,radius)
            # pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)

            # Draw the player image on top of the screen at (x ,y) position
            # game_screen.blit(player_image, (375, 375))