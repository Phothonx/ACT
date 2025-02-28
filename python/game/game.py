from ..ui.grid import grid
from .player import players
from ..pawns.soldier import Soldier

class Game():

  def __init__(self)->None:
    self.round = -1
    self.turn = -1
    # self.playing = -1

  def draw(self):
    grid.draw()
    for player in players:
      for pawn in player.pawns:
        pawn.draw(self.turn)

  def update(self):
    if self.round >= 3:
      print("FIN")
      quit()
    elif self.turn >= 5 or self.round <= -1:
      self.newRound()
    else:
      first_player = players[self.round%2]
      self.play(first_player)
      second_player = players[(self.round+1)%2]
      self.play(second_player)
      self.turn += 1
    # elif self.playing <= -1:
    #   self.newTurn()
    #   self.nextPlayer()
    # else:
    #   self.play()

  def nextPlayer(self):
    playing = self.playing
    round = self.round
    if playing == -1: # si tout le monde a joué
      self.playing = round%2 # on alterne le premier à jouer 1 round /2
    elif round%2 == (playing+1)%2: # si c'est le 2eme joueur du round qui a joué
      self.playing = -1 # il n'y a plus personne qui doit jouer
    else:
      self.playing = (playing+1)%2 # sinon c'est à l'autre de jouer

  def play(self, player):
    print("    - Joueur " + str(player.id) + " joue")
    if len(player.pawns) == 0:
      raise ValueError("No pawns to be played")
    if player.pawns[-1].select_move(self.turn):
      self.nextPlayer()

  def newRound(self):
    self.round += 1
    # if self.turn != -1 or self.turn != 5:
    #   raise ValueError(f"Round ended on wrong turn ({self.turn})")
    print("@ Round: " + str(self.round))
    self.turn = 0 # come back to the past baby
    for player in players:
      player.pawns.append(Soldier((5, 5), player))

  def newTurn(self):
    self.turn += 1
    print("  * Tour: " + str(self.turn))
    self.nextPlayer()
