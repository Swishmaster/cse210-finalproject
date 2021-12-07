import raylibpy
from game import constants
from game.point import Point
from game.loser_winner import LoserWinner
from game.audio_service import AudioService

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """

    def __init__(self, cast, script):
        """The class constructor.
        
        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        self._cast = cast
        self._script = script
        self._keep_playing = True
        self._audio_service = AudioService()
        
    def start_game(self, cast):
        """Starts the game loop to control the sequence of play."""
        while self._keep_playing:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")
            if raylibpy.window_should_close():
                self._keep_playing = False
            elif len(cast["enemy_lives"]) <= 0:
                cast["enemy"] = []
                cast["winner"] = []
                loser_winner = LoserWinner()
                position = Point(175, 50)
                loser_winner.set_position(position)
                loser_winner.set_velocity(Point(0,0))
                loser_winner.set_height(500)
                loser_winner.set_width(500)
                loser_winner.set_image(constants.IMAGE_WINNER)
                cast["winner"].append(loser_winner)
                self._audio_service.play_sound(constants.SOUND_WINNER)
            elif len(cast["tank_lives"]) <= 0:
                cast["tank"] = []
                cast["loser"] = []
                loser_winner = LoserWinner()
                position = Point(175, 50)
                loser_winner.set_position(position)
                loser_winner.set_velocity(Point(0,0))
                loser_winner.set_height(500)
                loser_winner.set_width(500)
                loser_winner.set_image(constants.IMAGE_LOSER)
                cast["loser"].append(loser_winner)
                self._audio_service.play_sound(constants.SOUND_LOSER)

    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)