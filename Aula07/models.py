class Games:
    def __init__(self, name, genre, platform, release_year):
        print("Criando um novo jogo...")
        self.name = name
        self.genre = genre
        self.platform = platform
        self.release_year = release_year
        self.IsOnline = False

    def StartVideoGame(self):
        print(f"Iniciando o jogo {self.name}...")
        self.IsOnline = True

    def to_dict(self):
        return {
            "name": self.name,
            "genre": self.genre,
            "platform": self.platform,
            "release_year": self.release_year,
            "IsOnline": self.IsOnline
        }