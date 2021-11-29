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
        bullet = cast["bullets"]
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
                    x = x + 2
                    dx = dx * -1
                elif x < x_wall:
                    x = x - 2
                    dx = dx * -1
                elif y > y_wall:
                    y = y + 2
                    dy = dy * -1
                elif y < y_wall:
                    y = y - 2
                    dy = dy * -1
                else:
                    x = x
                    y = y
                    dx = dx
                    dy = dy
            position = Point(x, y)
            velocity = Point(dx, dy)
            tank.set_position(position)
            tank.set_velocity(velocity)

            # if len(bullet) > 0:
            #     if self._physics_service.is_collision(bullet, wall):
            #         walls.remove(wall)   

        # paddles = cast["paddle"]
        # walls = cast["walls"]
        # audio_service = AudioService()
        # x = position.get_x()
        # dx = velocity.get_x()
        # dy = velocity.get_y()
        # for paddle in paddles:
        #     if self._physics_service.is_collision(paddle, ball):
        #             dx = dx
        #             dy = dy * -1
        #             audio_service.play_sound(constants.SOUND_BOUNCE)
        #     velocity = Point(dx, dy)
        #     ball.set_velocity(velocity)
        #     position2 = paddle.get_position()
        #     x_left = position2.get_x() - 96

        # for wall in walls:
        #     if self._physics_service.is_collision(ball, wall):
        #         dx = dx 
        #         dy = dy * -1
        #         audio_service.play_sound(constants.SOUND_BOUNCE)
        #         walls.remove(wall)

        # velocity = Point(dx, dy)
        # ball.set_velocity(velocity)
