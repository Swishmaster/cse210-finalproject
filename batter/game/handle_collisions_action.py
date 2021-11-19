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

        ball = cast["balls"][0]
        paddle = cast["paddle"][0] # there's only one
        bricks = cast["bricks"]
        audio_service = AudioService()
        velocity = ball.get_velocity()
        position = ball.get_position()
        position2 = paddle.get_position()
        x = position.get_x()
        x_middle = position2.get_x()
        x_left = x_middle - 47.5
        x_right = x_middle + 47.5
        dx = velocity.get_x()
        dy = velocity.get_y()

        if self._physics_service.is_collision(paddle, ball):
            if x >= x_middle and x <= x_right and dx < 0:
                dx = dx * -1
                dy = dy * -1
            elif x <= x_middle and x >= x_left and dx > 0:
                dx = dx * -1
                dy = dy * -1
            else:
                dx = dx
                dy = dy * -1
            audio_service.play_sound(constants.SOUND_BOUNCE)

        velocity = Point(dx, dy)
        ball.set_velocity(velocity)

        for brick in bricks:
            if self._physics_service.is_collision(ball, brick):
                dx = dx 
                dy = dy * -1
                audio_service.play_sound(constants.SOUND_BOUNCE)
                bricks.remove(brick)

        velocity = Point(dx, dy)
        ball.set_velocity(velocity)