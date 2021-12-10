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
from game.move_enemies_action import MoveEnemiesAction
from game.lives import Lives
from game.loser_winner import LoserWinner
from time import sleep

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    cast["walls"] = []
    walls = []
    for y in range(0, constants.MAX_Y, 20):  
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
    cast["enemy_bullets"] = []

    cast["enemy"] = []
    enemies = []
    c = 700
    position = Point(c, constants.TANK_Y)
    enemy = Enemies()
    enemy.set_position(position)
    enemy.set_height(constants.ENEMY_HEIGHT)
    enemy.set_width(constants.ENEMY_WIDTH) 
    enemy.set_image(constants.IMAGE_ENEMY_TANK)
    enemy.set_velocity(Point(0,0))
    enemies.append(enemy)
    cast["enemy"] = enemies

    cast["tank_lives"] = []
    x_value = 10
    for e in range(0, constants.TANK_LIVES):
        life = Lives()
        position = Point(x_value, 10)
        life.set_position(position)
        life.set_velocity((Point(0,0)))
        life.set_height(constants.LIVES_HEIGHT)
        life.set_width(constants.LIVES_WIDTH)
        life.set_image(constants.IMAGE_HEART)
        cast["tank_lives"].append(life)
        x_value = x_value + 25
    
    cast["enemy_lives"] = []
    enemy_x_value = 750
    for f in range(0, constants.ENEMY_LIVES):
        life = Lives()
        position = Point(enemy_x_value, 10)
        life.set_position(position)
        life.set_velocity((Point(0,0)))
        life.set_height(constants.LIVES_HEIGHT)
        life.set_width(constants.LIVES_WIDTH)
        life.set_image(constants.IMAGE_HEART)
        cast["enemy_lives"].append(life)
        enemy_x_value = enemy_x_value - 25

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
    move_enemies_action = MoveEnemiesAction()

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, shoot_bullet_action, move_enemies_action, handle_off_screen_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # Start the game
    output_service.open_window("Tanker")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game(cast)
    sleep(3)
    audio_service.stop_audio()

if __name__ == "__main__":
    main()
