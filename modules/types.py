from .scripts import ClearScreen
from PyInquirer import prompt, Separator

knowledgeTypes = {
    
}

def Select():
    print('Choose monster creature type(s). Monsters should generally have 1 major type with up to 1 additional major or related minor ' + 
        'type and optionally a single element subtype. Any more than that can lead to monsters with wide varieties of resistances ' + 
        'and bonuses, potentially increasing power beyond the intended level of the monster.\n\n' + 
        'Elementals and Dragons often have an element subtype, though they are not required.\n\n' + 
        'Most major creature types have an associated skill for Recall Knowledge; these will be reviewed after type selection with an opportunity to modify them.\n\n' + 
        'Press enter to continue.')
    input()
    ClearScreen()

    questions = [
        {
            'type': 'checkbox',
            'message': 'Choose monster types',
            'name': 'types',
            'choices': [
                Separator('-- Major Types --'),
                {'name': 'Aberration'},
                {'name': 'Animal'},
                {'name': 'Beast'},
                {'name': 'Celestial'},
                {'name': 'Construct'},
                {'name': 'Dragon'},
                {'name': 'Dream'},
                {'name': 'Elemental'},
                {'name': 'Fey'},
                {'name': 'Fiend'},
                {'name': 'Fungus'},
                {'name': 'Giant'},
                {'name': 'Humanoid'},
                {'name': 'Monitor'},
                {'name': 'Ooze'},
                {'name': 'Plant'},
                {'name': 'Spirit'},
                {'name': 'Undead'},

                Separator('-- Minor types for Celestials --'),
                {'name': 'Angel'},
                {'name': 'Archon'},
                {'name': 'Azata'},

                Separator('-- Minor Types for Fiends --'),
                {'name': 'Daemon'},
                {'name': 'Demon'},
                {'name': 'Devil'},
                {'name': 'Rakshasa'},

                Separator('-- Minor Types for Monitors --'),
                {'name': 'Aeon'},
                {'name': 'Inevitable'},
                {'name': 'Protean'},
                {'name': 'Psychopomp'},

                Separator('-- Minor Types for any major type --'),
                {'name': 'Ethereal'},
                {'name': 'Swarm'},

                Separator('-- Element Subtypes --'),
                {'name': 'Acid'},
                {'name': 'Air'},
                {'name': 'Cold'},
                {'name': 'Electricity'},
                {'name': 'Earth'},
                {'name': 'Fire'},
                {'name': 'Water'}
            ]
        }
    ]

    return(prompt(questions))