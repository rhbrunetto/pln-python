
class Content:
  """Represents the Content of an Article."""
  def __init__(self, chapters):
      self.chapters = chapters            # Chapter List

  def add_chapter(self, chapter):
    self.chapters.append(chapter)
  
  def show(self):
    for c in self.chapters:
      c.show()