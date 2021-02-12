from .scripts import ClearScreen
from PyInquirer import prompt

def SelectAlignment(creature):
    ClearScreen()
    print("Choose an alignment for your creature. Its current alignment is: " + creature.alignment + " (if it's not true neutral, it's alignment " +
    " was set by the type(s) selected earlier; you can still change it, however). You can choose to change the current alignment below, or keep the current one.")

    question = [
        {
            "type": "list",
            "name": "ans",
            "message": "Select an option:",
            "choices": [
                'Keep current aligment of ' + creature.alignment,
                'LG',
                'NG',
                'CG',
                'LN',
                'N',
                'CN',
                'LE',
                'NE',
                'CE'
            ]
        }
    ]

    answer = prompt(question)['ans']
    
    if answer == question[0]['choices'][0]:
        return
    else:
        creature.alignment = answer
        return