from enum import Enum


class Weapon(Enum):
    SWORD = 0


class Tool(Enum):
    THIEVES_TOOL = 0,


class Food(Enum):
    APPLE = 0,


class Item:
    WEAPON = Weapon
    TOOL = Tool
    FOOD = Food

    # Kind of cheating here huehue
    @classmethod
    def types(cls):
        return Enum
        # return [value for name, value in vars(cls).items()]
