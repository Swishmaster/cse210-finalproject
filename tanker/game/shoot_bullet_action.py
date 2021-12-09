import raylibpy
from game.action import Action
from game import constants
from game.point import Point
from game.input_service import InputService
from game.bullet import Bullet
from game.audio_service import AudioService
import random

class ShootBulletAction(Action):
    def __init__(self) -> None:
        super().__init__()
        self._input_service = InputService()
        self._audio_service = AudioService()

    def execute(self, cast):
        shoot = self._input_service.is_space_pressed()
        tanks = cast["tank"]
        for tank in tanks:
            position_tank = tank.get_position()
            x_position_tank = position_tank.get_x()
            y_position_tank = position_tank.get_y()
            position = Point(x_position_tank + 65, y_position_tank + 27) #x position was 63
            if shoot:
                bullet1 = Bullet()
                bullet1.set_position(position)
                bullet1.set_height(constants.BULLET_HEIGHT)
                bullet1.set_width(constants.BULLET_WIDTH)
                bullet1.set_velocity(Point(constants.BULLET_DX, 0))
                bullet1.set_image(constants.IMAGE_BULLET)
                cast["bullets"].append(bullet1)
                # self._audio_service.play_sound(constants.SOUND_BULLET)

        enemies = cast["enemy"]
        for enemy in enemies:
            enemy_shoot = 15
            if random.randint(0, 15) == enemy_shoot:
                position_enemy = enemy.get_position()
                x_position_enemy = position_enemy.get_x()
                y_position_enemy = position_enemy.get_y()
                position1 = Point(x_position_enemy - 28, y_position_enemy + 27)
                bullet = Bullet()
                bullet.set_position(position1)
                bullet.set_height(constants.BULLET_HEIGHT)
                bullet.set_width(constants.BULLET_WIDTH)
                bullet.set_velocity(Point(-constants.BULLET_DX, 0))
                bullet.set_image(constants.IMAGE_BULLET)
                cast["enemy_bullets"].append(bullet)