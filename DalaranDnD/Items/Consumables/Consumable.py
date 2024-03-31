from abc import ABC
from DalaranDnD.Dice import Dice
from typing import List


class Consumable(ABC):

    def drink(self):
        raise NotImplementedError


class PotionOfHealing(Consumable):
    def  __init__(self, dice: [Dice], modifier: int):
        self.dice= dice
        self.modifier= modifier

    def drink(self):
        total=0
        for dice in self.dice:
            calc=dice.roll()
            print("dice rolled is ", calc)
            total=total+calc

        print("The total rolled is ", total)
        a = ["HEALTH", total + self.modifier]
        print(a)
        return (a)

# dice4 = Dice.D4()
# dice6 = Dice.D6()
# dice8 = Dice.D8()
# lesserpotionofhealing = PotionOfHealing(dice=[dice4, dice4], modifier=2)
# lesserpotionofhealing.drink()
#
# greaterpotionofhealing = PotionOfHealing(dice=[dice6, dice4], modifier=4)
# greaterpotionofhealing.drink()
#
# superiorpotionofhealing = PotionOfHealing(dice=[dice8,dice8], modifier=6)
# superiorpotionofhealing.drink()
