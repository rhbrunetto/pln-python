
class Header:
  """Represents the Header of an Article."""
  def __init__(self, publication, code, title_author, abstract, keywords):
      self.publication = publication            # Publication
      self.code = code                          # Code
      self.title_author = title_author          # Title/Author
      self.abstract = abstract                  # Abstract content
      self.keywords = keywords                  # Keywords list

  def show(self):
    print("> Publication:", self.publication)
    print("> Code:", self.code)
    print("> Title_Author:", self.title_author)
    print("> Abstract:", self.abstract)
    print("> Keywords:", self.keywords)