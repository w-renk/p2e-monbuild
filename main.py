from pprint import pprint
from modules import StatBlock, ClearScreen

creature = StatBlock()

ClearScreen()
print(creature.renderPlainText())
print("\n\n\nPress enter to exit")