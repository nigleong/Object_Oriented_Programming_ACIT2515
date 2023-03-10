import csv

from pokemon import Pokemon

class Arena:
    def __init__(self) -> None:
        self.arena = []

    def add(self,pokemon):
        if not isinstance(pokemon,Pokemon):
            raise AttributeError("Is not a pokemon!")
        self.arena.append(pokemon)

    def active(self):
        active = []
        for pkmn in self.arena:
            if pkmn.health > 0:
                active.append(pkmn)
        return active

    def __len__(self):
        return len(self.active())
    
    def load_from_file(self,filename="pokemons.txt"):
       with open(filename, "r") as pkmn:
            reader = csv.reader(pkmn)
            next(reader) # skip header
            for row in reader:
                name, health, level = row
                pokemon = Pokemon(name)
                pokemon.health = int(health)
                pokemon.level = int(level)
                self.add(pokemon)
    
    def make_team(self,level):
        teams = []
        for pkmn in self.active():
            if pkmn.level == level:
                teams.append(pkmn)
        return Team(teams)

class Team:
    def __init__(self,team) -> None:
        self.team = team

    def get_pokemons(self):
        return self.team 


if __name__ == "__main__":
    A = Arena()
    charizard = Pokemon("Charizard")
    charizard.level = 2
    squirtle = Pokemon("Squirtle")
    A.add(charizard)
    A.add(squirtle)
    print(A.make_team(1))