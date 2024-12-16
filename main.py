#                              #
#    █████╗  ██████╗████████╗  #
#   ██╔══██╗██╔════╝╚══██╔══╝  #
#   ███████║██║        ██║     #
#   ██╔══██║██║        ██║     #
#   ██║  ██║╚██████╗   ██║     #
#   ╚═╝  ╚═╝ ╚═════╝   ╚═╝     #
# Agent de Corruption temporel #

import pyxel
from lib.config import TITLE, WIDTH_P, HEIGHT_P
from lib.ui.grid import grid
from lib.selection.cursor import cursor
from lib.turn.turn import turn

class App:
  def __init__(self):
    pyxel.init(WIDTH_P, HEIGHT_P, title=TITLE)
    pyxel.load("ressources/game.pyxres")
    pyxel.mouse(True)

    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()
    turn.update()
    print(len(turn.pawns[0]))

  def draw(self):
    grid.draw()
    cursor.highlight_selected_tile()
    turn.draw_pawns()
    turn.draw_mvts()


App()
