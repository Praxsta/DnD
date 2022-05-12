from types import BuiltinMethodType
from Behaviours import Behaviour
import random

class CharacterProfileSheet:
    def __init__(self, name: str, behaviour: Behaviour = None) -> None:
        """
        Character Sheet containing the traits of a character.
        :param name: Name of the Character
        :param behaviour: Behaviour type to define Character's behaviour
        """

        # Name of character
        self.__NAME = name

        # If behaviour hasn't been assigned, give it a random one.
        if behaviour == None:
            self.__BEHAVIOUR = random.choice(list(Behaviour))
        else:
            self.__BEHAVIOUR = behaviour

    @property
    def behaviour(self):
        return self.__BEHAVIOUR.name

    @property
    def name(self):
        return str(self.__NAME)


# To run the code. This should be removed but is left here as an example
if __name__ == "__main__":
    char = CharacterProfileSheet(name="Hairy Piles")
    print(f"{char.name} is {char.behaviour}")