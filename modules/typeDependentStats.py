def AssignTypeDependantStats(creature):

    def _calcLevelWeaknessAmount():
        # this returns roughly the mid point of minimum and maximum on page 63 of the gamemastery guide
        # which seems like a nice...middle ground
        # infuriatingly, there's no nice formula to calculate this
        # this is also used for calculating resistance amount
        # maybe some day i'll change the name, but not this day
        if creature.level == -1:
            return 1
        elif creature.level == 0:
            return 2
        elif creature.level <= 6:
            return creature.level + 1
        elif creature.level <= 10:
            return creature.level
        elif creature.level <= 15:
            return creature.level - 1
        elif creature.level <= 17:
            return creature.level -2
        elif creature.level <= 19:
            return creature.level - 3
        else:
            return creature.level - 4

    def _aberration():
        creature.senses.append(('Darkvision', 60))
        creature.languages.append('Aklo')
        
    def _animal():
        creature.alignment = 'N'
        
    def _beast():
        pass

    def _celestial():
        creature.alignment = 'NG'  # technically, this is any good, but the user will have the oppurtunity to change it and if they
                                   # selected a celestial subtype, it will overwrite this with the subtype's specific alignment anyway
        creature.senses.append(('Darkvision', 60))
        creature.languages.append('Celestial')
        creature.abilityList.append(('Saves', '+1 status bonus to all saves vs. magic'))
        creature.weaknesses.append(('evil', _calcLevelWeaknessAmount()))
        # somehow i also need to carry good damage forward with this trait, or maybe
        # check types again when doing attacks
        
    def _construct():
        creature.immunities.append('bleed')
        creature.immunities.append('death effects')
        creature.immunities.append('diseased')
        creature.immunities.append('doomed')
        creature.immunities.append('drained')
        creature.immunities.append('fatigued')
        creature.immunities.append('healing')
        creature.immunities.append('necromancy')
        creature.immunities.append('nonlethal attacks')
        creature.immunities.append('paralyzed')
        creature.immunities.append('poison')
        creature.immunities.append('sickened')
        creature.immunities.append('unconscious')
        
    def _dragon():
        pass
    def _dream():
        pass
    def _elemental():
        pass
    def _fey():
        pass
    def _fiend():
        pass
    def _fungus():
        pass
    def _giant():
        pass
    def _humanoid():
        pass
    def _monitor():
        pass
    def _ooze():
        pass
    def _plant():
        pass
    def _spirit():
        pass
    def _undead():
        pass
    def _angel():
        creature.alignment = 'NG'
        creature.speeds.append(('fly', 40))
        creature.innateSpells.append(('Angelic Messenger', '-'))
        creature.abilityList.append(('Aura', 'Angels each have a unique aura based on how they serve as messengers and how they deliver those messages'))

    def _archon():
        creature.alignment = 'LG'
        creature.abilityList.append(('Virtual Ability', "Archons each represent a specific virtue, like courage or hope, and have a " +
                                                        "special ability based on the virtue they represent."))
        
    def _azata():
        creature.alignment = 'CG'
        creature.weaknesses.append(('evil', _calcLevelWeaknessAmount()))
        creature.weaknesses.append(('cold iron', _calcLevelWeaknessAmount()))
        creature.abilityList.append(('Freedom Ability', "Azatas each represent a specific freedom, like free expression or free love, " +
                                                        "and have a special ability based on the freedom they represent. "))

    def _daemon():
        pass
    def _demon():
        pass
    def _devil():
        pass
    def _rakshasa():
        pass
    def _aeon():
        creature.alignment = 'LN'
        creature.languages.append('Utopian')
        creature.weaknesses.append(('chaotic', _calcLevelWeaknessAmount()))
        # somehow i also need to carry lawful damage forward with this trait, or maybe
        # check types again when doing attacks
        
    def _inevitable():
        pass
    def _protean():
        pass
    def _protean():
        pass
    def _psychopomp():
        pass
    def _ethereal():
        pass
    def _swarm():
        pass
    def _acid():
        pass
    def _air():
        creature.languages.append('Auran')
        creature.speeds.append(('fly', 40))
        
    def _cold():
        creature.immunities.append('cold')

    def _electricity():
        pass
    def _earth():
        pass
    def _fire():
        pass
    def _water():
        pass

    cases = {
        'Aberration': lambda: _aberration(),
        'Animal': lambda: _animal(),
        'Beast': lambda: _beast(),
        'Celestial': lambda: _celestial(),
        'Construct': lambda: _construct(),
        'Dragon': lambda: _dragon(),
        'Dream': lambda: _dream(),
        'Elemental': lambda: _elemental(),
        'Fey': lambda: _fey(),
        'Fiend': lambda: _fiend(),
        'Fungus': lambda: _fungus(),
        'Giant': lambda: _giant(),
        'Humanoid': lambda: _humanoid(),
        'Monitor': lambda: _monitor(),
        'Ooze': lambda: _ooze(),
        'Plant': lambda: _plant(),
        'Spirit': lambda: _spirit(),
        'Undead': lambda: _undead(),
        'Angel': lambda: _angel(),
        'Archon': lambda: _archon(),
        'Azata': lambda: _azata(),
        'Daemon': lambda: _daemon(),
        'Demon': lambda: _demon(),
        'Devil': lambda: _devil(),
        'Rakshasa': lambda: _rakshasa(),
        'Aeon': lambda: _aeon(),
        'Inevitable': lambda: _inevitable(),
        'Protean': lambda: _protean(),
        'Psychopomp': lambda: _psychopomp(),
        'Ethereal': lambda: _ethereal(),
        'Swarm': lambda: _swarm(),
        'Acid': lambda: _acid(),
        'Air': lambda: _air(),
        'Cold': lambda: _cold(),
        'Electricity': lambda: _electricity(),
        'Earth': lambda: _earth(),
        'Fire': lambda: _fire(),
        'Water': lambda: _water()
    }

    for type in creature.types:
        cases.get(type)