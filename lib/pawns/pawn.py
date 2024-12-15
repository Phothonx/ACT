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

