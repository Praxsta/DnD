from types import BuiltinMethodType
from Behaviours import Behaviour
import random
#dannywashere

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
        if behaviour is None:
            # Sorts the Behaviour Enums into a list and picks one at random
            self.__BEHAVIOUR = random.choice(list(Behaviour))
        else:
            self.__BEHAVIOUR = behaviour

        # TODO Create a character generator script where it does Behaviour = random.choice etc rather than putting it
        #   in here

        # Saving Throws for if you really fuck up.
        self.saving_throw_strength = 0
        self.saving_throw_dexterity = 0
        self.saving_throw_constitution = 0
        self.saving_throw_intelligence = 0
        self.saving_throw_wisdom = 0
        self.saving_throw_charisma = 0

        #######################

        self.__strength = 0
        self.__dexterity = 0
        self.__constitution = 0
        self.__intelligence = 0
        self.__wisdom = 0
        self.__charisma = 0

        self.acrobatics = 0
        self.animal_handling = 0
        self.arcana = 0
        self.athletics = 0
        self.deception = 0
        self.history = 0
        self.insight = 0
        self.intimidation = 0
        self.investigation = 0
        self.medicine = 0
        self.nature = 0
        self.perception = 0
        self.performance = 0
        self.persuasion = 0
        self.religion = 0
        self.sleight_of_hand = 0
        self.stealth = 0
        self.survival = 0

        self.proficiencies = []

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
