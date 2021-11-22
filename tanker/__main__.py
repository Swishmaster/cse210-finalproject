import random
import os
os.environ['RAYLIB_BIN_PATH'] = '.'
from raylibpy import RAYLIB_BIN_PATH
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService
from game.brick import Brick
from game.ball import Ball
from game.paddle import Paddle
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_off_screen_action import HandleOffScreenAction
from game.move_actors_action import MoveActorsAction
from game.artifact import Artifact

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    cast["bricks"] = []
    bricks = []
    for y in range(0, constants.MAX_Y-400, 40): #5 rows
        for x in range(0, constants.MAX_X, 50): #16 columns
            position = Point(x, y)

            brick = Brick()
            brick.set_position(position)
            brick.set_height(constants.BRICK_HEIGHT)
            brick.set_width(constants.BRICK_WIDTH)
            brick.set_image(constants.IMAGE_BRICK)
            bricks.append(brick)
    cast["bricks"] = bricks

    cast["balls"] = []
    ball = Ball()
    balls = []
    position = Point(constants.BALL_X, constants.BALL_Y)
    ball.set_position(position)
    ball.set_width(constants.BALL_WIDTH)
    ball.set_height(constants.BALL_HEIGHT)
    ball.set_image(constants.IMAGE_BALL)
    ball.set_velocity(Point(constants.BALL_DX,constants.BALL_DY))
    balls.append(ball)
    cast["balls"] = balls

    cast["paddle"] = []
    paddle = Paddle()
    paddles = []
    position = Point(constants.PADDLE_X, constants.PADDLE_Y)
    paddle.set_position(position)
    paddle.set_height(constants.PADDLE_HEIGHT)
    paddle.set_width(constants.PADDLE_WIDTH)
    paddle.set_image(constants.IMAGE_PADDLE)
    paddles.append(paddle)
    cast["paddle"] = paddles

    cast["artifact"] = []
    artifacts = []
    artifact = Artifact()
    x = random.randint(0, 775)
    y = random.randint(210, constants.MAX_Y - 100)
    position = Point(x, y)
    artifact.set_position(position)
    artifact.set_height(constants.ARTIFACT_HEIGHT)
    artifact.set_width(constants.ARTIFACT_WIDTH)
    artifact.set_text("Longer Paddle")
    artifact.set_image(constants.IMAGE_ARTIFACT)
    artifacts.append(artifact)
    cast["artifact"] = artifacts


    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    handle_off_screen_action = HandleOffScreenAction()
    control_actors_action = ControlActorsAction(input_service)
    handle_collisions_action = HandleCollisionsAction(physics_service)

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_off_screen_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # Start the game
    output_service.open_window("Batter")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
