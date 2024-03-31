from abc import ABC, abstractmethod
from random import randint


class Dice(ABC):
    @abstractmethod
    def roll(self):
        raise NotImplementedError


class D4(Dice):
    def roll(self):
        output = randint(1, 4)
        return output


class D6(Dice):
    def roll(self):
        output = randint(1, 6)
        return output


class D8(Dice):
    def roll(self):
        output = randint(1, 4)
        return output


class D10(Dice):
    def roll(self):
        output = randint(1, 4)
        return output


class D12(Dice):
    def roll(self):
        output = randint(1, 4)
        return output


class D20(Dice):
    def roll(self):
        output = randint(1, 4)
        return output
