import pyxel

class Player:
  def __init__(self):
    self.x = 50
    self.y = 50

class App:
  def __init__(self):
    pyxel.init(160, 120, title="A.C.T. - Agent de Corruption Temporel")
    pyxel.load("perso.pyxres")

    self.x = 0
    self.y = 0

    pyxel.run(self.update, self.draw)


  def update(self):
    self.x += 1
    self.y += 1
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()

  def draw(self):
    pyxel.cls(0)
    pyxel.blt(self.x, self.y, 0, 0, 0, 8, 8)

App()
