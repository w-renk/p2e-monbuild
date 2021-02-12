from .scripts import ClearScreen
from PyInquirer import prompt

def SetMindless(creature):
    ClearScreen()
    print("Would you like to make your creature mindless? Mindless creatures are forced to have a -5 intelligence modifier (corresponding to a score of 0) " +
    "and possibly -5 modifiers in wisdom and/or charisma as well. Mindless creatures are immune to all mind affecting effects.\n\n" +
    "Plants and constructs are usually mindless, but there is no specific requirement for them to not have an intelligence score.\n\n")

    question = [
        {
            'type': 'list',
            'name': 'ans',
            'message': 'Would you like to make your creature mindless?',
            'choices': [
                'Yes',
                'No'
            ]
        }
    ]

    creature.isMindless = True if prompt(question)['ans'] == 'Yes' else False