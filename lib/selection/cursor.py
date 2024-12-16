import pyxel
from ..config import TILES_W, TILES_H

class Cursor():
  def __init__(self):
    pass

  def get_selected_tile(self):
    pixel_pos = (pyxel.mouse_x, pyxel.mouse_y)
    tile_pos = (pixel_pos[0]//TILES_W, pixel_pos[1]//TILES_H)
    return tile_pos

  def highlight_selected_tile(self):
    tile_pos = self.get_selected_tile()
    pyxel.blt(
       tile_pos[0]*TILES_W,
       tile_pos[1]*TILES_H,
       0,
       32,
       0,
       TILES_W,
       TILES_H,
       0
    )

cursor = Cursor()
