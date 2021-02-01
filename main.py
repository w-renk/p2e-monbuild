from PyInquirer import style_from_dict, Token, prompt, print_json, Separator, Validator, ValidationError
from pprint import pprint

questions = [
    {
        'type': 'checkbox',
        'message': 'Choose monster creature type(s). Monsters should generally have between 1 and 3 types (in any combination of major, minor and element). \
            Any more than three can lead to monsters with wide varieties of resistances and bonuses potentially increasing power. \
            Elementals and Dragons often have an element subtype, though they are not required. Most major creature types have an \
            associated skill for Recall Knowledge; these will be reviewed after type selection with an opportunity to modify them.',
        'name': 'types',
        'choices': [
            Separator('-- Major Types --'),
            {
                'name': 'Aberration'
            },
            {
                'name': 'Animal'
            },
            {
                'name': 'Beast'
            },
            {
                'name': 'Celestial'
            },
            {
                'name': 'Construct'
            },
            {
                'name': 'Dragon'
            },
            {
                'name': 'Dream'
            },
            {
                'name': 'Elemental'
            },
            {
                'name': 'Fey'
            },
            {
                'name': 'Fiend'
            },
            {
                'name': 'Fungus'
            },
            {
                'name': 'Giant'
            },
            {
                'name': 'Humanoid'
            },
            {
                'name': 'Monitor'
            },
            {
                'name': 'Ooze'
            },
            {
                'name': 'Plant'
            },
            {
                'name': 'Spirit'
            },
            {
                'name': 'Undead'
            },
        ]
    }
]