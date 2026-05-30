#!/usr/bin/env python
"""
SPACE INVADERS

Final game should support:
    - Start screen with title, instructions, and enemy score guide.
    - Player ship movement using LEFT and RIGHT arrow keys.
    - Player shooting using SPACE.
    - Single bullet before 1000 score, double bullets after 1000 score.
    - Enemy fleet movement left/right and downward.
    - Enemy bullets fired from bottom-most enemies.
    - Mystery ship movement and random bonus score.
    - Blocker shields that can be destroyed by bullets/enemies.
    - Score display, lives display, next-round screen, and game-over screen.

IMPORTANT:
    - This is a skeleton/template file. Most methods contain TODO comments and pass.
    - Read the comments carefully before writing code.
    - Implement incrementally:
        1. Load window/background/images.
        2. Draw start menu.
        3. Add player ship movement.
        4. Add bullets.
        5. Add enemies and enemy movement.
        6. Add collisions, scoring, lives, and game-over logic.
        7. Add sounds, mystery ship, explosions, blockers, and next round.
"""
import sys
from dataclasses import dataclass
from os.path import abspath, dirname, join

import pygame as pg

# -----------------------------------------------------------------------------
# PATHS AND CONSTANTS
# -----------------------------------------------------------------------------

BASE_PATH = abspath(dirname(__file__))
FONT_PATH = join(BASE_PATH, "fonts")
IMAGE_PATH = join(BASE_PATH, "images")
SOUND_PATH = join(BASE_PATH, "sounds")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

FONT_FILE = join(FONT_PATH, "space_invaders.ttf")
BACKGROUND_IMAGE = join(IMAGE_PATH, "background.jpg")

BLOCKERS_POSITION = 450
ENEMY_DEFAULT_POSITION = 65
ENEMY_MOVE_DOWN = 35

SHIP_START_POSITION = (375, 540)
SHIP_SPEED = 5
SHIP_LEFT_LIMIT = 10
SHIP_RIGHT_LIMIT = 740

ENEMY_COLUMNS = 10
ENEMY_ROWS = 5
ENEMY_START_X = 157
ENEMY_X_GAP = 50
ENEMY_Y_GAP = 45
ENEMY_WIDTH = 40
ENEMY_HEIGHT = 35

MYSTERY_START_POSITION = (-80, 45)
MYSTERY_SIZE = (75, 35)
MYSTERY_MOVE_DELAY = 25000

PLAYER_BULLET_SPEED = 15
ENEMY_BULLET_SPEED = 5
ENEMY_SHOOT_DELAY = 700
NEW_SHIP_DELAY = 900
NEXT_ROUND_DELAY = 3000

WHITE = (255, 255, 255)
GREEN = (78, 255, 87)
BLUE = (80, 255, 239)
PURPLE = (203, 0, 255)
RED = (237, 28, 36)

IMAGE_NAMES = [
    "ship",
    "mystery",
    "enemy1_1",
    "enemy1_2",
    "enemy2_1",
    "enemy2_2",
    "enemy3_1",
    "enemy3_2",
    "explosionblue",
    "explosiongreen",
    "explosionpurple",
    "laser",
    "enemylaser",
]

SOUND_NAMES = ["shoot", "shoot2", "invaderkilled", "mysterykilled", "shipexplosion"]


# -----------------------------------------------------------------------------
# ASSET CONTAINER AND ASSET LOADING FUNCTIONS
# -----------------------------------------------------------------------------

@dataclass
class Assets:
    """
    Stores all game assets in one object.

    TODO for students:
        - Use this object to pass images, sounds, music notes, and background
          to different game classes instead of using many global variables.
    """
    images: dict
    sounds: dict
    music_notes: list
    background: pg.Surface


