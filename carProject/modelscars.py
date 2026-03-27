class Vehicles:
    def __init__(self, name, type, brand, release_year, cep, endereco):
        self.name = name
        self.type = type
        self.brand = brand
        self.release_year = release_year
        self.cep = cep
        self.endereco = endereco
        
      

    def FindVehicle(self):
        print(f"Buscando o veículo {self.name}, tipo {self.type}...")
        self.CanFind = True

    def to_dict(self):
        return {
            "name": self.name,
            "type": self.type,
            "brand": self.brand,
            "release_year": self.release_year,
            "cep": self.cep,
            "endereco": self.endereco
        }