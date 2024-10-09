class Item:
    def __init__(self, name: str, description: str = "", rarity: str = "common"):
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
        return ""  # Return an empty string to prevent item details from printing


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

    def __str__(self) -> str:
        if self.rarity == "legendary":
            return f"*** {self.name.upper()} *** - A legendary {self.weapon_type} with {self.damage} damage!"
        return super().__str__()


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


class Inventory:
    def __init__(self, owner: str = None):
        self.owner = owner
        self.items = []

    def add_item(self, item: Item) -> None:
        self.items.append(item)
        item.pick_up(self.owner)

    def drop_item(self, item: Item) -> None:
        if item in self.items:
            self.items.remove(item)
            item.throw_away()

    def view(self, item_type: str = None) -> None:
        if item_type:
            filtered_items = [item for item in self.items if isinstance(item, Shield) and item_type == 'shield']
        else:
            filtered_items = self.items
        return [str(item) for item in filtered_items]

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, item: Item):
        return item in self.items


# example usage
master_sword = Weapon(name='Master Sword', damage=300, weapon_type='sword', rarity='legendary')
belthronding = Weapon(name='Belthronding', damage=500, weapon_type='bow', rarity='legendary')
muramasa = Weapon(name='Muramasa', damage=580, weapon_type='katana', rarity='legendary')
gungnir = Weapon(name='Gungnir', damage=290, weapon_type='spear', rarity='legendary')
broken_pot_lid = Item(name='Broken Pot Lid')
hp_potion = Item(name='HP Potion')
round_shield = Shield(name='Round Shield', defense=50, rarity='common')

beleg_backpack = Inventory(owner='Beleg')


beleg_backpack.add_item(belthronding)
beleg_backpack.add_item(hp_potion)
beleg_backpack.add_item(master_sword)
beleg_backpack.add_item(broken_pot_lid)
beleg_backpack.add_item(muramasa)
beleg_backpack.add_item(gungnir)
beleg_backpack.add_item(round_shield)


shields_view = beleg_backpack.view(item_type='shield')
print("\n".join(shields_view))


all_items_view = beleg_backpack.view()
print("\n".join(all_items_view))


beleg_backpack.drop_item(broken_pot_lid)


if master_sword in beleg_backpack:
    print(master_sword.equip('Beleg'))
    print(master_sword)
    print(master_sword.use())

for item in beleg_backpack:
    if isinstance(item, Weapon):
        print(item)

