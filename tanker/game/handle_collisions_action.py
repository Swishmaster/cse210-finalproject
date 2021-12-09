from game import constants
from game.action import Action
from game.point import Point
from game.audio_service import AudioService

class HandleCollisionsAction(Action):
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service
        self._audio_service = AudioService()

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        tanks = cast["tank"]
        walls = cast["walls"]
        bullets = cast["bullets"]
        enemy_bullets = cast["enemy_bullets"]
        enemies = cast["enemy"]
        tank_lives = cast["tank_lives"]
        enemy_lives = cast["enemy_lives"]
        for tank in tanks:
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
                    enemy.set_position(position)
            for bullet in bullets:
                for wall in walls:
                    if self._physics_service.is_collision(bullet, wall):
                        walls.remove(wall)
                        bullets.remove(bullet)
                for enemy in enemies:
                    if self._physics_service.is_collision(bullet, enemy):
                        bullets.remove(bullet)
                        if len(enemy_lives) > 0:
                            cast["enemy_lives"].pop()
                        # self._audio_service.play_sound(constants.SOUND_YEAH)
        
            for enemy_bullet in enemy_bullets:
                if self._physics_service.is_collision(enemy_bullet, tank):
                            enemy_bullets.remove(enemy_bullet)
                            if len(tank_lives) > 0:
                                cast["tank_lives"].pop()
                            # self._audio_service.play_sound(constants.SOUND_HIT)
                for wall in walls:
                    if self._physics_service.is_collision(enemy_bullet, wall):
                            walls.remove(wall)
                            enemy_bullets.remove(enemy_bullet)             