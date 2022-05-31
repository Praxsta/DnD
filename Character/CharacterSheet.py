from Enums import Personality, Language, Item
from typing import List, Dict
from abc import ABC


# dannywashere


class BaseCharacterProfileSheet(ABC):
    def __init__(self, name: str, personality: Personality,
                 languages: List[Language],
                 expertise,
                 inventory: List[Item.types()],
                 saving_throw_strength=0,
                 saving_throw_dexterity=0,
                 saving_throw_constitution=0,
                 saving_throw_intelligence=0,
                 saving_throw_wisdom=0,
                 saving_throw_charisma=0,
                 __strength=0,
                 __dexterity=0,
                 __constitution=0,
                 __intelligence=0,
                 __wisdom=0,
                 __charisma=0,
                 acrobatics=0,
                 animal_handling=0,
                 arcana=0,
                 athletics=0,
                 deception=0,
                 history=0,
                 insight=0,
                 intimidation=0,
                 investigation=0,
                 medicine=0,
                 nature=0,
                 perception=0,
                 performance=0,
                 persuasion=0,
                 religion=0,
                 sleight_of_hand=0,
                 stealth=0,
                 survival=0,
                 proficiencies=None,
                 current_hp=0,
                 temp_hp=0,
                 hit_dice_type="DICE ENUM GOES HERE",
                 death_saves=None,
                 special_attack_move="Sneak Attack",
                 traits: Dict = None,
                 ) -> None:
        """
        Character Profile Sheet
        :param name: Name of Character
        :param personality: Personality Enum
        :param languages: List of Language Enums
        :param expertise: string of what the expertise is
        :param saving_throw_strength: int of saving throw for when you really fuck up
        :param saving_throw_dexterity: int of saving throw for when you really fuck up
        :param saving_throw_constitution: int of saving throw for when you really fuck up
        :param saving_throw_intelligence: int of saving throw for when you really fuck up
        :param saving_throw_wisdom: int of saving throw for when you really fuck up
        :param saving_throw_charisma: int of saving throw for when you really fuck up
        :param __strength: int of strength
        :param __dexterity: int of dex
        :param __constitution: int of constitution
        :param __intelligence: int of intelligence
        :param __wisdom: int
        :param __charisma: int
        :param acrobatics: int
        :param animal_handling: int
        :param arcana: int
        :param athletics: int
        :param deception: int
        :param history: int
        :param insight: int
        :param intimidation: int
        :param investigation: int
        :param medicine: int
        :param nature: int
        :param perception: int
        :param performance: int
        :param persuasion: int
        :param religion: int
        :param sleight_of_hand: int
        :param stealth: int
        :param survival: int
        :param proficiencies: int
        :param current_hp: int
        :param temp_hp: int
        :param hit_dice_type: Dice Enum
        :param death_saves: #TODO work out whether this needs to be in here? I think its defaults to Fail,F,F vs Success,S,S
        :param inventory: List of Item Values which are Enums Eg Item.Weapon.SWORD
        :param special_attack_move: String of the specials you can do
        :param traits: dictionary of special traits (str).
        """

        # Name of character
        self.__NAME = name
        self.__PERSONALITY = personality

        # Saving Throws for if you really fuck up.
        self.saving_throw_strength = saving_throw_strength
        self.saving_throw_dexterity = saving_throw_dexterity
        self.saving_throw_constitution = saving_throw_constitution
        self.saving_throw_intelligence = saving_throw_intelligence
        self.saving_throw_wisdom = saving_throw_wisdom
        self.saving_throw_charisma = saving_throw_charisma

        #######################
        self.__strength = __strength
        self.__dexterity = __dexterity
        self.__constitution = __constitution
        self.__intelligence = __intelligence
        self.__wisdom = __wisdom
        self.__charisma = __charisma

        self.acrobatics = acrobatics
        self.animal_handling = animal_handling
        self.arcana = arcana
        self.athletics = athletics
        self.deception = deception
        self.history = history
        self.insight = insight
        self.intimidation = intimidation
        self.investigation = investigation
        self.medicine = medicine
        self.nature = nature
        self.perception = perception
        self.performance = performance
        self.persuasion = persuasion
        self.religion = religion
        self.sleight_of_hand = sleight_of_hand
        self.stealth = stealth
        self.survival = survival

        # Generally consists of skills, ability to wield stuff etc.
        # eg light armour, hand crossbows, rapiers, thieves tools, playing cards, carpenters tools
        self.proficiencies = proficiencies

        # list of languages
        self.languages: List[Language] = languages

        # Generally a perk, eg "When you make a Dex check, or using thieves tools, your proficiency bonus is doubled"
        self.expertise = expertise

        self.current_hp = current_hp
        self.temp_hp = temp_hp

        # Dice Enum goes here
        self.hit_dice_type = hit_dice_type

        # 3 successes vs 3 fails
        self.death_saves = death_saves

        self.inventory: List[Item.types()] = inventory

        # eg "Sneak Attack"
        self.special_attack_move = special_attack_move

        # eg [{"thieves can't": "you can detect symbols", "Brave": "immunity to Frightened"}]
        self.traits = traits

    @property
    def personality(self):
        return self.__PERSONALITY.name

    @property
    def name(self):
        return str(self.__NAME)
