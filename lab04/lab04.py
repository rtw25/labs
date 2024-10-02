class Item:
    def __init__(self, name: str, description: str = "", rarity: str = "common",  ):
        self.name = name
        self.description = description
        self.rarity = rarity
        self._ownership = ""

    def pick_up(self, character: str) -> str:
        self._ownership = character
        return f"{self.name} is now owned by {character}"

    def throw_away(self) -> str:
        self._ownership = ""
        return f"{self.name} has been thrown away"

    def use(self) -> str:
        if self._ownership:
            return f"{self.name} is used"
        return ""

    def __str__(self) -> str:
        return f"Item(name={self.name}, description={self.description}, rarity={self.rarity}, ownership={self._ownership})"

class Weapon(Item):
    def __init__(self, name: str, damage: int, weapon_type: str, rarity: str = "common", description: str = ""):
        super().__init__(name=name, rarity=rarity)
        self.damage = damage
        self.weapon_type = weapon_type
        self.is_equipped = False
        self.attack_modifier = 1.15 if self.rarity == "legendary" else 1.0

    def equip(self, character_name: str) -> str:
        self.is_equipped = True
        return f"{self.name} is equipped by {character_name}."

    def use(self) -> str:
        if self.is_equipped and self._ownership:
            total_damage = self.damage * self.attack_modifier
            return f"{self.name} is used, dealing {total_damage} damage"
        return super().use()


class Shield(Item):
    def __init__(self, name: str, defense: int, broken: bool = False, rarity: str = "common", description: str = ""):
        super().__init__(name, rarity=rarity)
        self.defense = defense
        self.broken = broken
        self.is_equipped = False
        self.defense_modifier = 1.10 if self.rarity == "legendary" else 1.0

    def equip(self, character_name: str) -> str:
        self.is_equipped = True
        return f"{self.name} is equipped by {character_name}."

    def use(self) -> str:
        if self.is_equipped and self._ownership:
            total_defense = self.defense * self.defense_modifier * (0.5 if self.broken else 1.0)
            return f"{self.name} is used, blocking {total_defense} damage"
        return super().use()
class Potion(Item):
    def __init__(self, name: str, potion_type: str, value: int, effective_time: int, rarity: str = "common", description: str = ""):
        super().__init__(name, rarity=rarity)
        self.potion_type = potion_type
        self.value = value
        self.effective_time = effective_time
        self.empty = False

    def use(self, character_name: str) -> str:
        if not self.empty:
            self.empty = True
            if self.potion_type == 'attack':
                return f"{character_name} used {self.name}, and attack increase {self.value} for {self.effective_time}s."
            elif self.potion_type == 'defense':
                return f"{character_name} used {self.name}, and defense increase {self.value} for {self.effective_time}s."
            elif self.potion_type == 'hp':
                return f"{character_name} used {self.name}, restoring {self.value} health."
        return ""

    @classmethod
    def from_ability(cls, name: str, owner: str, potion_type: str):
        return cls(name, potion_type, 50, 30, rarity="common")


# weapon example

long_bow = Weapon(name='Belthronding', damage=5000, weapon_type='bow', rarity='legendary')
print(long_bow.pick_up('Beleg'))
print(long_bow.equip('Beleg'))
print(long_bow.use())

# shield example

broken_pot_lid = Shield(name='Wooden Lid',description='A lid made of wood, useful in cooking. No one will choose it willingly for a shield', defense = 5, broken = True)
metal_shield = Shield(name='Metal Shield', description='A basic shield made of wood.', defense=10)
print(broken_pot_lid.pick_up("Beleg"))
print(broken_pot_lid.use())
print(broken_pot_lid.throw_away())
print(broken_pot_lid.use())

# potion example
attack_potion = Potion.from_ability(name='atk potion temp', owner='Beleg', potion_type='attack')
print(attack_potion.use('Beleg'))
print(attack_potion.use('Beleg'))



print(isinstance(long_bow, Item))
print(isinstance(broken_pot_lid, Shield))
print(isinstance(attack_potion, Weapon))

