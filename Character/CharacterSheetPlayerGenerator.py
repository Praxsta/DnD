import json
import random

from CharacterSheet import BaseCharacterProfileSheet
from Enums import Personality, Language, Item


class CharacterProfile(BaseCharacterProfileSheet):
    """This is primarily used as an example of how to create PLAYABLE characters"""

    def __init__(self, name=None, personality=None):

        if name is None:
            self.__NAME = self.name_generator()
        else:
            self.__NAME = name

        if personality is None:
            # Sorts the Personality Enums into a list and picks one at random
            self.__PERSONALITY = random.choice(list(Personality))
        else:
            self.__PERSONALITY = personality

        super().__init__(name=self.__NAME,
                         personality=self.__PERSONALITY,
                         languages=[Language.ABYSSAL, Language.COMMON],
                         expertise="pee pee poo poo",
                         inventory=[Item.WEAPON.SWORD, Item.FOOD.APPLE, Item.TOOL.THIEVES_TOOL])

    @staticmethod
    def name_generator():
        """Uses the names json to generate a name at random"""
        with open("Names.json") as fp:
            list_of_names = json.load(fp)
            name = ""

            # Determine how many names the full name is to have.
            number_of_names = random.randint(1, 4)

            for i in range(number_of_names):
                # Pick a name at random
                name += list_of_names[random.randint(0, len(list_of_names) - 1)]

                # Add a spacing if it's not the last name
                if i + 1 < number_of_names:
                    name += " "
        return name


if __name__ == '__main__':
    ch_char = CharacterProfile()
    print(
        f"{ch_char.name} is {ch_char.personality} with an expertise of {ch_char.expertise} has an inventory of: {ch_char.inventory[0].name}")
