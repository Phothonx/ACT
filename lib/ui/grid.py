import pyxel
from ..constants import TILES_WIDTH, TILES_HEIGHT

class Grid():
  HEIGHT = 16 # tiles
  WIDTH = 16

  def __init__(self):
    pass

  def draw(self):
   for x in range(self.WIDTH):
     for y in range(self.HEIGHT):
       pyxel.bltm(
         x*TILES_WIDTH,
         y*TILES_HEIGHT,
         0,
         x*TILES_WIDTH,
         y*TILES_HEIGHT,
         TILES_WIDTH,
         TILES_HEIGHT
       )

grid = Grid()
