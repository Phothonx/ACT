import pyxel
from ..const import TILES_WIDTH, TILES_HEIGHT
from ..lib import addt

class Pawn:
  MAX_LIFE = 100
  SPRITE_P0 = (16, 0)
  SPRITE_P1 = (24, 0)

  def __init__(self, spawn, owner):
    self.owner = owner # int player 0, 1
    self.actions = [] # list of action as tuples of (action type, avtion data); ex a movement would be: ("move", (h, v))
    self.sprite = self.SPRITE_P0 if owner == 0 else self.SPRITE_P1
    self.pos = spawn # initial position
    self.life = self.MAX_LIFE

  def move(self, deplacement): # a depplacement is a tuple of (horizontal, vertical) deplacement
    self.pos = addt(self.pos, deplacement)
    self.actions.append(("move", deplacement))

  def draw(self):
    pyxel.blt(
      self.pos[0]*TILES_WIDTH,
      self.pos[1]*TILES_HEIGHT,
      0,
      self.sprite[0],
      self.sprite[1],
      TILES_WIDTH, # a pawn is the size of a tile
      TILES_HEIGHT,
      0 # black is colkey
    )

  def select_move(self, cursor):
    cardinals = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]
    for direction in cardinals:
      clickable = addt(self.pos, direction)
      if cursor.selected_tile() == clickable and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        self.move(direction)
        return True
    return False

  def draw_mvts(self):
    cardinals = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]
    for direction in cardinals:
      hlpos = addt(self.pos, direction)
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