def load_images() -> dict:
    """
    Load all image files from the images folder.

    TODO:
        - Create an empty dictionary.
        - Loop through IMAGE_NAMES.
        - For each name, load IMAGE_PATH/name.png using pg.image.load().
        - Use .convert_alpha() because these images may have transparency.
        - Store each image in the dictionary using its logical name.
        - Return the dictionary.

    Example key:
        images["ship"] should contain the ship image surface.
    """
    return {image_name: pg.image.load(f"{IMAGE_PATH}/{image_name}.png").convert_alpha() for image_name in IMAGE_NAMES}


def load_sounds() -> tuple[dict, list]:
    """
    Load sound effects and music notes.

    TODO:
        - Create a dictionary named sounds.
        - Loop through SOUND_NAMES.
        - Load each sound from SOUND_PATH/name.wav using pg.mixer.Sound().
        - Set volume to around 0.2.
        - Store it in the dictionary.
        - Load four music notes named 0.wav, 1.wav, 2.wav, 3.wav.
        - Set their volume to around 0.5.
        - Return (sounds, music_notes).
    """
    sounds = {}
    for sound_name in SOUND_NAMES:
        loaded_sound = pg.mixer.Sound(f"{SOUND_PATH}/{sound_name}.wav")
        loaded_sound.set_volume(0.2)
        sounds[sound_name] = loaded_sound

    dummy_notes = [num for num in range(4)]
    music_notes = []
    for music_note in dummy_notes:
        loaded_note = pg.mixer.Sound(f"{SOUND_PATH}/{music_note}.wav")
        loaded_note.set_volume(0.5)
        music_notes.append(loaded_note)

    return sounds, music_notes


def load_assets() -> Assets:
    """
    Load all assets needed by the game.

    TODO:
        - Call load_images().
        - Call load_sounds().
        - Load the background image from BACKGROUND_IMAGE.
        - Use .convert() for background because it has no transparency.
        - Return an Assets object.
    """
    images = load_images()
    sounds, music_notes = load_sounds()
    background = pg.image.load(BACKGROUND_IMAGE).convert()
    return Assets(images=images, sounds=sounds, music_notes=music_notes, background=background)

# -----------------------------------------------------------------------------
# BASIC TEXT HELPER
# -----------------------------------------------------------------------------

class Text:
    """
    Helper class for rendering and drawing text.
    """
    def __init__(self, text_font, size, message, color, xpos, ypos):
        """
        TODO:
            - Create a pg.font.Font object using text_font and size.
            - Render the message using the given color.
            - Store the rendered surface.
            - Create a rect with topleft position (xpos, ypos).
        """
        self.font = pg.font.Font(text_font, size)
        self.surface = self.font.render(message, True, color)
        self.rect = self.surface.get_rect(topleft=(xpos,ypos))

    def draw(self, surface):
        """
        TODO:
            - Draw/blit the text surface on the given surface using its rect.
        """
        surface.blit(self.surface, self.rect)


# -----------------------------------------------------------------------------
# SPRITE CLASSES
# -----------------------------------------------------------------------------

class Ship(pg.sprite.Sprite):
    """
    Player ship controlled by LEFT and RIGHT arrow keys.
    """
    def __init__(self, assets):
        """
        TODO:
            - Call the parent Sprite constructor.
            - Set image to assets.images["ship"].
            - Create rect at SHIP_START_POSITION.
            - Store movement speed as SHIP_SPEED.
        """
        super().__init__()
        self.image = assets.images["ship"]
        self.rect = self.image.get_rect(topleft=SHIP_START_POSITION)
        self.speed = SHIP_SPEED

    def update(self, screen, keys, current_time=None):
        """
        Move and draw the ship.
        TODO:
            - If LEFT key is pressed and ship is not beyond SHIP_LEFT_LIMIT,
              decrease rect.x by speed.
            - If RIGHT key is pressed and ship is not beyond SHIP_RIGHT_LIMIT,
              increase rect.x by speed.
            - Draw the ship image on the screen.
        """
        if keys[pg.K_LEFT] and self.rect.x > SHIP_LEFT_LIMIT:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT] and self.rect.x < SHIP_RIGHT_LIMIT:
            self.rect.x += self.speed

        screen.blit(self.image, self.rect)


