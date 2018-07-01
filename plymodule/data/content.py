import utils

class Content:
  """Represents the Content of an Article."""
  def __init__(self, chapters):
      # self.chapters = [y for x in chapters for y in x] # Flat Chapter List
      self.chapters = utils.flatten(chapters) # Flat Chapter List

  def add_chapter(self, chapter):
    self.chapters.append(chapter)
  
  def show(self):
    # for c in self.chapters:
    #   c.show()
    print(self.chapters)