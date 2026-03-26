from models import Games
import json


print("Olá mundo!")

games = Games("JoJo's Bizarre Adventure: Eyes of Heaven", "Action", "PlayStation 4", 2019)

print(F"Jogo: {games.name}")
print(F"Gênero: {games.genre}")
print(F"Plataforma: {games.platform}")
print(F"Ano de Lançamento: {games.release_year}")

games.StartVideoGame()

print(f"O jogo {games.name} está online? {games.IsOnline}")

json.dump(games.__dict__, open("game.json", "w"), indent=4)