from action import Action

class Turn():

  def __init__(self) -> None:
    ended = False
    self.actions = []
    self.next()

  def update(self):
    action = self.actions[-1]
    if not action.ended:
      action.update()
    else:
      self.next()

  def next(self):
    self.actions.append(Action())


#   def __init__(self):
#     self.playing = 0 # player 0 start
#     self.turn = 0 # counter
#     self.round = 0 # counter
#     self.pawns = [[], []] # list of pawns in the game for player 0, 1
#
#   def update(self):
#     self.playing = self.turn % 2
#     if self.turn % 8 == 0 and len(self.pawns[0]) < self.round+1:
#       self.play_round()
#     self.play_turn()
#
#
#   def draw_pawns(self):
#     for player in [0, 1]:
#       for pawn in self.pawns[player]:
#         pawn.draw()
#
#   def draw_mvts(self):
#     self.pawns[self.playing][self.round].draw_mvts()
#
#   def play_round(self):
#     self.pawns[0].append(Soldier((15, 8), 0))
#     self.pawns[1].append(Soldier((0, 8), 1))
#
#   def play_turn(self):
#     player = self.playing
#     pawn = self.pawns[player][self.round]
#     played = pawn.select_move()
#     if played:
#       self.turn += 1
#
# turn = Turn()
