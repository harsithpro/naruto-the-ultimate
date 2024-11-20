import random
import time

# Player class
class Player:
    def __init__(self):
        self.name = "Naruto"
        self.hp = 150  # Updated Naruto's health to 150
        self.jutsu_points = 3  # Number of Jutsu available
        self.attacks = {
            "rasengan": 30,
            "rasenshuriken": 50,
            "shadow_clone_throw_kunai": 25,  # Shadow Clone + Kunai combined
        }

    def attack(self, attack_type):
        if attack_type == "rasengan":
            return self.attacks["rasengan"]
        elif attack_type == "rasenshuriken":
            return self.attacks["rasenshuriken"]
        elif attack_type == "shadow_clone_throw_kunai":
            return self.attacks["shadow_clone_throw_kunai"]

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} took {damage} damage. HP remaining: {self.hp}")

    def heal(self):
        heal_amount = random.randint(20, 40)  # Heal amount between 20 and 40
        self.hp += heal_amount
        if self.hp > 150:  # Ensure health doesn't go above 150
            self.hp = 150
        print(f"{self.name} healed for {heal_amount}. HP is now {self.hp}.")

# Enemy class
class Enemy:
    def __init__(self, name, hp, poison=False, dodge_chance=0):
        self.name = name
        self.hp = hp
        self.poison = poison  # Whether the enemy can poison the player
        self.dodge_chance = dodge_chance  # Chance to dodge attacks

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} took {damage} damage. HP remaining: {self.hp}")

    def attack(self, player):
        # If enemy has poison, apply poison damage
        if self.poison:
            poison_damage = random.randint(5, 10)
            print(f"{self.name} poisons Naruto for {poison_damage} damage!")
            player.take_damage(poison_damage)
        
        # If enemy has dodge chance, it might evade an attack
        if random.random() < self.dodge_chance:
            print(f"{self.name} dodged your attack!")
            return 0  # Attack missed

        # Otherwise, normal attack
        enemy_damage = random.randint(10, 30)
        print(f"{self.name} attacks Naruto for {enemy_damage} damage.")
        return enemy_damage

# Function to generate random enemies with special abilities
def generate_enemy():
    enemies = [
        Enemy("Obito", 120),  # Obito with 120 HP
        Enemy("Kaguya", 250),  # Kaguya with 250 HP
        Enemy("Pain", 150),
        Enemy("Madara", 200)
    ]
    return random.choice(enemies)

# Main game loop
def game():
    player = Player()
    print("Welcome to the Naruto Jutsu Battle Game!\n")
    time.sleep(1)
    
    while player.hp > 0:
        print("\nCurrent HP:", player.hp)
        enemy = generate_enemy()
        print(f"\nA wild {enemy.name} appears with {enemy.hp} HP!")
        
        while enemy.hp > 0:
            print("\nChoose your action:")
            print("1. Rasengan")
            print("2. Rasenshuriken")
            print("3. Shadow Clone Throw Kunai")
            print("4. Heal")  # New Heal option

            action = input("\nEnter the number of your action: ")

            if action == "1":
                damage = player.attack("rasengan")
                enemy.take_damage(damage)
            elif action == "2":
                damage = player.attack("rasenshuriken")
                enemy.take_damage(damage)
            elif action == "3":
                damage = player.attack("shadow_clone_throw_kunai")
                enemy.take_damage(damage)
            elif action == "4":
                player.heal()  # Call the heal method
                continue  # Skip the rest of the actions for this turn
            else:
                print("Invalid action. Please choose again.")
                continue

            if enemy.hp > 0:
                # Enemy attacks back
                enemy_damage = enemy.attack(player)
                player.take_damage(enemy_damage)

            if player.hp <= 0:
                print("\nYou have been defeated!")
                break
            if enemy.hp <= 0:
                print(f"\n{enemy.name} has been defeated!")
                break
        if player.hp <= 0:
            print("\nGame Over!")
            break

if __name__ == "__main__":
    game()
