import utils

class Article:
  """Represents an Article and its structure."""
  def __init__(self, header, content, references):
      self.header = header                        # Header
      self.content = content                      # Content
      # self.references = utils.flatten(references) # Flat List of Reference
      self.references = []
      utils.flatten_2(references, self.references)                # Flat List of Reference

  def show(self):
    print("> Article: ", self.header.title_author)
    print("> Publication: ", self.header.publication)
    print("> Chapters: ")
    # self.content.show()
    for item in self.content.chapters:
      item.show()
    print("> References: ")
    # print(self.references)
    for item in self.references:
      print(item)