import pyxel
from ..const import WIDTH
from ..pawns.soldier import Soldier
from turn import Turn
from ..ui.grid import Grid
from player import Player


class Game():

  def __init__(self, cursor) -> None:
    self.cursor = cursor
    self.players = [ Player(0), Player(1) ]
    self.grid = Grid()

  def update(self):
    pass

  def draw(self):
    self.grid.draw()
    for player in self.players:
      for pawn in player.pawns:
        pawn.draw()

  def end(self):
    pass

  def reset(self):
    pass
