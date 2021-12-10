import os
import random

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 30

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_WALL = os.path.join(os.getcwd(), "./tanker/assets/brick-wall.png")
IMAGE_TANK = os.path.join(os.getcwd(), "./tanker/assets/tank.png")
IMAGE_BULLET = os.path.join(os.getcwd(), "./tanker/assets/bullet.png")
IMAGE_ENEMY_TANK = os.path.join(os.getcwd(), "./tanker/assets/enemy_tank.png")
IMAGE_HEART = os.path.join(os.getcwd(), "./tanker/assets/heart.png")
IMAGE_WINNER = os.path.join(os.getcwd(), "./tanker/assets/winner.png")
IMAGE_LOSER = os.path.join(os.getcwd(), "./tanker/assets/loser.png")

SOUND_START = os.path.join(os.getcwd(), "./tanker/assets/start.wav")
SOUND_BULLET = os.path.join(os.getcwd(), "./tanker/assets/bullet.wav")
SOUND_LOSER = os.path.join(os.getcwd(), "./tanker/assets/game_over.wav") 
SOUND_WINNER = os.path.join(os.getcwd(), "./tanker/assets/cheers.wav")
SOUND_HIT = os.path.join(os.getcwd(), "./tanker/assets/im_hit.wav")
SOUND_YEAH = os.path.join(os.getcwd(), "./tanker/assets/yeah.wav")

BULLET_DX = 10

TANK_X = 25
TANK_Y = MAX_Y/2
MAX_TANK_X = 745
MAX_TANK_Y = 545

WALL_WIDTH = 48
WALL_HEIGHT = 24

WALL_SPACE = 5

TANK_SPEED = 6
TANK_LIVES = 3

TANK_WIDTH = 64
TANK_HEIGHT = 64

BULLET_WIDTH = 25
BULLET_HEIGHT = 10

ENEMY_SPEED = 3
ENEMY_HEIGHT = 64
ENEMY_WIDTH = 64
ENEMY_LIVES = 10

LIVES_WIDTH = 25
LIVES_HEIGHT = 25