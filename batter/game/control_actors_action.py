from game.action import Action
from game import constants
from game.point import Point

class ControlActorsAction(Action):
    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        paddles = cast["paddle"]
        for paddle in paddles:
            # position = paddle.get_position()
            # x = position.get_x()

            direction = self._input_service.get_direction()
            paddle.set_velocity(direction.scale(constants.PADDLE_SPEED))        
