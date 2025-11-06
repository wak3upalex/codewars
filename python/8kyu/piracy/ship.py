class LEXA_Ship:
    def __init__(self, LEXA_draft, LEXA_crew):
        self.LEXA_draft = LEXA_draft
        self.LEXA_crew = LEXA_crew

    def LEXA_is_worth_it(self):
        return True if self.LEXA_draft - self.LEXA_crew * 1.5 > 20 else False
