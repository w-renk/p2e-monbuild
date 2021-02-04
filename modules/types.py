from .scripts import ClearScreen
from PyInquirer import prompt, Separator

knowledgeTypes = {

}

def _promptTypesOverride(template, types):
    ClearScreen()
    print("You have selected a template to use for your creature. It is not recommended to override or change the types dictated by templates. Would you like " +
    "to override creature types anyway?")
    question = [
        {
            'type': 'confirm',
            'message': 'Y/n? (default "no")',
            'name': 'override',
            'default': False
        }
    ]

    if prompt(question)['override']:
        ClearScreen()
        print("The template you have selected is " + template + " and types that have already been assigned to your creature are:")
        for type in types:
            print(type)
        print("\nIf you want to keep any of the above types, be sure to select them in the next step as only explicitly selected types will be carried forward.\n\n" +
        "Press enter to continue")
        input()
        return True
    return False

def SelectTypes(template, types):

    if types:
        if not _promptTypesOverride(template, types):
            return types

    ClearScreen()
    print('Choose monster creature type(s). Monsters should generally have 1 major type with up to 1 additional major or related minor ' + 
        'type and optionally a single element subtype. Any more than that can lead to monsters with wide varieties of resistances ' + 
        'and bonuses, potentially increasing power beyond the intended level of the monster. In addition, the "Undead" creature type should not be combined' +
        'with other types except for "Spirit". It is rare for a creature with the "Spirit" type to not also bear the "Undead" type.\n\n' + 
        'Elementals and Dragons often have an element subtype, though one is not required.\n\n' + 
        'Most major creature types have an associated skill for Recall Knowledge; these will be reviewed after type selection with an opportunity to modify them.\n\n' + 
        '(Press spacebar to select entries and enter to confirm)\n' +
        'Press enter to continue.')
    input()

    questions = [
        {
            'type': 'checkbox',
            'message': 'Choose monster types',
            'name': 'types',
            'choices': [
                Separator('\n-- Major Types --'),
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

                Separator('\n-- Minor types for Celestials --'),
                {'name': 'Angel'},
                {'name': 'Archon'},
                {'name': 'Azata'},

                Separator('\n-- Minor Types for Fiends --'),
                {'name': 'Daemon'},
                {'name': 'Demon'},
                {'name': 'Devil'},
                {'name': 'Rakshasa'},

                Separator('\n-- Minor Types for Monitors --'),
                {'name': 'Aeon'},
                {'name': 'Inevitable'},
                {'name': 'Protean'},
                {'name': 'Psychopomp'},

                Separator('\n-- Minor Types for any major type --'),
                {'name': 'Ethereal'},
                {'name': 'Swarm'},

                Separator('\n-- Element Subtypes --'),
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

    return prompt(questions)['types']