import pyxel
from ..config import WIDTH_T, HEIGHT_T, TILES_W, TILES_H

class Grid():
  def __init__(self):
    pass

  def draw(self):
   for x in range(WIDTH_T):
     for y in range(HEIGHT_T):
       pyxel.bltm(
         x*TILES_W,
         y*TILES_H,
         0,
         x*TILES_W,
         y*TILES_H,
         TILES_W,
         TILES_H
       )

grid = Grid()
