class Vehicles:
    def __init__(self, name, type, genre, brand, release_year):
        print("Criando um novo veículo...")
        self.name = name
        self.type = type
        self.genre = genre
        self.brand = brand
        self.release_year = release_year
        self.CanFind = False

    def FindVehicle(self):
        print(f"Buscando o veículo {self.name}, tipo {self.type}...")
        self.CanFind = True

    def to_dict(self):
        return {
            "name": self.name,
            "type": self.type,
            "genre": self.genre,
            "brand": self.brand,
            "release_year": self.release_year,
            "CanFind": self.CanFind
        }