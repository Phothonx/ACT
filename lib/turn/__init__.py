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


