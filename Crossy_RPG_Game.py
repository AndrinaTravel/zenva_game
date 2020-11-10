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
pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)


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

        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width, height))

    # Main game loop, used to update all gameplay
    def run_game_loop(self, level_speed):
        is_game_over = False
        did_win = False
        direction = 0

        player_character = PlayerCharacter('player.png', 375, 700, 50, 50)
        enemy_0 = NonPlayerCharacter('enemy.png', 20, 600, 50, 50)
        enemy_0.SPEED += level_speed

        enemy_1 = NonPlayerCharacter('enemy.png', self.width - 40, 400, 50, 50)
        enemy_0.SPEED += level_speed

        enemy_2 = NonPlayerCharacter('enemy.png', 20, 200, 50, 50)
        enemy_0.SPEED += level_speed

        treasure = GameObject('treasure.png', 375, 50, 50, 50)

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
            self.game_screen.blit(self.image, (0, 0))

            # Draw the treasure
            treasure.draw(self.game_screen)
            # Update the player position
            player_character.move(direction, self.height)
            # Draw the player at the new position
            player_character.draw(self.game_screen)

            # Move and draw the enemy character
            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)

            if level_speed > 2:
                enemy_1.move(self.width)
                enemy_1.draw(self.game_screen)
            if level_speed > 4:
                enemy_2.move(self.width)
                enemy_2.draw(self.game_screen)

            # End game if collision between enemy or treasure
            if player_character.detect_collision(enemy_0):
                is_game_over = True
                did_win = False
                text = font.render('You Lose!', True, BLACK_COLOR)
                self.game_screen.blit(text, (300, 350))
                pygame.display.update()
                clock.tick(1)
                break

            elif player_character.detect_collision(treasure):
                is_game_over = True
                did_win = True
                text = font.render('You Win!', True, BLACK_COLOR)
                self.game_screen.blit(text, (275, 350))
                pygame.display.update()
                clock.tick(1)
                break


            # Update all game graphics
            pygame.display.update()
            # Tick the clock to update everything within the game
            clock.tick(self.TICK_RATE)

        if did_win:
            self.run_game_loop(level_speed + 0.5)
        else:
            return

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
    SPEED = 5

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # Move function will move the character up if direction > 0 and down if < 0
    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED
        # Make sure the character never goes past the bottom of the screen
        if self.y_pos >= max_height - 40:
            self.y_pos = max_height - 40

    # Return False (no collision) if y positions and x positions do not overlap
    # Return True x and y positions overlap
    def detect_collision(self, other_body):
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False

        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.x_pos:
            return False

        return True


# Class to represent the enemy character
class NonPlayerCharacter(GameObject):

    # How many tiles the enemy moves per second
    SPEED = 5

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # Move function will move the enemy
    def move(self, max_width):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 40:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED


pygame.init()

new_game = Game('background.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop(1)

# Quit pygame and the program
pygame.quit()
quit()

