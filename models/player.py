from random import shuffle

from models.dashboard import Dashboard


VALID_OPTIONS = ["x", "o"]


class Player():
    def __init__(self,
                 name: str = None,
                 mark: str = None):
        valid_options = VALID_OPTIONS
        shuffle(valid_options)
        self._mark = valid_options[0] if not mark else mark
        self._name = name if name else 'Noughts' if self._mark == 'o' else 'Crosses'
        self._my_turn = False
        self._winner = False

    @classmethod
    def create(cls,
             mark: str = None,
             name: str = None):
        kwarg = {}
        if mark in VALID_OPTIONS or not mark:
            kwarg["mark"] = mark if mark in VALID_OPTIONS else None
            kwarg["name"] = name if name else None
            print(kwarg)

            return Player(**kwarg)

    @property
    def name(self):
        return self._name
    
    @property
    def mark(self):
        return self._mark

    @property
    def my_turn(self):
        return self._my_turn

    @property
    def winner(self):
        return self._winner

    @name.setter
    def name(self, name):
        self._name = name

    @mark.setter
    def mark(self, mark):
        self._mark = mark

    @my_turn.setter
    def my_turn(self, my_turn):
        self._my_turn = my_turn

    @winner.setter
    def winner(self, winner):
        self._winner = winner
