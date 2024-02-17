'''Опишіть об'єкти мистецтва для музею. скористайтесь всіма 5 принципами:
абстракція, наслідування, поліморфізм, скриття, інкапсуляція. додайте property, setter.
Створіть хоча-б по одному інстансу кожного класу і викличте методи'''

class ArtPiece:
    def __init__(self, title:str, artist:str, year:int):
        self._title = title
        self._artist = artist
        self._year = year

    @property
    def title(self):
        return self._title

    @property
    def artist(self):
        return self._artist

    @property
    def year(self):
        return self._year

    @title.setter
    def title(self, value):
            self._title = value
    @artist.setter
    def artist(self, value: str):
        self._artist = value

    @year.setter
    def year(self, value):
        self._year = value

    def display_info(self):
        return f"{self._title} by {self._artist}, created in {self._year}"

class Painting(ArtPiece):
    def __init__(self, title, artist, year, style):
        super().__init__(title, artist, year)
        self._style = style

    @property
    def style(self):
        return self._style
    @property
    def year(self):
        return self._year

    @style.setter
    def style(self, value):
        self._style = value

    @year.setter
    def year(self, value):
        self._year = value

    def display_info(self):
        return f"{super().display_info()} in {self._style} style"

class Sculpture(ArtPiece):
    def __init__(self, title, artist, year, material):
        super().__init__(title, artist, year)
        self._material = material

    @property
    def style(self):
        return self._style

    @property
    def year(self):
        return self._year

    @style.setter
    def style(self, value):
        self._style = value

    @year.setter
    def year(self, value):
        self._year = value
    @property
    def material(self):
        return self._material
    @material.setter
    def material(self, value):
        self._material = value

    def display_info(self):
        return f"{super().display_info()} made of {self._material}"


painting = Painting(title="kartina", artist="Vincent van Gogh", year=2024, style="Impressionism")
sculpture = Sculpture(title="Gorgulia", artist="Michelangelo", year=1555, material="glina")

print(painting.display_info())
print(sculpture.display_info())

painting.title = "kartina1"
sculpture.title = "godzila"
painting.year = 1889
sculpture.year = 2024
sculpture.material = "sand"

print(painting.display_info())
print(sculpture.display_info())