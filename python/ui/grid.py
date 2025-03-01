import pyxel
from ..const import WIDTH, HEIGHT, TILES_WIDTH, TILES_HEIGHT
from ..sprites import TILEMAP

class Grid():
  def draw(self):
   for x in range(WIDTH):
     for y in range(HEIGHT):
       pyxel.bltm(
         x*TILES_WIDTH,
         y*TILES_HEIGHT,
         TILEMAP,
         x*TILES_WIDTH,
         y*TILES_HEIGHT,
         TILES_WIDTH,
         TILES_HEIGHT
       )

grid = Grid()
