from ..ui.grid import grid
from .player import players
from ..pawns.soldier import Soldier

class Game():

  def __init__(self)->None:
    self.round = -1
    self.turn = -1
    self.playing = -1

  def draw(self):
    grid.draw()
    for player in players:
      for pawn in player.pawns:
        pawn.draw(self.turn)
    if self.playing != -1:
      players[self.playing].pawns[-1].draw_mvts(self.turn)

  def update(self):
    if self.round  >= 3 and self.playing <= -1:
      print("FIN")
      quit()
    elif (self.turn >= 2 or self.round <= -1) and self.playing <= -1:
      self.newRound()
    elif self.playing <= -1 or self.turn <= -1:
      self.newTurn()
    else:
      self.play(players[self.playing])

      # first_player = players[self.round%2]
      # self.play(first_player)
      # second_player = players[(self.round+1)%2]
      # self.play(second_player)
      # self.turn += 1
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
      print("    - Joueur " + str(self.playing) + " joue")
    elif round%2 == (playing+1)%2: # si c'est le 2eme joueur du round qui a joué
      self.playing = -1 # il n'y a plus personne qui doit jouer
    else:
      self.playing = (playing+1)%2 # sinon c'est à l'autre de jouer
      print("    - Joueur " + str(self.playing) + " joue")

  def play(self, player):
    # print(self.turn)
    if len(player.pawns) == 0:
      raise ValueError("No pawns to be played")
    if player.pawns[-1].select_move(self.turn):
      self.nextPlayer()

  def newRound(self):
    self.round += 1
    if self.turn != -1 and self.turn != 2:
      raise ValueError(f"Round ended on wrong turn ({self.turn})")
    if self.playing != -1:
      raise ValueError(f"Bad end of round, ended on player{self.playing}'s turn")
    print("@ Round: " + str(self.round))
    self.turn = -1 # come back to the past baby
    for player in players:
      new_pawn = Soldier((5, 5), player)
      player.pawns.append(new_pawn)
      # print(player.pawns)

  def newTurn(self):
    if self.playing != -1:
      raise ValueError(f"Bad end of turn, ended on player{self.playing}'s turn")
    self.turn += 1
    print("  * Tour: " + str(self.turn))
    self.nextPlayer()
