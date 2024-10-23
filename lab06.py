import json

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

    def to_json(self) -> dict:
        """Converts Item to a JSON-serializable dict."""
        return {
            'name': self.name,
            'description': self.description,
            'rarity': self.rarity,
            'ownership': self._ownership
        }

    @classmethod
    def from_json(cls, data: dict):
        """Creates an Item instance from a JSON dictionary."""
        item = cls(name=data['name'], description=data['description'], rarity=data['rarity'])
        item._ownership = data.get('ownership', "")
        return item

    def __str__(self) -> str:
        return ""  # returns an empty string to prevent item details from printing


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

    def to_json(self) -> dict:
        """Converts Weapon to a JSON-serializable dict."""
        data = super().to_json()
        data.update({
            'damage': self.damage,
            'weapon_type': self.weapon_type,
            'is_equipped': self.is_equipped
        })
        return data

    @classmethod
    def from_json(cls, data: dict):
        """Creates a Weapon instance from a JSON dictionary."""
        weapon = cls(name=data['name'], damage=data['damage'], weapon_type=data['weapon_type'], rarity=data['rarity'])
        weapon._ownership = data.get('ownership', "")
        weapon.is_equipped = data.get('is_equipped', False)
        return weapon

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

    def to_json(self) -> dict:
        """Converts Shield to a JSON-serializable dict."""
        data = super().to_json()
        data.update({
            'defense': self.defense,
            'broken': self.broken,
            'is_equipped': self.is_equipped
        })
        return data

    @classmethod
    def from_json(cls, data: dict):
        """Creates a Shield instance from a JSON dictionary."""
        shield = cls(name=data['name'], defense=data['defense'], broken=data['broken'], rarity=data['rarity'])
        shield._ownership = data.get('ownership', "")
        shield.is_equipped = data.get('is_equipped', False)
        return shield


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

    def to_json(self) -> dict:
        """Converts Inventory to a JSON-serializable dict."""
        return {
            'owner': self.owner,
            'items': [item.to_json() for item in self.items]
        }

    @classmethod
    def from_json(cls, data: dict):
        """Creates an Inventory instance from a JSON dictionary."""
        inventory = cls(owner=data['owner'])
        for item_data in data['items']:
            item_type = item_data.get('weapon_type') or item_data.get('defense')
            if 'weapon_type' in item_data:
                item = Weapon.from_json(item_data)
            elif 'defense' in item_data:
                item = Shield.from_json(item_data)
            else:
                item = Item.from_json(item_data)
            inventory.add_item(item)
        return inventory

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, item: Item):
        return item in self.items


# json encoder for inventory
def custom_inventory_encoder(obj):
    if isinstance(obj, Inventory):
        return obj.to_json()
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")


# example
master_sword = Weapon(name='Master Sword', damage=300, weapon_type='sword', rarity='legendary')
broken_pot_lid = Item(name='Broken Pot Lid')
round_shield = Shield(name='Round Shield', defense=50, rarity='common')

# create an inventory and add items
beleg_backpack = Inventory(owner='Beleg')
beleg_backpack.add_item(master_sword)
beleg_backpack.add_item(broken_pot_lid)
beleg_backpack.add_item(round_shield)

# serialize inventory to json
inventory_json = json.dumps(beleg_backpack.to_json(), indent=4)
print(inventory_json)

# deserialize inventory from json
deserialized_inventory = Inventory.from_json(json.loads(inventory_json))
print(deserialized_inventory.owner)  # should print 'Beleg'
