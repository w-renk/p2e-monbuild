from .scripts import ClearScreen
from PyInquirer import prompt

def SelectTemplateGraft():
    ClearScreen()
    print("You can optionally use a template graft to start the creation process. Template grafts grant specific bonuses and unique abilities. They also " +
            "largely determine the creature types the monster will have. Listed minimum levels account for the graft applied to a level -1 " +
            "creature except for when the grafts themselves require a minimum level, e.g., graveknight. See " +
            "https://2e.aonprd.com/MonsterTemplates.aspx for additional information on the abilities that each of these grant.\n\n" +

            "Ghost: incorporeal undead; has the Spirit and Undead traits; minimum level 1\n\n" +

            "Ghoul: usually intelligent, flesh-eating undead formed from humanoids; often form societies; has the Undead trait; minimum level 0\n\n" +

            "Ghast: stronger version of Ghouls; minimum level 1\n\n" +

            "Graveknight: once humanoid undead warriors kept alive by cursed armor; has the Undead trait; minimum level 6\n\n" +

            "Lich: powerful spellcasters that have intentionally become undead; has the Undead trait; recommended minimum level 13\n\n" +

            "Ravener: skeletal undead dragons that feed on the souls of the living; has the Undead trait; recommended minimum level 15\n\n" +

            "True Vampire: once humanoid undead that feed on the blood of living creatures; has the Undead trait; minimum level 6\n\n" +

            "Vampire Spawn: undead turned by a True Vampire's bite; has the Undead trait; minimum level 0\n\n" +

            "Vrykolakas: vampiric, plague-bearing undead risen from neglected corpses; has the Undead trait; minimum level 0\n\n" +

            "Werecreature: shapeshifting, humanoid animal hybrids; has the Beast and Humanoid traits; minimum level 0\n\n" +

            "Worm That Walks: eldritch spellcasters formed from an amalgamation of grave worms; has the Aberration and Swarm traits; recommended minimum level 5\n\n")

    question = [
        {
            'type': 'list',
            'name': 'template',
            'message': 'Choose one of the following:',
            'choices': ['Create a monster without a template graft', 
                        'Ghost', 'Ghoul', 'Ghast', 'Graveknight', 'Lich', 'Ravener', 'True Vampire', 
                        'Vampire Spawn', 'Vrykolakas', 'Werecreature', 'Worm That Walks']
        }
    ]

    return prompt(question)