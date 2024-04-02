from enum import Enum
from typing import List


class ClassHP(Enum):
    """
    Class types and their base HP at Level 1.
    """
    SORCERER = 6,
    WIZARD = 6,
    ARTIFICER = 8,
    BARD = 8,
    CLERIC = 8,
    DRUID = 8,
    MONK = 8,
    ROGUE = 8,
    WARLOCK = 8,
    FIGHTER = 10,
    PALADIN = 10,
    RANGER = 10,
    BARBARIAN = 12,

    @classmethod
    def list(cls) -> List:
        return list(map(lambda c: c.value, cls))

    @classmethod
    def __len__(cls) -> int:
        return len(cls)
