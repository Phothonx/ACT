from ..pawns.soldier import Soldier

class Player():

  def __init__(self, id) -> None:
    self.id = id
    # self.id = 0 ou 1
    self.pawns = []
    # liste de pions possédés par le joueur
    # un nouveau est àjouté à chaque tour

  # ajoute un nouveau pion au coordonnées spawn (h, l)
  def newPawn(self, spawn):
    new_pawn = Soldier(spawn, self)
    self.pawns.append(new_pawn)

players = [ Player(0), Player(1) ]
