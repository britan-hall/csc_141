import random
import os

# Clear console
os.system('cls')

# Elemental advantage system
element_advantages = {
    'Fire': 'Earth',   # Fire is strong against Earth
    'Water': 'Fire',   # Water is strong against Fire
    'Earth': 'Air',    # Earth is strong against Air
    'Air': 'Water'     # Air is strong against Water
}

# Character class
class Character:
    def __init__(self, name, power_level, max_damage, element):
        self.name = name
        self.power_level = power_level
        self.max_damage = max_damage
        self.element = element
    
    def attack(self):
        """Performs an attack and returns the damage dealt."""
        return random.randint(0, self.max_damage)

    def take_damage(self, damage):
        """Reduces the power level based on damage taken."""
        self.power_level -= damage
        return self.power_level <= 0  # Returns True if the character is dead

    def calculate_damage(self, opponent):
        """Calculates damage considering elemental strengths and weaknesses, showing the multiplier."""
        base_damage = self.attack()
        multiplier = 1.0  # Default multiplier

        # Check for elemental advantage/disadvantage
        if element_advantages.get(self.element) == opponent.element:
            multiplier = 1.5
            print(f"\n[Advantage] {self.name}'s element ({self.element}) is strong against {opponent.name}'s element ({opponent.element})! Damage multiplier: x1.5")
        elif element_advantages.get(opponent.element) == self.element:
            multiplier = 0.75
            print(f"\n[Disadvantage] {self.name}'s element ({self.element}) is weak against {opponent.name}'s element ({opponent.element})! Damage multiplier: x0.75")
        
        return int(base_damage * multiplier)

# Function to get player element choice
def get_player_element():
    elements = ['Fire', 'Water', 'Earth', 'Air']
    while True:
        print("\nChoose your element:")
        print("1. Fire\n2. Water\n3. Earth\n4. Air")
        player_element = input("Enter the name of your element: ").capitalize()
        if player_element in elements:
            return player_element
        else:
            print("Invalid element. Please choose again.")

# Player chooses their element
player_element = get_player_element()

# Player character with selected element
player = Character('Player', 12, 7, player_element)

# Create superhero characters with elements
superheroes = [
    Character('Batman', 7, 5, 'Fire'),
    Character('Spiderman', 9, 7, 'Air'),
    Character('Hulk', 9, 8, 'Earth'),
    Character('Aquaman', 1, 3, 'Water'),
    Character('Ironman', 10, 6, 'Fire')
]

# Display the available superheroes and their elements
print('\nThe heroes in the arena are:')
for hero in superheroes:
    print(f"- {hero.name} (Power: {hero.power_level}, Max Damage: {hero.max_damage}, Element: {hero.element})")
print('\n')

# Select a random hero to fight
opponent = random.choice(superheroes)
print(f'You find yourself in the arena with {opponent.name}, who has a power level of {opponent.power_level} and an element of {opponent.element}!\n')

# Fight loop
choice = ''
while True:
    if choice == 'e':
        print(f"\nYou have left the arena, with {opponent.name} mocking you as you retreat.")
        break
    
    choice = input("Do you want to (e)scape or (f)ight?: ").lower()

    if choice == 'f':
        # Player attacks first, considering elemental advantage
        damage_to_opponent = player.calculate_damage(opponent)
        print(f"\nYou attack {opponent.name} and deal {damage_to_opponent} points of damage.")
        
        if opponent.take_damage(damage_to_opponent):
            print(f"\nYou defeated {opponent.name}!")
            break

        # Opponent attacks back, considering elemental advantage
        damage_to_player = opponent.calculate_damage(player)
        print(f"{opponent.name} attacks you and deals {damage_to_player} points of damage.")
        
        if player.take_damage(damage_to_player):
            print("\nYou have been defeated!")
            break

print("\nThanks for playing!")