class Bullet(pg.sprite.Sprite):
    """
    Bullet used by both player and enemies.
    """
    def __init__(self, assets, xpos, ypos, direction, speed, image_name, side):
        """
        TODO:
            - Call parent Sprite constructor.
            - Load image from assets.images[image_name].
            - Create rect at (xpos, ypos).
            - Store speed, direction, side, and image_name.

        Meaning:
            - direction = -1 means bullet moves upward.
            - direction = 1 means bullet moves downward.
            - side can be "center", "left", or "right".
        """
        super().__init__()
        self.image = assets.images[image_name]
        self.rect = self.image.get_rect(topleft=(xpos, ypos))
        self.direction = direction
        self.speed = speed
        self.side = side
        self.image_name = image_name

    def update(self, screen, keys=None, current_time=None):
        """
        Draw and move bullet.

        TODO:
            - Draw bullet image on screen.
            - Update rect.y by speed * direction.
            - If bullet goes above top boundary or below screen, kill it.
        """
        screen.blit(self.image, self.rect)
        self.rect.y += self.speed + self.direction
        if (self.rect.y < 15) or (self.rect.y > SCREEN_HEIGHT):
            self.kill()



class Enemy(pg.sprite.Sprite):
    """
    One enemy in the enemy grid.
    """

    def __init__(self, assets, row, column):
        """
        TODO:
            - Call parent constructor.
            - Store assets, row, and column.
            - Create image list using load_images().
            - Set animation index to 0.
            - Set current image and rect.
        """
        super().__init__()
        self.assets = assets
        self.row = row
        self.column = column
        self.images = []
        self.load_images()
        self.animation_index = 0
        self.current_image = self.images[self.animation_index]
        self.rect = self.current_image.get_rect()

    def load_images(self):
        """
        Load the two animation frames for this enemy based on its row.

        TODO:
            - Use the row number to decide which two enemy images to use.
            - Rows 0, 1/2, and 3/4 use different enemy image pairs.
            - Scale each image to (ENEMY_WIDTH, ENEMY_HEIGHT).
            - Store both frames in self.images.
        """
        image_names = []
        if self.row == 0:
            image_names = ["enemy1_2", "enemy1_1"]
        elif self.row in (1,2):
            image_names = ["enemy2_2", "enemy2_1"]
        else:
            image_names = ["enemy3_2", "enemy3_1"]

        self.images = [pg.transform.scale(self.assets.images[name], (ENEMY_WIDTH, ENEMY_HEIGHT)) for name in image_names]

    def toggle_image(self):
        """
        Switch between the two enemy animation frames.

        TODO:
            - Increase index by 1.
            - If index reaches length of images, reset to 0.
            - Update self.image.
        """
        self.animation_index += 1
        if self.animation_index >= len(self.images):
            self.animation_index = 0
        self.current_image = self.images[self.animation_index]

    def update(self, screen, *args):
        """
        TODO:
            - Draw enemy image on screen.
        """
        screen.blit(self.images, self.rect)


