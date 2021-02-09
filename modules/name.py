from .scripts import ClearScreen
from PyInquirer import prompt

def SelectName(statBlock):
    ClearScreen()
    print("First, enter a name for your creature (or leave blank if you want). This doesn't determine stats in any way.\n\n")
    question = [
        {
            'type': 'input',
            'message': 'Name (leave blank for none):',
            'name': 'name'
        }
    ]

    statBlock.name = prompt(question)['name']