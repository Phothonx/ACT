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
from python.game.game import Game
from python.selection.cursor import cursor

class App:

  def __init__(self) -> None:
    print("[] Création du jeu...")
    pyxel.init(WIDTH_PIXELS, HEIGHT_PIXELS, title=TITLE)
    pyxel.load("ressources/game.pyxres")
    pyxel.mouse(True)
    self.game = Game()

  def run(self):
    pyxel.run(self.__update, self.__draw)

  def __update(self):
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()
    self.game.update()
    cursor.updateCursorPos()

  def __draw(self):
    self.game.draw()
    cursor.highlight_selected_tile()

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