class EnemiesGroup(pg.sprite.Group):
    """
    Custom sprite group that controls all enemies together.
    """

    def __init__(self, columns, rows, start_y):
        """
        TODO:
            - Call parent Group constructor.
            - Create a 2D list to track enemies by row and column.
            - Store columns and rows.
            - Initialize movement variables:
                * moveTime, direction, rightMoves, leftMoves, moveNumber.
            - Store timer using pg.time.get_ticks().
            - Compute bottom position of the enemy grid.
            - Track alive columns so enemies can shoot from valid columns.
        """
        super().__init__()
        self.columns = columns
        self.rows = rows
        self.enemy_list = [[None] * columns for _ in range(rows)]
        self.moveTime = 600
        self.direction = 1
        self.rightMoves = 30
        self.leftMoves = 30
        self.moveNumber = 15
        self.timer = pg.time.get_ticks()
        self.bottom = start_y + ((rows - 1)*ENEMY_Y_GAP) + ENEMY_HEIGHT
        self.alive_columns = list(range(columns))
        self.left_alive_columns = 0
        self.right_alive_columns = columns - 1

    def update(self, screen, current_time):
        """
        Move the enemy group.

        TODO:
            - Only move when current_time - timer > moveTime.
            - If moving right, use positive velocity.
            - If moving left, use negative velocity.
            - After enough moves in one direction:
                * Change direction.
                * Move all enemies down by ENEMY_MOVE_DOWN.
                * Update bottom position.
            - Toggle each enemy image whenever it moves.
        """
        if current_time - self.timer <= self.moveTime:
            return


    def add_internal(self, *sprites):
        """
        TODO:
            - Call parent add_internal().
            - For each enemy, store it in self.enemies[row][column].
        """
        pass

    def remove_internal(self, *sprites):
        """
        TODO:
            - Call parent remove_internal().
            - For each removed enemy, update the 2D list.
            - Update speed after enemies are killed.
        """
        pass

    def is_column_dead(self, column):
        """
        TODO:
            - Return True if no enemy is alive in the given column.
            - Otherwise return False.
        """
        pass

    def random_bottom(self):
        """
        Select a random bottom-most enemy from an alive column.

        TODO:
            - Randomly choose a column from alive columns.
            - Starting from bottom row, search upward.
            - Return the first non-None enemy found.
        """
        pass

    def update_speed(self):
        """
        TODO:
            - If only one enemy remains, make enemy movement fastest.
            - If 10 or fewer enemies remain, make movement faster than normal.
        """
        pass

    def kill_enemy_in_grid(self, enemy):
        """
        Update grid and alive-column information after an enemy dies.

        TODO:
            - Set self.enemies[enemy.row][enemy.column] to None.
            - If the whole column is dead, remove it from alive columns.
            - If leftmost/rightmost alive column changes, adjust movement limits
              so the remaining enemy group can still travel across the screen.
        """
        pass


class Blocker(pg.sprite.Sprite):
    """
    One small square block of the shield/barrier.
    """

    def __init__(self, size, color, row, column):
        """
        TODO:
            - Create a square Surface of the given size.
            - Fill it with color.
            - Create rect.
            - Store row and column.
        """
        pass

    def update(self, screen, *args):
        """
        TODO:
            - Draw blocker square on screen.
        """
        pass


class Mystery(pg.sprite.Sprite):
    """
    Bonus mystery ship moving across the top of the screen.
    """

    def __init__(self, assets):
        """
        TODO:
            - Load and scale mystery image.
            - Start it outside the left side of the screen.
            - Set row = 5 because score calculation uses row 5 for mystery.
            - Set movement delay, direction, timer, sound, and playSound flag.
        """
        pass

    def update(self, screen, keys=None, current_time=None):
        """
        Move and draw mystery ship after a delay.

        TODO:
            - Check how much time has passed from self.timer.
            - After MYSTERY_MOVE_DELAY, move mystery ship horizontally.
            - Play sound when it enters.
            - Fade out sound while moving.
            - When it exits screen, reverse direction and reset timer.
        """
        pass


class EnemyExplosion(pg.sprite.Sprite):
    """
    Short explosion animation after an enemy is destroyed.
    """

    def __init__(self, assets, enemy, *groups):
        """
        TODO:
            - Call parent constructor with groups.
            - Select explosion image based on enemy row.
            - Create two scaled versions for simple animation.
            - Position explosion at enemy position.
            - Store timer.
        """
        pass

    @staticmethod
    def get_image(assets, row):
        """
        TODO:
            - Return purple explosion for top row.
            - Return blue explosion for middle rows.
            - Return green explosion for lower rows.
        """
        pass

    def update(self, screen, current_time, *args):
        """
        TODO:
            - For first 100 ms draw small explosion.
            - For next 100 ms draw bigger explosion.
            - After around 400 ms, kill this sprite.
        """
        pass


