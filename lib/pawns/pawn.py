import pyxel
from ..config import TILES_W, TILES_H
from ..utils import addt
from ..selection.cursor import cursor

class Pawn:
  LIFE = 100
  SPRITE_P0 = (16, 0)
  SPRITE_P1 = (24, 0)

  def __init__(self, spawn, owner):
    self.spawn = spawn # tuple (x, y)
    self.owner = owner # int player 0, 1
    self.actions = [] # array of action
    self.sprite = self.SPRITE_P0 if owner == 0 else self.SPRITE_P1
    self.pos = self.spawn
    self.life = self.LIFE

  def move(self, deplacement):
    self.pos = addt(self.pos, deplacement)
    self.actions.append(("move", deplacement))

  def draw(self):
    pyxel.blt(
      self.pos[0]*TILES_W,
      self.pos[1]*TILES_H,
      0,
      self.sprite[0],
      self.sprite[1],
      TILES_W,
      TILES_H,
      0
    )

  def select_move(self):
    cardinals = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]
    for direction in cardinals:
      clickable = addt(self.pos, direction)
      if cursor.get_selected_tile() == clickable and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        self.move(direction)
        return True
    return False

  def draw_mvts(self):
    cardinals = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]
    for direction in cardinals:
      hlpos = addt(self.pos, direction)
      pyxel.blt(
        hlpos[0]*TILES_W,
        hlpos[1]*TILES_H,
        0,
        32,
        0,
        TILES_W,
        TILES_H,
        0
      )
