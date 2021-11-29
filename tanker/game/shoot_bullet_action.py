from game.action import Action
from game import constants
from game.point import Point
from game.input_service import InputService
from game.bullet import Bullet

class ShootBulletAction(Action):
    def __init__(self) -> None:
        super().__init__()
        self._input_service = InputService()

    def execute(self, cast):
        shoot = self._input_service.is_space_pressed()
        bullets = []
        if shoot:
            tank = cast["tank"][0]
            bullet = Bullet()
            position_tank = tank.get_position()
            x_position_tank = position_tank.get_x()
            y_position_tank = position_tank.get_y()
            position = Point(x_position_tank + 32, y_position_tank)
            bullet.set_position(position)
            bullet.set_height(constants.BULLET_HEIGHT)
            bullet.set_width(constants.BULLET_WIDTH)
            bullet.set_velocity(Point(constants.BULLET_DX, 0))
            bullet.set_image(constants.IMAGE_BULLET)
            bullets.append(bullet)
            cast["bullets"] = bullets