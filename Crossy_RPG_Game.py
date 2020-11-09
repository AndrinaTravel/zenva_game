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

    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # Create a window of specified size to display the game in
        self.game_screen = pygame.display.set_mode((width, height))
        # Set screen color to white
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

    # Main game loop, used to update all gameplay
    def run_game_loop(self):
        is_game_over = False
        direction = 0

        player_character = PlayerCharacter('player.png', 375, 700, 50, 50)

        while not is_game_over:
            # A loop to get all of the events occurring at any given time
            for event in pygame.event.get():
                # If we press exit then exit out of the game
                if event.type == pygame.QUIT:
                    is_game_over = True
                # Detect when pressed key down
                elif event.type == pygame.KEYDOWN:
                    # Move up if the up key pressed
                    if event.key == pygame.K_UP:
                        direction = 1
                    # Move down if the down key is pressed
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                # Detect when key is released
                elif event.type == pygame.KEYUP:
                    # Stop movement when key no longer pressed
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                print(event)

            # Redraw the screen to be a blank white window
            self.game_screen.fill(WHITE_COLOR)
            # Update the player position
            player_character.move(direction)
            # Draw the player at the new position
            player_character.draw(self.game_screen)


            # Update all game graphics
            pygame.display.update()
            # Tick the clock to update everything within the game
            clock.tick(self.TICK_RATE)


# Generic Game Object class to be subclassed by other objects in the game
class GameObject:

    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        # Scale the image up
        self.image = pygame.transform.scale(object_image, (width, height))

        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

    # Draw the object by blit it onto the background(game screen)
    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))


# Class to represent the character controlled by the player
class PlayerCharacter(GameObject):

    # How many tiles the character moves per second
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # Move function will move the character up if direction > 0 and down if < 0
    def move(self, direction):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED


pygame.init()

new_game = Game('background.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
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