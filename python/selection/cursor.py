import pyxel
from ..const import TILES_WIDTH, TILES_HEIGHT

class Cursor():

  def __init__(self) -> None:
    self.selected_tile_x = (0, 0);
    self.selected_tile_y = (0, 0);

  def getSelectedTile(self):
    return (self.selected_tile_x, self.selected_tile_y)

  def updateCursorPos(self):
    self.selected_tile_x = pyxel.mouse_x//TILES_WIDTH
    self.selected_tile_y = pyxel.mouse_y//TILES_HEIGHT

  def highlight_selected_tile(self):
    tile_pos = self.getSelectedTile()
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

cursor = Cursor()
