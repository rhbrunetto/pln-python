import utils

class Article:
  """Represents an Article and its structure."""
  def __init__(self, header, content, references):
      self.header = header                        # Header
      self.content = content                      # Content
      self.topTen = []                            # TopTen terms
      self.references = []
      utils.flatten_2(references, self.references)                # Flat List of Reference

  def show(self):
    print("> Article: ", self.header.title_author)
    print("> Publication: ", self.header.publication)
    print("> Top ten terms: ", self.topTen)
    print("> Chapters: ")
    for item in self.content.chapters:
      item.show()
    print("> References: ")
    # print(self.references)
    for item in self.references:
      print("\t-> " + item)
      
  def toString(self):
    strmain = "> Article: " + self.header.title_author + "\n> Publication: " + self.header.publication + "\n> Top ten terms: " + str(self.topTen) + "\n" +"> Chapters: \n"
    for item in self.content.chapters:
      strmain += "\t-> " + item.toString() + "\n"
    strmain += "> References: \n"
    for item in self.references:
      strmain += "\t-> " + item + "\n"
    return strmain

  def setTopTen(self, topten):
    self.topTen = topten
