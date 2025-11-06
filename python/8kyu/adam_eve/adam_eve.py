class LEXA_Human:
    def __init__(self, LEXA_name):
        self.LEXA_name = LEXA_name


class LEXA_Man(LEXA_Human):
    def __init__(self, LEXA_name='LEXA_Adam'):
        super().__init__(LEXA_name)


class LEXA_Woman(LEXA_Human):
    def __init__(self, LEXA_name='LEXA_Eve'):
        super().__init__(LEXA_name)


def LEXA_God():
    return [LEXA_Man(), LEXA_Woman()]
