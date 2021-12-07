from game.action import Action
from game import constants
from game.point import Point
from game.physics_service import PhysicsService

class MoveEnemiesAction(Action):
    def __init__(self) -> None:
        super().__init__()
        self._physics_service = PhysicsService()

    def execute(self, cast):
        enemies = cast["enemy"]
        tanks = cast["tank"]
        walls = cast["walls"]
        if len(cast["tank"]) > 0:
            for tank in tanks:
                position_tank = tank.get_position()
                x_position_tank = position_tank.get_x()
                y_position_tank = position_tank.get_y()

            for wall in walls:
                for enemy in enemies:
                    position_enemy = enemy.get_position()
                    x_position_enemy = position_enemy.get_x()
                    y_position_enemy = position_enemy.get_y()
                    velocity_enemy = enemy.get_velocity()
                    dx_enemy = velocity_enemy.get_x()
                    dy_enemy = velocity_enemy.get_y()

                    if x_position_enemy > constants.MAX_X/2 + 48:
                        dx_enemy = -constants.ENEMY_SPEED
                    elif x_position_enemy < constants.MAX_X/2:
                        dx_enemy = constants.ENEMY_HEIGHT
                    elif x_position_enemy == constants.MAX_X/2 + 48:
                        dx_enemy = 0
                    

                    # if self._physics_service.is_collision(enemy, wall):
                    #     if y_position_enemy > y_position_tank:
                    #         dy_enemy = constants.ENEMY_SPEED
                    #     elif y_position_enemy < y_position_tank:
                    #         dy_enemy = -constants.ENEMY_SPEED
                    #     elif y_position_enemy == y_position_tank:
                    #         dy_enemy = constants.ENEMY_SPEED
                    if y_position_enemy > y_position_tank:
                        dy_enemy = -constants.ENEMY_SPEED
                    elif y_position_enemy < y_position_tank:
                        dy_enemy = constants.ENEMY_SPEED
                    elif y_position_enemy == y_position_tank:
                        dy_enemy = 0
                    
                    velocity = Point(dx_enemy, dy_enemy)
                    enemy.set_velocity(velocity)