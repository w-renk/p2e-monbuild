from .scripts import ClearScreen
from PyInquirer import prompt
from prompt_toolkit.validation import Validator, ValidationError

def SelectLevel(creature):
    ClearScreen()

    if creature.template:
        constraintString = ("You have chosen the following template: " + creature.template + 
                            ", and it has the following level constraint: " + creature.levelConstraint + ". There is no checking to enforce this, just be sure to " +
                            "honor the constraint unless you know for sure the consequences of choosing a lower level (e.g., potentially over-powered enemies for " +
                            "a given level)")
    else:
        constraintString = ""

    print("Choose a level for your creature. " + constraintString + "\n\n")

    class LevelValidator(Validator):
        def validate(self, document):
            try:
                ok = True if (int(document.text) >= -1 and int(document.text) <= 24) else False
            except:
                ok = False

            if not ok:
                raise ValidationError(
                message='Enter a number between -1 and 24',
                cursor_position=len(document.text))

    question = [
        {
            'type': 'input',
            'name': 'level',
            'message': 'Enter a number between -1 and 24',
            'validate': LevelValidator
        }
    ]

    creature.level = prompt(question)['level']