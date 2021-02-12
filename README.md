# Pathfinder 2nd Edition Monster Builder

Interactive CLI monster builder for Pathfinder 2nd Edition

**This is a work in progress and is currently mostly useless.**

&nbsp;

## Installation

Requires Python 3 to be installed on your system. Install dependencies by running:
```
$ pip install -r requirements.txt
```

&nbsp;

## Running

Run the program with:
```
$ python main.py
```

Currently generates a plaintext statblock in the following format (printed to the console):
```
Test Monster, Please Ignore                  Creature 6
N  Animal
Perception +0; low-light vision, scent 30 feet
Skills Acrobatics +20, Occultism +7
Str 0, Dex 0, Con 0, Int 0, Wis 0, Cha 0
Items The shiniest shiny, The second shiniest shiny

================================================================

AC 23; Fort 12, Reflex 18, Will 12
HP 115; Resistances fire 5, piercing 5; Weaknesses cold 10

================================================================

Speed walk: 25 feet, swim: 35 feet
Strike +18 [+13/+8], Damage 2d8+8 slashing
test ability name this is some rules text for that ability
second test ability name this rules text is worse than the first

================================================================
```