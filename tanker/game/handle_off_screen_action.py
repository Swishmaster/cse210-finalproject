from game.action import Action
from game.point import Point
from game import constants
from game.bullet import Bullet
from game.tank import Tank

class HandleOffScreenAction(Action):
    def execute(self, cast):
        for group in cast.values():
            for actor in group:
                self._handle_actions(actor, cast)

    def _handle_actions(self, actor, cast):
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        bullets = cast["bullets"]
        
        if x > constants.MAX_X-20 or x < 0:
            if x < 0:
                x = 0
            elif x > constants.MAX_X - 96:
                x = constants.MAX_TANK_X
                for bullet in bullets:
                    bullets.remove(bullet)
            else:
                x = x
        elif y < 0 or y > constants.MAX_Y-20:
            if y < 0:
                y = 0
            elif y > constants.MAX_Y-20:
                y = constants.MAX_TANK_Y
                for bullet in bullets:
                    bullets.remove(bullet)
            else:
                y = y

        position = Point(x, y)
        actor.set_position(position)

