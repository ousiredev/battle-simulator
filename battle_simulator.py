class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.poison_turns = 0
    
    def attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        target.hp -= self.attack_power

    def apply_poison(self):
        if self.poison_turns > 0:
            print(f"{self.name} takes 5 poison damage!")
            self.hp -= 5
            self.poison_turns -= 1

    def is_alive(self):
        return self.hp > 0
    
class Warrior(Character):
    def slash(self, target):
        print(f"{self.name} slashes {target.name} for {self.attack_power} with a sword")
        target.hp -= self.attack_power

    def stab(self, target):
        print(f"{self.name} stabs {target.name} for {self.attack_power} with a poisoned dagger")
        target.hp -= self.attack_power
        target.poison_turns = 3



class Mage(Character):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power)
        self.mana = mana

    def cast_spell(self, target):
        if self.mana >= 10:
            print(f"{self.name} casts Fireball at {target.name}!")
            target.hp -= 20
            self.mana -= 10
        else:
            print(f"{self.name} has no mana left !")

class Enemy(Character):
    def taunt(self):
        print(f"{self.name} says: You're too weak to fight me!")
    
    def bite(self, target):
        print(f"{self.name} bits {target.name} for 8 damage!")
        target.hp -= 8

warrior = Warrior("Leon", 100, 15)
mage = Mage("Zara", 80, 10, 30)
enemy = Enemy("Goblin", 60, 8)

print("Battle start!")

turn = 1
while warrior.is_alive() and enemy.is_alive():
    print(f"\n--- Turn {turn} ---")

    if turn % 2 == 1:
        if turn % 4 == 1:
            warrior.slash(enemy)
        else:
            warrior.stab(enemy)
    else:
        mage.cast_spell(enemy)

    enemy.apply_poison()

    if not enemy.is_alive():
        print(f"{enemy.name} is defeated!")
        break

    enemy.bite(warrior)

    if not warrior.is_alive():
        print(f"{warrior.name} is defeated!")
        break

    # Print current HP
    print(f"{warrior.name} HP: {warrior.hp}")
    print(f"{mage.name} HP: {mage.hp}")
    print(f"{enemy.name} HP: {enemy.hp}")

    turn += 1

print("\nBattle over!")