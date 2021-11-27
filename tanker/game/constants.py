import os

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 30

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_WALL = os.path.join(os.getcwd(), "./tanker/assets/brick-wall.png")
IMAGE_TANK = os.path.join(os.getcwd(), "./tanker/assets/tank.png")
IMAGE_BULLET = os.path.join(os.getcwd(), "./tanker/assets/bullet.png")

SOUND_START = os.path.join(os.getcwd(), "./tanker/assets/start.wav")
SOUND_BULLET = os.path.join(os.getcwd(), "./tanker/assets/bullet.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./tanker/assets/over.wav")

BULLET_X = MAX_X / 2
BULLET_Y = MAX_Y - 125

BULLET_DX = 8
BULLET_DY = BULLET_DX * -1

TANK_X = 25
TANK_Y = MAX_Y/2

WALL_WIDTH = 48
WALL_HEIGHT = 24

WALL_SPACE = 5

TANK_SPEED = 6

TANK_WIDTH = 96
TANK_HEIGHT = 24

BULLET_WIDTH = 5
BULLET_HEIGHT = 2