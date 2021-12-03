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
from game.enemies import Enemies
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_off_screen_action import HandleOffScreenAction
from game.move_actors_action import MoveActorsAction
from game.shoot_bullet_action import ShootBulletAction

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    cast["walls"] = []
    walls = []
    for y in range(70, constants.MAX_Y - 50, 20):  
        x = constants.MAX_X/2
        position = Point(x, y)

        wall = Wall()
        wall.set_position(position)
        wall.set_height(constants.WALL_HEIGHT)
        wall.set_width(constants.WALL_WIDTH)
        wall.set_image(constants.IMAGE_WALL)
        walls.append(wall)

    for p in range(200, constants.MAX_Y-200, 20):
        q = 200
        position = Point(q, p)

        wall = Wall()
        wall.set_position(position)
        wall.set_height(constants.WALL_HEIGHT)
        wall.set_width(constants.WALL_WIDTH)
        wall.set_image(constants.IMAGE_WALL)
        walls.append(wall)

    for a in range(200, constants.MAX_Y-200, 20):
        b = 600
        position = Point(b, a)

        wall = Wall()
        wall.set_position(position)
        wall.set_height(constants.WALL_HEIGHT)
        wall.set_width(constants.WALL_WIDTH)
        wall.set_image(constants.IMAGE_WALL)
        walls.append(wall)

    cast["walls"] = walls

    cast["tank"] = []
    tank = Tank()
    tanks = []
    position = Point(constants.TANK_X, constants.TANK_Y)
    tank.set_position(position)
    tank.set_height(constants.TANK_HEIGHT)
    tank.set_width(constants.TANK_WIDTH)
    tank.set_image(constants.IMAGE_TANK)
    tanks.append(tank)
    cast["tank"] = tanks

    cast["bullets"] = []

    cast["enemies"] = []
    enemies = []
    for d in range(100, constants.MAX_Y - 100, 100):
        c = 700
        position = Point(c, d)
        enemy = Enemies()
        enemy.set_position(position)
        enemy.set_height(constants.ENEMY_HEIGHT)
        enemy.set_width(constants.ENEMY_WIDTH)
        enemy.set_velocity(Point(0, 0))#random.randint(-3, 0), random.randint(-3, 3)))
        enemy.set_image(constants.IMAGE_ENEMY_TANK)
        enemies.append(enemy)
    cast["enemies"] = enemies

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
    shoot_bullet_action = ShootBulletAction()


    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, shoot_bullet_action ,handle_off_screen_action, handle_collisions_action]
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
