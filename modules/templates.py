from .scripts import ClearScreen
from PyInquirer import prompt

def SelectTemplateGraft():
    ClearScreen()
    print("You can optionally apply a template graft to your creature. Template grafts increase the level of the monster they're applied" +
            "to and add certain bonuses and unique abilities.\n\n" +
            "Ghost (+2): AC, attacks, DCs, saves, perception and skills increase; has enforced traits; loses abilities and traits tied to being a living creature\n\n" +
            "Ghoul (+1): AC, attacks, DCs, saves, and skills increase; has enforced traits; loses abilities and traits tied to being a living creature\n\n" +
            "Ghast (+2): same as Ghoul, but bonuses are further increased\n\n" +
            "Graveknight (+1): must be humanoid and at least level 6; AC, attacks, saves, perception and skills increase; gains the " +
            "undead trait; loses abilities and traits tied to being a living creature\n\n" +
            "Lich (+1): must be a spellcaster and at least level 13; spell DCs and spell attacks increase; gains undead trait; loses abilities +"
            "and traits tied to being a living creature\n\n" +
            "Ravener (+2): must be a dragon and at least level 15; rare to see raveners that were not originally an ancient true dragon (chromatic, metallic or primal);"+
            "AC, attacks, DCs, saves and skills are increased; gains the undead trait\n\n" +
            "Vampire (+1): AC, attacks, DCs, saves and skills increase; gains the undead trait; loses abilities and traits tied to being a living creature\n\n" +
            "Vrykolakas (+1): same as vampire except that it gains different abilities\n\n" +
            "Werecreature (+1): must be a humanoid; AC, attacks, DCs, saves and skills increase; gains the beast trait\n\n" +
            "Worm That Walks (+1): must be a spellcaster; AC, attacks, DCs, saves and skills increase; gains the aberration and swarm traits\n\n")

    question = [
        {
            'type': 'list',
            'name': 'template',
            'message': 'Choose one of the following:',
            'choices': ['Ghost', 'Ghoul', 'Ghast', 'Graveknight', 'Lich', 'Ravener', 'Vampire', 'Vrykolakas', 'Werecreature', 'Worm That Walks']
        }
    ]

    return prompt(question)