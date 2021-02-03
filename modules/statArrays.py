from scripts import ClearScreen
from PyInquirer import prompt

def SelectStatArray(statBlock):
    ClearScreen()
    print("You now have the option of using a preset stat array (listed below) or to make a custom array.\n\n" +
    "Melee combatant: high (or extreme, at higher levels) Str, high Con\n\n" +
    "Ranged combatant: high (or extreme, at higher levels) Dex, high Wis\n\n" +
    "Spellcaster: high Dex, high (or extreme) mental stat\n\n" + 
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
                'Spellcaster',
                'Skill monkey'
            ]
        }
    ]

    answer = prompt(question)
    #print(answer)

    # define stat arrays here
    # need to define functions here to calculate arrays based on the predefined arrays


    # god i fucking forgot python still doesn't have switch case statements oh god
    cases = {
        'Melee combatant': lambda: print("Melee combatant"),
        'Ranged combatant': lambda: print("ranged"),
        'Spellcaster': lambda: print('spellcaster'),
        'Skill monkey': lambda: print('skill monkey')
    }
    cases.get(answer['array'], lambda: print('custom'))()

SelectStatArray()