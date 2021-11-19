from game import constants
from game.action import Action
from game.point import Point
from game.audio_service import AudioService
from game.paddle import Paddle

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
        paddles = cast["paddle"]
        bricks = cast["bricks"]
        audio_service = AudioService()
        velocity = ball.get_velocity()
        position = ball.get_position()
        x = position.get_x()
        dx = velocity.get_x()
        dy = velocity.get_y()
        for paddle in paddles:
            if self._physics_service.is_collision(paddle, ball):
                    dx = dx
                    dy = dy * -1
                    audio_service.play_sound(constants.SOUND_BOUNCE)
            velocity = Point(dx, dy)
            ball.set_velocity(velocity)
            position2 = paddle.get_position()
            x_left = position2.get_x() - 96

        for brick in bricks:
            if self._physics_service.is_collision(ball, brick):
                dx = dx 
                dy = dy * -1
                audio_service.play_sound(constants.SOUND_BOUNCE)
                bricks.remove(brick)

        velocity = Point(dx, dy)
        ball.set_velocity(velocity)

        if cast["artifact"]:
            artifact = cast["artifact"][0]
            if self._physics_service.is_collision(ball, artifact):
                dx = dx
                dy = dy
                audio_service.play_sound(constants.SOUND_START)
                cast["artifact"] = []
                paddle = Paddle()
                paddles = cast["paddle"]
                position = Point(x_left, constants.PADDLE_Y)
                paddle.set_position(position)
                paddle.set_height(constants.PADDLE_HEIGHT)
                paddle.set_width(constants.PADDLE_WIDTH)
                paddle.set_image(constants.IMAGE_PADDLE)
                paddles.append(paddle)
                cast["paddle"] = paddles

            velocity = Point(dx, dy)
            ball.set_velocity(velocity)
