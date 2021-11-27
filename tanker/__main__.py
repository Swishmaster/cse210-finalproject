import random
import os
os.environ['RAYLIB_BIN_PATH'] = '.'
from raylibpy import RAYLIB_BIN_PATH
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService
from game.wall import Wall
from game.bullet import Bullet
from game.tank import Tank
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_off_screen_action import HandleOffScreenAction
from game.move_actors_action import MoveActorsAction

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    cast["walls"] = []
    walls = []
    for y in range(50, constants.MAX_Y - 50):  
        x = constants.MAX_X/2
        position = Point(x, y)

        wall = Wall()
        wall.set_position(position)
        wall.set_height(constants.BRICK_HEIGHT)
        wall.set_width(constants.BRICK_WIDTH)
        wall.set_image(constants.IMAGE_BRICK)
        walls.append(wall)

    for p in range(200, constants.MAX_Y-200):
        q = 200
        position = Point(q, p)

        wall = Wall()
        wall.set_position(position)
        wall.set_height(constants.BRICK_HEIGHT)
        wall.set_width(constants.BRICK_WIDTH)
        wall.set_image(constants.IMAGE_BRICK)
        walls.append(wall)

    for a in range(200, constants.MAX_Y-200):
        b = 600
        position = Point(b, a)

        wall = Wall()
        wall.set_position(position)
        wall.set_height(constants.BRICK_HEIGHT)
        wall.set_width(constants.BRICK_WIDTH)
        wall.set_image(constants.IMAGE_BRICK)
        walls.append(wall)

    cast["walls"] = walls

    cast["tank"] = []
    tank = Tank()
    tanks = []
    position = Point(constants.PADDLE_X, constants.PADDLE_Y)
    tank.set_position(position)
    tank.set_height(constants.PADDLE_HEIGHT)
    tank.set_width(constants.PADDLE_WIDTH)
    tank.set_image(constants.IMAGE_PADDLE)
    tanks.append(tank)
    cast["tank"] = tanks

    cast["bullets"] = []

    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    handle_off_screen_action = HandleOffScreenAction()
    control_actors_action = ControlActorsAction(input_service)
    handle_collisions_action = HandleCollisionsAction(physics_service)

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_off_screen_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # Start the game
    output_service.open_window("Tanker")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
