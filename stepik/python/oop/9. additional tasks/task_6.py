from dataclasses import dataclass, field


@dataclass
class HighScoreTable:
    scores_num: int
    scores: list = field(default_factory=list, init=False)

    def update(self, score):
        self.scores.append(score)
        self.scores.sort(reverse=True)
        self.scores[:] = self.scores[:self.scores_num]

    def reset(self):
        self.scores.clear()


# alt

class HighScoreTable:
    def __init__(self, limit):
        self._limit = limit
        self.scores = []

    def update(self, n):
        self.scores.append(n)
        self.scores = sorted(self.scores, reverse=True)[:self._limit]

    def reset(self):
        self.scores = []
