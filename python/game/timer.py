import time
from ..const import PLAY_WAIT

class Countdown():
  def __init__(self) -> None:
    self.countstop = time.time()

  def start(self):
    self.countstop = time.time() + PLAY_WAIT

  def ended(self):
    return time.time() >= self.countstop
