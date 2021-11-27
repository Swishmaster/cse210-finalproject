from game import constants
from game.action import Action
from game.point import Point
from game.audio_service import AudioService
from game.tank import Tank

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
        tank = Tank()
        velocity = tank.get_velocity()
        dx = velocity.get_x()
        dy = velocity.get_y()

        for wall in walls:
            if self._physics_service.is_collision(tank, wall):
                dx = 0
                dy = 0
            velocity = Point(dx, dy)
            tank.set_velocity(velocity)

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
