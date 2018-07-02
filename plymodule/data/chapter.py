
class Chapter:
  """Represents the Chapter of an Article."""
  def __init__(self, number, content):
      self.number = number                      # Number of the chapter
      self.content = content                    # Chapter text content

  def show(self):
    print("> Chapter Title: ", self.number)

  def toString(self):
    return "\t-> Chapter Title:\t" + self.number
    # print("> Content:", self.content)