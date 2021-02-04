from .scripts import ClearScreen
from PyInquirer import prompt

def SelectStatArray(statBlock):
    ClearScreen()
    print("You now have the option of using a preset stat array (listed below) or to make a custom array.\n\n" +
    "Melee combatant: high (or extreme, at higher levels) Str, high Con\n\n" +
    "Ranged combatant: high (or extreme, at higher levels) Dex, high Wis\n\n" +
    "Spellcaster(Int): high Dex, high (or extreme) Int\n\n" + 
    "Spellcaster(Wis): high Dex, high (or extreme) Wis\n\n" + 
    "Spellcaster(Cha): high Dex, high (or extreme) Cha\n\n" + 
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

    # the following calc funtions near enough reflect the math used to calculate the chart on page 59 of the Gamemastery Guide
    # theirs breaks the pattern in a couple places, i'm not overly concerned about it
    def _calcExtreme(level):
        if level > 0:
            return "+" + str(int(level * 8 / 24 + 5))
        return 'N/a'

    def _calcHigh(level):
        return "+" + str(int((level + 2) * 9 / 26 + 3))

    def _calcModerate(level):
        return "+" + str(int((level + 2) * 7 / 26 + 2))

    def _calcLow(level):
        return "+" + str(int((level + 2) * 7 / 26))

    def _melee(statBlock):
        if statBlock.level > 10:
            statBlock.str = _calcExtreme(statBlock.level)
        else:
            statBlock.str = _calcHigh(statBlock.level)
        statBlock.dex = _calcLow(statBlock.level)
        statBlock.con = _calcHigh(statBlock.level)
        statBlock.wis = _calcModerate(statBlock.level)
        statBlock.int = _calcLow(statBlock.level)
        statBlock.cha = _calcModerate(statBlock.level)

    def _ranged(statBlock):
        pass

    def _spellcasterInt(statBlock):
        pass

    def _spellcasterWis(statBlock):
        pass

    def _spellcasterCha(statBlock):
        pass

    def _skilled(statBloc):
        pass

    # this function needs to be called in the default case of the switch case below
    # and should prompt the user to create a custom stat array
    def _custom():
        pass

    # god i fucking forgot python still doesn't have switch case statements oh god
    cases = {
        'Melee combatant': lambda statBlock : _melee(statBlock),
        'Ranged combatant': lambda statBlock : _ranged(statBlock),
        'Spellcaster(Int)': lambda statBlock : _spellcasterInt(statBlock),
        'Spellcaster(Wis)': lambda statBlock : _spellcasterWis(statBlock),
        'Spellcaster(Cha)': lambda statBlock : _spellcasterCha(statBlock),
        'Skill monkey': lambda statBlock : _skilled(statBlock)
    }
    statArray = cases.get(answer['array'], lambda statBlock : _custom(statBlock.level))()  # why the hell does this extra set of parentheses need to be here?

    return statArray