class MysteryExplosion(pg.sprite.Sprite):
    """
    Displays mystery ship bonus score briefly.
    """

    def __init__(self, mystery, score, *groups):
        """
        TODO:
            - Create a Text object showing score.
            - Position it near mystery ship.
            - Store timer.
        """
        pass

    def update(self, screen, current_time, *args):
        """
        TODO:
            - Blink the score text for a short time.
            - Kill the sprite after the display duration is over.
        """
        pass


class ShipExplosion(pg.sprite.Sprite):
    """
    Short blinking animation after player is hit.
    """

    def __init__(self, assets, ship, *groups):
        """
        TODO:
            - Store ship image and position.
            - Store timer.
        """
        pass

    def update(self, screen, current_time, *args):
        """
        TODO:
            - Blink ship image for a short time.
            - Kill explosion sprite when animation is complete.
        """
        pass


class Life(pg.sprite.Sprite):
    """
    Small ship icon shown in the lives area.
    """

    def __init__(self, assets, xpos, ypos):
        """
        TODO:
            - Load ship image.
            - Scale it to small icon size.
            - Create rect at (xpos, ypos).
        """
        pass

    def update(self, screen, *args):
        """
        TODO:
            - Draw life icon on screen.
        """
        pass


# -----------------------------------------------------------------------------
# MAIN GAME CLASS
# -----------------------------------------------------------------------------

