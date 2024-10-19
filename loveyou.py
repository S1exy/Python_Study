import random


class Pokemon:
    def __init__(self, name, hp, attack, defense, element, dodge_rate):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.element = element
        self.dodge_rate = dodge_rate
        self.status_effects = []

    def is_faint(self):
        return self.hp <= 0

    def attack_pokemon(self, other, move):
        damage = self.attack * move['damage_multiplier'] - other.defense
        if damage < 0:
            damage = 0
        other.hp -= damage
        print(f"{self.name} used {move['name']}! {other.name} received {damage} damage! Remaining HP: {other.hp}")

        # Handle status effects
        if "status" in move:
            if random.random() < move['status']['chance']:
                other.status_effects.append(move['status']['type'])
                print(f"{other.name} is now affected by {move['status']['type']}!")


class ElectricPokemon(Pokemon):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense, 'Electric', 30)

    # Define Electric-specific moves here if necessary


class GrassPokemon(Pokemon):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense, 'Grass', 10)

    # Define Grass-specific moves here if necessary


class WaterPokemon(Pokemon):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense, 'Water', 20)

    # Define Water-specific moves here if necessary


class FirePokemon(Pokemon):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense, 'Fire', 10)

    # Define Fire-specific moves here if necessary


# Create instances of your Pokémon
pika = ElectricPokemon("Pikachu", 80, 35, 5)
bulbasaur = GrassPokemon("Bulbasaur", 100, 35, 10)
squirtle = WaterPokemon("Squirtle", 80, 25, 20)
charizard = FirePokemon("Charmander", 80, 35, 15)

# Sample moves
moves = {
    'Pikachu': [{'name': 'Thunderbolt', 'damage_multiplier': 1.4, 'status': {'type': 'Paralyze', 'chance': 0.1}}],
    'Bulbasaur': [{'name': 'Seed Bomb', 'damage_multiplier': 1.0, 'status': {'type': 'Poison', 'chance': 0.15}}],
    'Squirtle': [{'name': 'Aqua Jet', 'damage_multiplier': 1.4}],
    'Charmander': [{'name': 'Ember', 'damage_multiplier': 1.0, 'status': {'type': 'Burn', 'chance': 0.1}}]
}


# Game loop
def game():
    player_team = [pika, bulbasaur, squirtle, charizard]
    enemy_team = [pika, bulbasaur, squirtle, charizard]

    print("请选择3个宝可梦用于组成你的队伍：")
    for i, pokemon in enumerate(player_team, 1):
        print(f"{i}. {pokemon.name}({pokemon.element}属性)")

    choices = [int(x) - 1 for x in input("输入数字选择你的宝可梦: ").split()]
    player_pokemon = [player_team[i] for i in choices]
    enemy_pokemon = random.sample(enemy_team, 3)

    print("\n请选择你的宝可梦:")
    for i, pokemon in enumerate(player_pokemon, 1):
        print(f"{i}. {pokemon.name}({pokemon.element}属性)")

    player_choice = int(input("输入数字选择你的宝可梦: ")) - 1
    player_current = player_pokemon[player_choice]
    enemy_current = random.choice(enemy_pokemon)

    while not player_current.is_faint() and not enemy_current.is_faint():
        print(f"\n你的 {player_current.name} 的技能:")
        for i, move