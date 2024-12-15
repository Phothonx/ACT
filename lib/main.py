#                              #
#    █████╗  ██████╗████████╗  #
#   ██╔══██╗██╔════╝╚══██╔══╝  #
#   ███████║██║        ██║     #
#   ██╔══██║██║        ██║     #
#   ██║  ██║╚██████╗   ██║     #
#   ╚═╝  ╚═╝ ╚═════╝   ╚═╝     #
# Agent de Corruption temporel #

import pyxel

HEIGHT = 128 # pixels
WIDTH = 128

TILES_WIDTH = 8 # pixels
TILES_HEIGHT = 8

def addt(a, b):
  return tuple(sum(i) for i in zip(a, b))

class Turn:
  SELECTOR = (32, 0)

  def __init__(self):
    self.turn = 0 # player 0 start
    self.pawns = [[], []] # list of pawns in the game for player 0, 1

  def __click(pos): # return True
    mouse = (pyxel.mouse_x(), pyxel.mouse_y())
    button = pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)
    return mouse == pos and button

  def __highlight_case(self, pos):
    pyxel.blt(
      pos[0]*TILES_WIDTH,
      pos[1]*TILES_HEIGHT,
      0,
      self.SELECTOR[0],
      self.SELECTOR[1],
      TILES_WIDTH,
      TILES_HEIGHT,
      0
    )

  def select_move(self, pawn):
    cardinals = [ (0, 1), (2, 0), (0, -1), (-1, 0) ]
    for direction in cardinals:
      clickable = addt(pawn.pos, direction)
      self.__highlight_case(clickable)
      if self.__click(clickable):
        pawn.move(direction)
        return True
    return False

class Pawn:
  LIFE = 100
  DESIGN = (0, 0)

  def __init__(self, spawn, owner):
    self.spawn = spawn # tuple (x, y)
    self.owner = owner # int player 0, 1
    self.actions = [] # array of action
    self.design = self.DESIGN
    self.pos = self.spawn
    self.life = self.LIFE

  def move(self, deplacement):
    self.pos = self.addt(self.pos, deplacement)
    self.actions.append(("move", deplacement))

  def draw(self):
    pyxel.blt(
      self.pos[0]*TILES_WIDTH,
      self.pos[1]*TILES_HEIGHT,
      0,
      self.design[0],
      self.design[1],
      TILES_WIDTH,
      TILES_HEIGHT,
      0
    )


class Soldier(Pawn):
  LIFE = 100
  DESIGN = (16, 0)

class Grid:
  HEIGHT = 16 # tiles
  WIDTH = 16

  def __init__(self):
    self.tilemap = pyxel.tilemaps[0]

  def draw(self):
   for x in range(self.WIDTH):
     for y in range(self.HEIGHT):
       pyxel.bltm(
         x*TILES_WIDTH,
         y*TILES_HEIGHT,
         0,
         x*TILES_WIDTH,
         y*TILES_HEIGHT,
         TILES_WIDTH,
         TILES_HEIGHT
       )


class App:
  def __init__(self):
    pyxel.init(WIDTH, HEIGHT, title="A.C.T. - Agent de Corruption Temporel")
    pyxel.load("ressources.pyxres")
    pyxel.mouse(True)

    self.grid = Grid()
    self.grid.draw()

    self.turn = Turn()
    self.turn.pawns[0].append(Soldier((10, 5), 0))
    for i in range(5):
      while not self.turn.select_move(self.turn.pawns[0][0]):
        pass

    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()

  def draw(self):
    pass


App()
