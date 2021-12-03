from game import constants
from game.action import Action
from game.point import Point
from game.audio_service import AudioService

class HandleCollisionsAction(Action):
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        tank = cast["tank"][0]
        walls = cast["walls"]
        bullets = cast["bullets"]
        enemies = cast["enemies"]
        position = tank.get_position()
        velocity = tank.get_velocity()
        x = position.get_x()
        y = position.get_y()
        dx = velocity.get_x()
        dy = velocity.get_y()

        for wall in walls:
            if self._physics_service.is_collision(tank, wall):
                wall_position = wall.get_position()
                x_wall = wall_position.get_x()
                y_wall = wall_position.get_y()
                if x > x_wall:
                    x = x_wall + 48
                elif x < x_wall:
                    x = x_wall - 65
            position = Point(x, y)
            velocity = Point(dx, dy)
            tank.set_position(position)
            tank.set_velocity(velocity)

            for enemy in enemies:
                enemy_position = enemy.get_position()
                x_enemy = enemy_position.get_x()
                y_enemy = enemy_position.get_y()
                if self._physics_service.is_collision(enemy, wall):
                    wall_position = wall.get_position()
                    x_wall = wall_position.get_x()
                    y_wall = wall_position.get_y()
                    if x_enemy > x_wall:
                        x_enemy = x_wall + 48
                    elif x_enemy < x_wall:
                        x_enemy = x_wall - 65
                position = Point(x_enemy, y_enemy)
                #velocity = Point(dx_enemy, dy_enemy)
                enemy.set_position(position)
                #enemy.set_velocity(velocity)
            
        for bullet in bullets:
            for wall in walls:
                if self._physics_service.is_collision(bullet, wall):
                    walls.remove(wall)
                    bullets.remove(bullet)
            for enemy in enemies:
                if self._physics_service.is_collision(bullet, enemy):
                    enemies.remove(enemy)
                    bullets.remove(bullet)