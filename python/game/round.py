from turn import Turn

class Round():

  def __init__(self) -> None:
    ended = False
    self.turns = []
    self.next()

  def update(self):
    turn = self.turns[-1]
    if not turn.ended:
      turn.update()
    else:
      self.next()

  def next(self):
    self.turns.append(Turn())
