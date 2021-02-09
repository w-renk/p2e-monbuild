from os import stat
from .scripts import ClearScreen
from PyInquirer import prompt

def SelectStatArray(creature):
    # this is a goddamn mess, but it fucking works so whatever
    ClearScreen()
    if creature.isMindless or "Animal" in creature.types:
        print("You now have the option of using a preset stat array (listed below) or to make a custom array.\n\n")
        print('You have chosen to make your creature Mindless or have chosen the "Animal" type. Your options are limited due ' +
              'to the enforced Int value of -5 or -4, respectively.\n\n')
        print("Melee combatant: high (or extreme, at higher levels) Str, high Con\n\n" +
              "Ranged combatant: high (or extreme, at higher levels) Dex, high Wis\n\n")
        question = [
            {
                'type': 'list',
                'name': 'array',
                'message': 'Select One',
                'choices': [
                    'Make a creature with a custom stat array',
                    'Melee combatant',
                    'Ranged combatant'
                ]
            }
        ]
    else:
        print("You now have the option of using a preset stat array (listed below) or to make a custom array.\n")
        if "Beast" in creature.types:
            print('Please note that you have selected "Beast" as one of your creature\'s types. If you choose "Skill monkey" or "Spellcaster", '+
                  'it will override the default Int value of -3.')
        print("Melee combatant: high (or extreme, at higher levels) Str, high Con\n\n" +
        "Ranged combatant: high (or extreme, at higher levels) Dex, high Wis\n\n" +
        "Spellcaster(Int): high Dex and Wis, high (or extreme) Int, terrible Str and Con\n\n" + 
        "Spellcaster(Wis): high Dex, high (or extreme) Wis\n\n" + 
        "Spellcaster(Cha): high Dex and Wis, high (or extreme) Cha, terrible Str and Con\n\n" + 
        "Skill monkey: high Dex, Int, Wis and Cha, terrible Str and Con\n\n")


        # if you change the text of any of the choices in this prompt, be sure to change
        # the corresponding text in cases dictionary below
        question = [
            {
                'type': 'list',
                'name': 'array',
                'message': 'Select One',
                'choices': [
                    'Make a creature with a custom stat array',
                    'Melee combatant',
                    'Ranged combatant',
                    'Spellcaster(Int)',
                    'Spellcaster(Wis)',
                    'Spellcaster(Cha)',
                    'Skill monkey'
                ]
            }
        ]

    answer = prompt(question)
    #print(answer)

    # the following equations near enough reflect the math used to calculate the chart on page 59 of the Gamemastery Guide
    # theirs breaks the pattern in a couple places, i'm not overly concerned about it
    # the terrible calculation is extrapolated
    high = "+" + str(int((int(creature.level) + 2) * 9 / 26 + 3))
    ext = ("+" + str(int(int(creature.level) * 8 / 24 + 5))) if int(creature.level) > 0 else high
    mod = "+" + str(int((int(creature.level) + 2) * 7 / 26 + 2))
    low = "+" + str(int((int(creature.level) + 2) * 7 / 26))
    terr = "+" + str(int((int(creature.level) + 2) * 7 / 26 - 3))

    def _ranged():
        creature.str, creature.con, creature.wis, creature.cha = low, mod, high, mod
        creature.dex = ext if int(creature.level) > 10 else high
        creature.int = "-5" if creature.isMindless else ("-3" if "Beast" in creature.types else ("-4" if "Animal" in creature.types else low))

    def _melee():
        creature.dex, creature.con, creature.wis, creature.cha = low, high, mod, mod
        creature.str = ext if int(creature.level) > 10 else high
        creature.int = "-5" if creature.isMindless else ("-3" if "Beast" in creature.types else ("-4" if "Animal" in creature.types else low))

    def _spellcasterInt():
        creature.str, creature.dex, creature.con, creature.wis, creature.cha = terr, high, terr, high, mod
        creature.int = ext if int(creature.level) > 10 else high

    def _spellcasterWis():
        creature.str, creature.dex, creature.con, creature.int, creature.cha = low, high, low, mod, mod
        creature.wis = ext if int(creature.level) > 10 else high

    def _spellcasterCha():
        creature.str, creature.dex, creature.con, creature.int, creature.wis = terr, high, terr, mod, high
        creature.cha = ext if int(creature.level) > 10 else high

    def _skilled():
        creature.str, creature.con = terr, terr
        creature.dex, creature.int, creature.wis, creature.cha = high, high, high, high

    # this function needs to be called in the default case of the switch case below
    # and should prompt the user to create a custom stat array
    def _custom():
        ClearScreen()
        print('Choose your stats below. Creatures level 10 and below are recommended to have up to two high stats and the rest ' +
        'moderate or low (if your creature is Mindless or an Animal or Beast, consider adding a third high stat. Creatures above level 10 should ' +
        'have one extreme stat, one or two high stats and the rest moderate or low. Extreme stats are rare in creatures below level 10. ' +
        'Creatures below level 0 cannot have extreme stats. Terrible stats are generally not recommended except to offset a higher than ' +
        'normal number of high stats (two terrible stats per extra high stat).\n\n')

        cases = {
            'Extreme - ' + ext: lambda : ext,
            'High - ' + high: lambda : high,
            'Moderate - ' + mod: lambda : mod,
            'Low - ' + low: lambda : low,
            'Terrible - ' + terr: lambda : terr
        }

        # the following questions could be answered as set, but there's custom logic for int scores
        # may reorder to do int first then group the rest

        # str
        question = [
            {
                'type': 'list',
                'name': 'ans',
                'message': 'Choose STR:',
                'choices': [
                    'Extreme - ' + ext,
                    'High - ' + high,
                    'Moderate - ' + mod,
                    'Low - ' + low,
                    'Terrible - ' + terr
                ]
            }
        ]
        creature.str = cases.get(prompt(question)['ans'])()

        # dex
        ClearScreen()
        print('Choose your stats below. Creatures level 10 and below are recommended to have up to two high stats and the rest ' +
        'moderate or low (if your creature is Mindless or an Animal or Beast, consider adding a third high stat. Creatures above level 10 should ' +
        'have one extreme stat, one or two high stats and the rest moderate or low. Extreme stats are rare in creatures below level 10. ' +
        'Creatures below level 0 cannot have extreme stats. Terrible stats are generally not recommended except to offset a higher than ' +
        'normal number of high stats (two terrible stats per extra high stat).\n\n')
        question = [
            {
                'type': 'list',
                'name': 'ans',
                'message': 'Choose DEX:',
                'choices': [
                    'Extreme - ' + ext,
                    'High - ' + high,
                    'Moderate - ' + mod,
                    'Low - ' + low,
                    'Terrible - ' + terr
                ]
            }
        ]
        creature.dex = cases.get(prompt(question)['ans'])()

        # con
        ClearScreen()
        print('Choose your stats below. Creatures level 10 and below are recommended to have up to two high stats and the rest ' +
        'moderate or low (if your creature is Mindless or an Animal or Beast, consider adding a third high stat. Creatures above level 10 should ' +
        'have one extreme stat, one or two high stats and the rest moderate or low. Extreme stats are rare in creatures below level 10. ' +
        'Creatures below level 0 cannot have extreme stats. Terrible stats are generally not recommended except to offset a higher than ' +
        'normal number of high stats (two terrible stats per extra high stat).\n\n')
        question = [
            {
                'type': 'list',
                'name': 'ans',
                'message': 'Choose CON:',
                'choices': [
                    'Extreme - ' + ext,
                    'High - ' + high,
                    'Moderate - ' + mod,
                    'Low - ' + low,
                    'Terrible - ' + terr
                ]
            }
        ]
        creature.con = cases.get(prompt(question)['ans'])()

        # int
        if creature.isMindless:
            print("Your creature is mindless; its Int is -5. Press enter to continue.")
            creature.int = "-5"
            input()

        elif "Animal" in creature.types:
            print("Your creature is an Animal; its Int is -4. Press enter to continue.")
            creature.int = "-4"
            input()

        elif "Beast" in creature.types:
            ClearScreen()
            print("Your creature is a Beast. The typical Int score for beasts is -3, but it can be higher if you choose.")
            if prompt([{'type': 'confirm', 'name': 'ans', 'message': 'Assign different Int score? (default No)', 'default': False}])['ans']:
                ClearScreen()
                print('Choose your stats below. Creatures level 10 and below are recommended to have up to two high stats and the rest ' +
                'moderate or low (if your creature is Mindless or an Animal or Beast, consider adding a third high stat. Creatures above level 10 should ' +
                'have one extreme stat, one or two high stats and the rest moderate or low. Extreme stats are rare in creatures below level 10. ' +
                'Creatures below level 0 cannot have extreme stats. Terrible stats are generally not recommended except to offset a higher than ' +
                'normal number of high stats (two terrible stats per extra high stat).\n\n')
                question = [
                    {
                        'type': 'list',
                        'name': 'ans',
                        'message': 'Choose INT:',
                        'choices': [
                            'Extreme - ' + ext,
                            'High - ' + high,
                            'Moderate - ' + mod,
                            'Low - ' + low,
                               'Terrible - ' + terr
                        ]
                    }
                ]
                creature.int = cases.get(prompt(question)['ans'])()
            else:
                creature.int = "-3"
        
        else:
            ClearScreen()
            print('Choose your stats below. Creatures level 10 and below are recommended to have up to two high stats and the rest ' +
            'moderate or low (if your creature is Mindless or an Animal or Beast, consider adding a third high stat. Creatures above level 10 should ' +
            'have one extreme stat, one or two high stats and the rest moderate or low. Extreme stats are rare in creatures below level 10. ' +
            'Creatures below level 0 cannot have extreme stats. Terrible stats are generally not recommended except to offset a higher than ' +
            'normal number of high stats (two terrible stats per extra high stat).\n\n')
            question = [
                {
                    'type': 'list',
                    'name': 'ans',
                    'message': 'Choose INT:',
                    'choices': [
                        'Extreme - ' + ext,
                        'High - ' + high,
                        'Moderate - ' + mod,
                        'Low - ' + low,
                        'Terrible - ' + terr
                    ]
                }
            ]
            creature.int = cases.get(prompt(question)['ans'])()

        # wis
        ClearScreen()
        print('Choose your stats below. Creatures level 10 and below are recommended to have up to two high stats and the rest ' +
        'moderate or low (if your creature is Mindless or an Animal or Beast, consider adding a third high stat. Creatures above level 10 should ' +
        'have one extreme stat, one or two high stats and the rest moderate or low. Extreme stats are rare in creatures below level 10. ' +
        'Creatures below level 0 cannot have extreme stats. Terrible stats are generally not recommended except to offset a higher than ' +
        'normal number of high stats (two terrible stats per extra high stat).\n\n')
        question = [
            {
                'type': 'list',
                'name': 'ans',
                'message': 'Choose WIS:',
                'choices': [
                    'Extreme - ' + ext,
                    'High - ' + high,
                    'Moderate - ' + mod,
                    'Low - ' + low,
                    'Terrible - ' + terr
                ]
            }
        ]
        creature.wis = cases.get(prompt(question)['ans'])()

        # cha
        ClearScreen()
        print('Choose your stats below. Creatures level 10 and below are recommended to have up to two high stats and the rest ' +
        'moderate or low (if your creature is Mindless or an Animal or Beast, consider adding a third high stat. Creatures above level 10 should ' +
        'have one extreme stat, one or two high stats and the rest moderate or low. Extreme stats are rare in creatures below level 10. ' +
        'Creatures below level 0 cannot have extreme stats. Terrible stats are generally not recommended except to offset a higher than ' +
        'normal number of high stats (two terrible stats per extra high stat).\n\n')
        question = [
            {
                'type': 'list',
                'name': 'ans',
                'message': 'Choose CHA:',
                'choices': [
                    'Extreme - ' + ext,
                    'High - ' + high,
                    'Moderate - ' + mod,
                    'Low - ' + low,
                    'Terrible - ' + terr
                ]
            }
        ]
        creature.cha = cases.get(prompt(question)['ans'])()

    # god i fucking forgot python still doesn't have switch case statements oh god
    cases = {
        'Melee combatant': lambda : _melee(),
        'Ranged combatant': lambda : _ranged(),
        'Spellcaster(Int)': lambda : _spellcasterInt(),
        'Spellcaster(Wis)': lambda : _spellcasterWis(),
        'Spellcaster(Cha)': lambda : _spellcasterCha(),
        'Skill monkey': lambda : _skilled()
    }
    cases.get(answer['array'], lambda : _custom())()
