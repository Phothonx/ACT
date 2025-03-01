import pyxel
from ..const import TILES_WIDTH, TILES_HEIGHT
from ..lib import addt
from ..selection.cursor import cursor

class Pawnstate:
  def __init__(self, life, pos) -> None:
    self.life = life
    self.pos = pos


class Pawn:
  MAX_LIFE = 100
  SPRITE_P0 = (16, 0)
  SPRITE_P1 = (24, 0)

  def __init__(self, spawn, owner):
    self.owner = owner
    spawn_state = Pawnstate(self.MAX_LIFE, spawn)
    self.state = [ spawn_state ] # state of the pawn for a certain turn in this array
    self.sprite = self.SPRITE_P0 if owner.id == 0 else self.SPRITE_P1
    # self.pos = spawn # initial position
    # self.life = self.MAX_LIFE

  def move(self, turn, deplacement): # edit next pawn state
    pos = self.state[turn].pos
    npos = addt(pos, deplacement)
    nlife = self.state[turn].life
    new_state = Pawnstate(nlife, npos)
    if len(self.state) < turn:
      raise ValueError(f"Move: Missing pawn state {turn}")
    self.state[turn] = new_state
    if turn+1 >= len(self.state): # on ajoute un state si il n'existe pas encore
      self.state.append(new_state)
    else:
      self.state[turn + 1] = new_state

  def draw(self, turn):
    if len(self.state) < turn:
      raise ValueError(f"Draw: Missing pawn state {turn} for player {self.owner.id}")
    if turn != -1:
      pyxel.blt(
        self.state[turn].pos[0]*TILES_WIDTH,
        self.state[turn].pos[1]*TILES_HEIGHT,
        0,
        self.sprite[0],
        self.sprite[1],
        TILES_WIDTH, # a pawn is the size of a tile
        TILES_HEIGHT,
        0 # black is colkey
      )

  def select_move(self, turn):
    cardinals = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]
    for direction in cardinals:
      clickable = addt(self.state[turn].pos, direction)
      if cursor.selected_tile() == clickable and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        self.move(turn, direction)
        return True
    return False

  def draw_mvts(self, turn):
    cardinals = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]
    if turn != -1:
      for direction in cardinals:
        hlpos = addt(self.state[turn].pos, direction)
        pyxel.blt(
          hlpos[0]*TILES_WIDTH,
          hlpos[1]*TILES_HEIGHT,
          0,
          32,
          0,
          TILES_WIDTH,
          TILES_HEIGHT,
          0
        )
