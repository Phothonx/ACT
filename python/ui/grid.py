import pyxel
from ..const import WIDTH, HEIGHT, TILES_WIDTH, TILES_HEIGHT

class Grid():
  def draw(self):
   for x in range(WIDTH):
     for y in range(HEIGHT):
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
