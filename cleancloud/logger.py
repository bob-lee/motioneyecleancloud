import datetime

class logger:
  FILENAME = 'test.log'

  def __init__(self, name):
    if name:
      self.FILENAME = name

  def log(self, t, s):
    N = datetime.datetime.now()
    now = N.strftime("%Y-%m-%d %H:%M:%S")
    with open(self.FILENAME, 'a') as file:
      file.write('{} [{}] {}\n'.format(now, t, s))

  def debug(self, s):
    self.log('DEBUG', s)

  def info(self, s):
    self.log('INFO', s)

  def error(self, s):
    self.log('ERROR', s)
