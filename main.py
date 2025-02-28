#                              #
#    █████╗  ██████╗████████╗  #
#   ██╔══██╗██╔════╝╚══██╔══╝  #
#   ███████║██║        ██║     #
#   ██╔══██║██║        ██║     #
#   ██║  ██║╚██████╗   ██║     #
#   ╚═╝  ╚═╝ ╚═════╝   ╚═╝     #
# Agent de Corruption temporel #

import pyxel
from python.const import TITLE, WIDTH_PIXELS, HEIGHT_PIXELS
from python.selection.cursor import Cursor
from python.game.game import Game

class App:

  def __init__(self) -> None:
    print("[] Création du jeu...")
    pyxel.init(WIDTH_PIXELS, HEIGHT_PIXELS, title=TITLE)
    pyxel.load("ressources/game.pyxres")
    pyxel.mouse(True)
    self.cursor = Cursor()
    self.game = Game()

  def run(self):
    pyxel.run(self.__update, self.__draw)

  def __update(self):
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()
    self.game.update()

  def __draw(self):
    self.game.draw()

if __name__ == "__main__":
  print('''
-----------------------------------
 ▄▀█ █▀▀ ▀█▀
 █▀█ █▄▄ ░█░
Agent de corruption temporel
-----------------------------------
''')
  client = App()
  print("[] Lancement du jeu...")
  client.run()
