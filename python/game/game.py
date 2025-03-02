from ..ui.grid import grid
from .player import players
from .timer import Countdown
from ..const import NB_ROUNDS, NB_TURNS, HEIGHT


def spawnPos(round, player_id):
  return (0, round) if player_id == 0 else (HEIGHT - 1, round)


class Game():

  def __init__(self)->None:
    # l'initialisation se fait à -1 pour appeler une fois newRound() et newTurn() dans le "vide", et évider une initialisation manuelle
    self.frame = 0
    self.upd = 0
    self.round = -1
    self.turn = -1
    self.playing = -1 # 0, 1 ou -1 = tout le monde a joué pour ce tour
    self.wait = Countdown()

  # dessine dans l'ordre la grille, les pions, les interfaces de sélaction
  def draw(self):
    self.frame += 1
    grid.draw()
    for player in players:
      for pawn in player.pawns[:-1]:
        pawn.draw(self.turn)
        pawn.highlightNext(self.turn)
      player.pawns[-1].draw(self.turn)
    if self.playing != -1:
      players[self.playing].pawns[-1].draw_mvts(self.turn)

  # decide de l'action à réaliser en fonction de self.tour, self.round et self.playing:
  # fait appel à la fonction de jeu pour le joueur actuel la plupart du temps
  def update(self):
    self.upd += 1
    if self.wait.ended():
      if self.playing <= -1: # on finit un tour/round ssi les 2 jours on joués
        if (self.round  >= NB_ROUNDS - 1) and (self.turn >= NB_TURNS-1):
          print("FIN")
          quit()
        elif self.turn >= NB_TURNS - 1 or self.round <= -1:
          self.newRound()
        elif self.playing <= -1 or self.turn <= -1:
          self.newTurn()
      else:
        self.play(players[self.playing])

  # définit le prochain joueur qui doit jouer ce tour pour l'attribut self.playing
  # quand le 2eme joueur a joué, -1 (pour passer au tour/round suivant)
  # roud pair: joueur0 joue en premier
  # round impair: joueur1 joue en premier
  def nextPlayer(self):
    playing = self.playing
    round = self.round
    if playing == -1: # si tout le monde a joué
      self.playing = round%2 # on alterne le premier à jouer 1 round sur 2
      print(f"    - Joueur {str(self.playing)} joue")
    elif round%2 == (playing+1)%2: # si c'est le 2eme joueur du round qui a joué
      self.playing = -1 # il n'y a plus personne qui doit jouer
      self.wait.start() # on temporise la fin du tour pour la lecture de jeu
    else:
      self.playing = (playing+1)%2 # sinon c'est à l'autre de jouer
      print(f"    - Joueur {str(self.playing)} joue")

  # check si le joueur a joué cette frame
  # si oui, appelle la fonction de mouvement du dernier pion (normalemnt joué pour ce round)
  # change self.playing une fois l'action jouée
  def play(self, player):
    # print(self.turn)
    if len(player.pawns) == 0:
      raise ValueError("Pas de pion à jouer")
    if player.pawns[-1].select_move(self.turn):
      self.nextPlayer()

  # appelée pour passer au round suivant
  # incrémente self.round
  # réinitialise self.turn à 0 (action qui "remonte le temps")
  # appelle nextPlayer
  # crée un jouveau pion pour chaque joueur
  def newRound(self):
    self.round += 1
    if self.turn != -1 and self.turn != NB_TURNS-1:
      raise ValueError(f"Round finit sur le mauvais tour: {self.turn}")
    if self.playing != -1:
      raise ValueError(f"Le round s'est finit lors du tour du joueur {self.playing}")
    print("@ Round: " + str(self.round))
    self.turn = 0
    print("  * Tour: " + str(self.turn))
    self.nextPlayer()
    for player in players:
      spawn_position = spawnPos(self.round, player.id)
      player.newPawn(spawn_position)

  # appelée pour passer au tour suivant
  # incrément self.turn
  # appelle nextPlayer
  def newTurn(self):
    if self.playing != -1:
      raise ValueError(f"Le tour s'est finit lors du tour du joueur {self.playing}")
    self.turn += 1
    print("  * Tour: " + str(self.turn))
    self.nextPlayer()
