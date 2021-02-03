class StatBlock:
    def __init__(self):
        # these assignments will call each of the scripts for their respective stats
        # they are assigning dummy vales just to check functionality
        self.name = 'test creature'
        self.level = 7

        # these represent modifiers, not raw stats
        self.str = 4
        self.dex = 5
        self.con = 3
        self.int = -4
        self.wis = 1
        self.cha = -2
        
        self.perception = 18

        self.senses = [('low-light vision', 120), ('scent', 0)]  # ('senseType', range:int) 0 for no range

        self.languages = ['Aklo','Abyssal']

        # should skills be implemented as a class?
        self.skills = [('Acrobatics', 20), ('Occultism', 7)]  # should be in the form ('skill name', bonus:int) [('acrobatics', 23), ('diplomacy', 18)]

        # items should just be names; ac and damage are already factored into creation process
        # any items carried by the monster are purely for flavor
        self.items = ['The shiniest shiny', 'The second shiniest shiny']

        self.ac = 23

        self.will = 12
        self.reflex = 18
        self.fortitude = 12

        self.hp = 115
        
        # immunities can just be a list of strings
        self.immunities = []

        # resistances should be in the form ('name', amount:int)
        # there should be some checking in place to ensure that resistances aren't listed for types
        # that the creature is immune to. check will have to take place after all resistances and
        # immunities have been added
        self.resistances = [('fire', 5)]

        self.speeds = [('walk', 25), ('swim', 35)]  # ('movementType', distance:int)

        self.attackBonus = 18
        self.attackDamage = (2,8,8)  # in the form (numberOfDice:int, sidesOfDie:int, flatAmound:int), (2, 6, 5) represents 2d6+5

        self.isSpellCaster = False  # boolean, the following few variables will only be set and rendered if this flag is set to on
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

        # abilities can probably just have a function to pull rules text from a database and
        # put it into the stat block when everything gets rendered
        self.abilityList = []

    def getDamage(self):
        return (str(self.attackDamage[0]) + 'd' + str(self.attackDamage[1]) + '+' + str(self.attackDamage[2]))

    def render(self):
        renderString = ""
        # just so i don't forget to do this and kick myself later

        # render some stuff

        if self.isSpellCaster:
            pass
            # render spell stuff
        
        # render other stuff

