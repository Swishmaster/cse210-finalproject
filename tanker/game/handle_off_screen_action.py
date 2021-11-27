from game.action import Action
from game.point import Point
from game import constants
import sys

class HandleOffScreenAction(Action):
    def execute(self, cast):
        for group in cast.values():
            for actor in group:
                self._handle_actions(actor, cast)

    def _handle_actions(self, actor, cast):
        pass
        # position = actor.get_position()
        # velocity = actor.get_velocity()
        # balls = cast["balls"]
        # x = position.get_x()
        # y = position.get_y()
        # dx = velocity.get_x()
        # dy = velocity.get_y()

        # if x > constants.MAX_X-20 or x < 0:
        #     dx = dx * -1
        # elif y < 0 or y > constants.MAX_Y-20:
        #     dy = dy * -1
        # # elif y > constants.MAX_Y-20:
        # #     print("You have run out of balls. You lose. Try again!") 
        # #     sys.exit()
        # else:
        #     dx = dx
        #     dy = dy

        # velocity = Point(dx, dy)
        # actor.set_velocity(velocity)

