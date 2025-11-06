import random


class LEXA_Ghost:
    def __init__(self):
        self.LEXA_color = random.choice(['LEXA_white', 'LEXA_yellow', 'LEXA_purple', 'LEXA_red'])


LEXA_ghost = LEXA_Ghost()
print(LEXA_ghost.LEXA_color)
