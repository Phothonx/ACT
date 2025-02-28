from ..pawns.soldier import Soldier

class Player():

  def __init__(self, id) -> None:
    self.id = id
    self.pawns = []

  def newPawn(self, spawn):
    self.pawns.append(Soldier(spawn, self))

players = [ Player(0), Player(1)]
