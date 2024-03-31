from abc import ABC
from DalaranDnD.Dice import Dice


class Consumable(ABC):

    def drink(self):
        raise NotImplementedError


class PotionOfHealing(Consumable):
    def __init__(self, dice: [Dice], modifier: int):
        self.dice = dice
        self.modifier = modifier

    def drink(self):
        total = 0
        for dice in self.dice:
            calc = dice.roll()
            total = total + calc

        print("Hp gained: ", total + self.modifier)
        output = ["HEALTH", total + self.modifier]
        return output
