#                              #
#    █████╗  ██████╗████████╗  #
#   ██╔══██╗██╔════╝╚══██╔══╝  #
#   ███████║██║        ██║     #
#   ██╔══██║██║        ██║     #
#   ██║  ██║╚██████╗   ██║     #
#   ╚═╝  ╚═╝ ╚═════╝   ╚═╝     #
# Agent de Corruption temporel #

import pyxel
from lib.ui.grid import Grid
from lib.constants import HEIGHT, WIDTH


class App:
  def __init__(self):
    pyxel.init(WIDTH, HEIGHT, title="A.C.T. - Agent de Corruption Temporel")
    pyxel.load("ressources/game.pyxres")
    # pyxel.mouse(True)

    self.grid = Grid()
    self.grid.draw()

    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()

  def draw(self):
    pass


if __name__ == "__main__":
  App()
