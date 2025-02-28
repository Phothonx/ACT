from ..selection.cursor import cursor
from player import players

class Action():
  def __init__(self, first_player) -> None:
    self.play(players[first_player]) # each player play
    self.play(players[(first_player+1)%2]) # first player change each turn

  def play(self, player):
    pawn = player.pawns[-1]
    pawn.select_move(cursor)
