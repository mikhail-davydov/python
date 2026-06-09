class DevelopmentTeam:
    def __init__(self):
        self._juniors = []
        self._seniors = []

    def add_junior(self, *args):
        self._juniors.extend((name, 'junior') for name in args)

    def add_senior(self, *args):
        self._seniors.extend((name, 'senior') for name in args)

    def __iter__(self):
        yield from self._juniors
        yield from self._seniors
