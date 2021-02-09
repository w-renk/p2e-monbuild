from .name import SelectName
from .level import SelectLevel
from .statArrays import SelectStatArray
from .templates import SelectTemplateGraft
from .types import SelectTypes

class StatBlock:
    def __init__(self):
        # these assignments will call each of the scripts for their respective stats
        # most are assigning dummy values just to check functionality

        self.name = "";
        SelectName(self)  # done

        self.levelConstraint = 'none'
        self.template = None
        self.types = []
        SelectTemplateGraft(self)  # done

        self.level = 6
        SelectLevel(self) # done

        self.types = []  # ['Animal', 'Aberration'] # SelectTypes()
        SelectTypes(self)  # done

        self.alignment = 'N'
        # TODO
        #SelectAlignment(self)

        self.isMindless = False
        # TODO
        #SetMindless(self)

        # modifiers are going to be handled as strings to make the render function easier
        self.str, self.dex, self.con, self.int, self.wis, self.cha = ('0','0','0','0','0','0')
        SelectStatArray(self)  # done
        
        self.perception = 0
        # TODO
        #SetPerception(self)

        self.senses = [('low-light vision', 0), ('scent', 30)]  # ('senseType', range:int) 0 for no range
        # TODO
        #SelectSenses(self)

        self.languages = ['Aklo','Abyssal']
        # TODO
        #SelectLanguages(self)

        # should skills be implemented as a class?
        self.skills = [('Acrobatics', 20), ('Occultism', 7)]  # should be in the form ('skill name', bonus:int) [('acrobatics', 23), ('diplomacy', 18)]
        # TODO
        #SelectSkills(self)

        # items should just be names; ac and damage are already factored into creation process
        # any items carried by the monster are purely for flavor
        self.items = ['The shiniest shiny', 'The second shiniest shiny']
        # TODO
        #SelectItems(self)

        self.ac = 23
        # TODO
        #SetAC(self)

        self.fortitude = 12
        self.reflex = 18
        self.will = 12
        # TODO
        #SelectSaves(self)

        self.hp = 115
        # TODO
        #SetHP(self)
        
        # immunities can just be a list of strings
        self.immunities = []
        # TODO
        #SelectImmunities(self)

        # resistances should be in the form ('name', amount:int)
        # there should be some checking in place to ensure that resistances aren't listed for types
        # that the creature is immune to. check will have to take place after all resistances and
        # immunities have been added
        self.resistances = [('fire', 5), ('piercing', 5)]
        # TODO
        #SelectImmunities(self)

        self.weaknesses = [('cold', 10)]
        # TODO
        #SelectWeaknesses(self)

        self.speeds = [('walk', 25), ('swim', 35)]  # ('movementType', distance:int)
        # TODO
        #SetSpeeds(self)

        # change attacks to an array of attacks [(attackName, bonus, damage, type), (name, bonud, damage, type)]
        # make sure render() changes to reflect this as well
        self.attackBonus = 18
        self.attackDamage = (2,8,8)  # in the form (numberOfDice:int, sidesOfDie:int, flatAmound:int), (2, 6, 5) represents 2d6+5
        self.damageType = 'slashing'
        # TODO
        #SelectAttacks(self)

        self.isSpellCaster = False  # boolean, the following few variables will only be set and rendered if this flag is set to on
        # TODO
        #SetSpellCasting(self)
        # add all of the following to SetSpellCasting
        if self.isSpellCaster:
            self.spellDC = 0
            self.spellAttack = 0
            self.casterLevel = int(self.level / 2)
            # list of names should be fine for this
            self.spellList = []
            self.spellSlots = {
                0: 0,
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
                7: 0,
                8: 0,
                9: 0,
                10: 0
            }
            self.preparedSpells = []  # in form ('name', numberPrepared:int), ('magic missile', 3) means 3 prepared casts of magic missile
            self.innateSpells = []  # in form ('name', 'usage') e.g., ('magic missile', 'at will'), ('shocking grasp', '3/day')

        # best way to handle this is probably to have the SelectAbilities() return just a list to here
        # then pull rules text for known abilities from a lookup table
        # for unknown abilities, either don't include rules text (with the intent being the user will add it after rendering text)
        # or set up a prompt for each unknown ability to allow the user to enter custom text for it
        self.abilityList = [('test ability name', 'this is some rules text for that ability'),
                            ('second test ability name', 'this rules text is worse than the first')]
        # TODO
        #EnterAbilities(self)

    def renderPlainText(self):
        renderString = ""
        # just so i don't forget to do this and kick myself later

        # render some stuff

        renderString += self.name
        renderString += "                  "
        renderString += "Creature " + str(self.level)
        renderString += "\n"

        renderString += self.alignment

        for type in self.types:
            renderString += "  " + type

        renderString += "\n"

        renderString += "Perception +" + str(self.perception) + ";"

        for sense in self.senses:
            renderString += " " + sense[0]
            if (sense[1] != 0): renderString += " " + str(sense[1]) + " feet"
            renderString += ","
        
        renderString = renderString[:-1]  # remove trailing comma from last for loop

        renderString += "\n"

        renderString += "Skills"

        for skill in self.skills:
            renderString += ' ' + skill[0] + " +" + str(skill[1]) + ','

        renderString = renderString[:-1]

        renderString += '\n'

        renderString += "Str " + str(self.str) + ','
        renderString += " Dex " + str(self.dex) + ','
        renderString += " Con " + str(self.con) + ','
        renderString += " Int " + str(self.int) + ','
        renderString += " Wis " + str(self.wis) + ','
        renderString += " Cha " + str(self.cha)

        renderString += '\n'

        renderString += "Items"

        for item in self.items:
            renderString += ' ' + item + ','

        renderString = renderString[:-1]

        renderString += '\n\n'
        renderString += "================================================================"
        renderString += '\n\n'

        renderString += "AC " + str(self.ac) + '; '
        renderString += "Fort " + str(self.fortitude) + ', '
        renderString += "Reflex " + str(self.reflex) + ', '
        renderString += "Will " + str(self.will)

        renderString += '\n'

        renderString += 'HP ' + str(self.hp)

        if self.immunities:
            renderString += "; Immunities"
            for imm in self.immunities:
                renderString += ' ' + imm + ','
            renderString = renderString [:-1]

        if self.resistances:
            renderString += "; Resistances"
            for res in self.resistances:
                renderString += ' ' + res[0] + ' ' + str(res[1]) + ','
            renderString = renderString [:-1]


        if self.weaknesses:
            renderString += "; Weaknesses"
            for weak in self.weaknesses:
                renderString += ' ' + weak[0] + ' ' + str(weak[1]) + ','
            renderString = renderString[:-1]

        # paizo statblocks have attack of opportunity listed here

        renderString += '\n\n'
        renderString += "================================================================"
        renderString += '\n\n'

        renderString += "Speed"

        for speed in self.speeds:
            renderString += ' ' + speed[0] + ': ' + str(speed[1]) + ' feet,'
        renderString = renderString[:-1]

        renderString += '\n'

        renderString += "Strike +" + str(self.attackBonus)
        if self.attackBonus >= 6:
            renderString += " [+" + str(self.attackBonus - 5)
            if self.attackBonus >= 11:
                renderString += "/+" + str(self.attackBonus - 10)
            renderString += ']'
        renderString += ', Damage ' + str(self.attackDamage[0]) + 'd' + str(self.attackDamage[1]) + '+' + str(self.attackDamage[2]) + ' ' + self.damageType
        
        renderString += "\n"

        if self.abilityList:
            for ability in self.abilityList:
                renderString += ability[0] + ' ' + ability[1] + '\n'
            renderString = renderString [:-1]

        renderString += '\n\n'
        renderString += "================================================================"
        renderString += '\n\n'

        if self.isSpellCaster:
            pass

        return renderString

