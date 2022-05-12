from enum import Enum
from typing import List


class Behaviour(Enum):
    """
    Behaviour Enums to define what sort of Behaviour an entity is to have.
    """
    AGGRESSION = 0
    BRAWLER = 1
    CAUTIOUS = 2
    DISHONEST = 3
    EASY_GOING = 4
    FARSIGHTED = 5
    HONESTY = 6
    ILLITERACY = 7
    POLITE = 8
    RELENTLESS = 9
    SUSPICIOUS = 10
    SLOW = 11
    UNCIVILIZED = 12

    @classmethod
    def list(cls) -> List:
        return list(map(lambda c: c.value, cls))

    @classmethod
    def __len__(cls) -> int:
        return len(cls)