class SpaceInvaders:
    """
    Main class that controls the full Space Invaders game.

    Responsibilities:
        - Initialize pygame, screen, clock, and assets.
        - Manage game states: main screen, active game, next round, and game over.
        - Create and reset sprites.
        - Handle input.
        - Update movement, bullets, collisions, scoring, lives, and drawing.
    """

    def __init__(self):
        """
        Initialize game-level objects and text.

        TODO:
            - Pre-initialize pygame mixer.
            - Call pg.init().
            - Create clock.
            - Set window caption.
            - Create the screen.
            - Load assets using load_assets().
            - Set initial game-state flags:
                * start_game = False
                * main_screen = True
                * game_over = False
            - Set enemy starting position to ENEMY_DEFAULT_POSITION.
            - Create title, instruction, game-over, next-round, score, lives,
              and enemy-score-guide Text objects.
            - Create three Life icons and livesGroup.
        """
        pg.mixer.pre_init(44100, -16, 1, 4096)
        pg.init()
        self.clock = pg.time.Clock()
        pg.display.set_caption("Space Invaders Game!")
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.assets = load_assets()
        self.start_game = False
        self.main_screen = True
        self.game_over = False
        self.enemy_default_position = ENEMY_DEFAULT_POSITION
        self._create_static_text()
        self.all_blockers = []
        self.life_1 = Life(self.assets, 715, 3)
        self.life_2 = Life(self.assets, 742, 3)
        self.life_3 = Life(self.assets, 769, 3)
        self.lives_group = pg.sprite.Group(self.life_1, self.life_2, self.life_3)


    # ------------------------------------------------------------------
    # RESET AND CREATION HELPERS
    # ------------------------------------------------------------------

    def _create_static_text(self):
        self.title_text = Text(FONT_FILE, 50, "SPACE INVADER GAME", WHITE, 200,300)
        self.instruction_text = Text(FONT_FILE, 35, "PRESS ANY KEY TO CONTINUE", WHITE, 200,400)


    def reset(self, score):
        """
        Reset active game objects for a new game or new round.

        TODO:
            - Create player ship and playerGroup.
            - Create explosionsGroup.
            - Create player bullets group.
            - Create mystery ship and mysteryGroup.
            - Create enemy bullets group.
            - Create enemies using make_enemies().
            - Create allSprites group.
            - Store current key state.
            - Reset timers.
            - Store score.
            - Set makeNewShip = False.
            - Set shipAlive = True.
        """
        pass

    def make_blockers(self, number):
        """
        Create one shield made of many small Blocker squares.

        TODO:
            - Create a sprite group.
            - Use nested loops for rows and columns.
            - Create a Blocker of size 10.
            - Position it based on number, row, and column.
            - Add it to the group.
            - Return the group.
        """
        pass

    def make_enemies(self):
        """
        Create the full enemy grid.

        TODO:
            - Create EnemiesGroup with ENEMY_COLUMNS and ENEMY_ROWS.
            - Loop through rows and columns.
            - Create Enemy objects.
            - Set each enemy's x and y position.
            - Add each enemy to the group.
            - Store group in self.enemies.
        """
        pass

    # ------------------------------------------------------------------
    # SOUND AND MUSIC
    # ------------------------------------------------------------------

    def play_main_music(self, current_time):
        """
        Play repeating alien movement notes.

        TODO:
            - If current_time - noteTimer is greater than enemy moveTime:
                * Select current music note.
                * Advance note index from 0 to 3 repeatedly.
                * Play the note.
                * Update noteTimer.
        """
        pass

    # ------------------------------------------------------------------
    # INPUT HANDLING
    # ------------------------------------------------------------------

    @staticmethod
    def should_exit(evt):
        """
        Return True if the game should close.

        TODO:
            - Return True for QUIT event.
            - Return True for KEYUP event with ESCAPE key.
            - Otherwise return False.
        """
        pass

    def check_input(self):
        """
        Process keyboard and quit events during active gameplay.

        TODO:
            - Read current keys using pg.key.get_pressed().
            - Loop through pg.event.get().
            - If should_exit(event), quit the program.
            - If KEYDOWN and key is SPACE:
                * If no player bullet exists and ship is alive:
                    - If score < 1000, create one center bullet.
                    - Else create left and right bullets.
                    - Add bullets to bullet group and allSprites.
                    - Play correct shooting sound.
        """
        pass

    # ------------------------------------------------------------------
    # ENEMY SHOOTING AND SCORING
    # ------------------------------------------------------------------

    def make_enemies_shoot(self):
        """
        Let enemies fire bullets from a random bottom enemy.

        TODO:
            - If enough time passed since last enemy shot and enemies exist:
                * Select a random bottom enemy.
                * Create an enemy bullet moving downward.
                * Add it to enemyBullets and allSprites.
                * Reset timer.
        """
        pass

    def calculate_score(self, row):
        """
        Calculate score based on enemy row and add it to total score.

        TODO:
            - Rows 3 and 4 give 10 points.
            - Rows 1 and 2 give 20 points.
            - Row 0 gives 30 points.
            - Row 5, mystery ship, gives random score from [50, 100, 150, 300].
            - Add score to self.score.
            - Return score earned.
        """
        pass

    # ------------------------------------------------------------------
    # MENU DRAWING
    # ------------------------------------------------------------------

    def create_main_menu(self):
        """
        Draw enemy images beside their score values on the start screen.

        TODO:
            - Load enemy and mystery images from assets.
            - Scale them to the same sizes as the original game.
            - Blit them at fixed menu positions.
        """
        pass

    # ------------------------------------------------------------------
    # COLLISION LOGIC
    # ------------------------------------------------------------------

    def check_collisions(self):
        """
        Handle all game collisions.

        TODO:
            1. Player bullets vs enemy bullets:
                - Destroy both bullets.
            2. Player bullets vs enemies:
                - Kill enemy and bullet.
                - Play invader killed sound.
                - Add score.
                - Create EnemyExplosion.
                - Store gameTimer for next-round delay.
            3. Player bullets vs mystery ship:
                - Stop mystery sound.
                - Play mystery killed sound.
                - Add random mystery score.
                - Create MysteryExplosion.
                - Create a new Mystery ship and add it to groups.
            4. Enemy bullets vs player:
                - Remove one life icon.
                - If no lives remain, set game_over and stop active game.
                - Play ship explosion sound.
                - Create ShipExplosion.
                - Mark that a new ship should be created after delay.
            5. Enemies reaching player/bottom:
                - If enemy group reaches player area or screen bottom, game over.
            6. Bullets vs blockers:
                - Destroy bullets and blocker pieces.
            7. Enemies vs blockers:
                - Destroy blocker pieces when enemies reach them.
        """
        pass

    def create_new_ship(self, create_ship, current_time):
        """
        Create a new player ship after player is hit.

        TODO:
            - If create_ship is True and enough time passed since shipTimer:
                * Create new Ship.
                * Add it to allSprites and playerGroup.
                * Set makeNewShip = False.
                * Set shipAlive = True.
        """
        pass

    # ------------------------------------------------------------------
    # SCREEN STATE DRAWING
    # ------------------------------------------------------------------

    def create_game_over(self, current_time):
        """
        Draw blinking Game Over screen and eventually return to main menu.

        TODO:
            - Draw background.
            - Use current_time - timer to blink the Game Over text.
            - After around 3000 ms, set main_screen = True.
            - Still process quit/ESC events while on this screen.
        """
        pass

    def draw_main_screen(self):
        """
        Draw the start menu screen.

        TODO:
            - Draw background.
            - Draw title and instruction text.
            - Draw enemy score guide text.
            - Call create_main_menu() to draw enemy icons.
            - Process events:
                * Quit/ESC should exit.
                * Any KEYUP should start a new game:
                    - Create blockers.
                    - Reset lives.
                    - Call reset(0).
                    - Set start_game = True and main_screen = False.
        """
        self.screen.blit(self.assets.background, (0,0))
        self.title_text.draw(self.screen)
        self.instruction_text.draw(self.screen)
        self.create_main_menu()
        while True:
            for event in pg.event.get():
                if self.should_exit(event):
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYUP:
                    self.all_blockers = pg.sprite.Group(self.make_blockers(0), self.make_blockers(1), self.make_blockers(2), self.make_blockers(3))
                    self.lives_group.add(self.life_1, self.life_2, self.life_3)
                    self.reset(0)
                    self.start_game = True
                    self.main_screen = False
        # self.screen.display.update()

    def draw_next_round_screen(self, current_time):
        """
        Draw the Next Round message after all enemies are defeated.

        TODO:
            - For NEXT_ROUND_DELAY duration:
                * Draw background.
                * Draw score.
                * Draw Next Round text.
                * Draw lives.
                * Still allow input/quit handling.
            - After delay:
                * Move enemy starting position down by ENEMY_MOVE_DOWN.
                * Call reset(self.score).
        """
        pass

    def draw_active_game(self, current_time):
        """
        Draw and update one frame of active gameplay.

        TODO:
            - Play main music.
            - Draw background.
            - Draw blockers.
            - Draw score and lives text.
            - Handle input.
            - Update enemies.
            - Update allSprites.
            - Update explosions.
            - Check collisions.
            - Possibly create a new ship.
            - Make enemies shoot.
        """
        pass

    # ------------------------------------------------------------------
    # MAIN LOOP
    # ------------------------------------------------------------------

    def main(self):
        """
        Main game loop.

        TODO:
            - Run while True.
            - If main_screen is True, call draw_main_screen().
            - Else if start_game is True:
                * If all enemies are gone and explosions are finished,
                  handle next-round screen.
                * Else draw active game.
            - Else if game_over is True:
                * Reset enemy starting position.
                * Draw game-over screen.
            - Update display.
            - Limit FPS using self.clock.tick(FPS).
        """
        while True:
            if self.main_screen:
                self.draw_main_screen()
            elif self.start_game:
                self.draw_active_game()
            elif self.game_over:
                self.create_game_over()


# -----------------------------------------------------------------------------
# ENTRY POINT
# -----------------------------------------------------------------------------

def main():
    """
    Entry point for the game.

    TODO for students:
        - After completing the template, uncomment the lines below.
        - Run the file and test step by step.

    Suggested testing order:
        1. Confirm pygame window opens.
        2. Confirm images and background load.
        3. Confirm main menu appears.
        4. Confirm player ship draws and moves.
        5. Confirm bullets fire.
        6. Confirm enemies appear and move.
        7. Confirm collisions, scoring, lives, and game-over logic.
    """

    game = SpaceInvaders()
    game.main()
    pass


if __name__ == "__main__":
    main()
