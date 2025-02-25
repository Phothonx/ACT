import pyxel
from ..const import TILES_WIDTH, TILES_HEIGHT

class Cursor():

  def selected_tile(self):
    pixel_pos = (pyxel.mouse_x, pyxel.mouse_y)
    tile_pos = (pixel_pos[0]//TILES_WIDTH, pixel_pos[1]//TILES_HEIGHT)
    return tile_pos

  def highlight_selected_tile(self):
    tile_pos = self.selected_tile()
    pyxel.blt(
       tile_pos[0]*TILES_WIDTH,
       tile_pos[1]*TILES_HEIGHT,
       0,
       32,
       0,
       TILES_WIDTH,
       TILES_HEIGHT,
       0
    )
