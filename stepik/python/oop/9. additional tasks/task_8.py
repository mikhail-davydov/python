from dataclasses import dataclass, field


@dataclass
class Testpaper:
    discipline: str
    correct_answers: list
    pass_pct: str


@dataclass
class Student:
    _tests: dict = field(default_factory=dict, init=False)

    @property
    def tests_taken(self):
        return self._tests if self._tests else 'No tests taken'

    def take_test(self, testpaper: Testpaper, answers: list):
        student_total = sum(student == correct for student, correct in zip(answers, testpaper.correct_answers))
        student_pct = round(100 * student_total / len(testpaper.correct_answers))
        passed_condition = student_pct >= int(testpaper.pass_pct[:-1])
        test_result = 'Passed' if passed_condition else 'Failed'
        self._tests.update({
            testpaper.discipline: f'{test_result}! ({student_pct}%)'
        }
        )


# alt

class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark


class Student:
    def __init__(self):
        self.tests_taken = 'No tests taken'

    def take_test(self, paper: Testpaper, student_answers):
        score = len(set(paper.markscheme) & set(student_answers)) / len(paper.markscheme) * 100
        result = 'Passed!' if score >= int(paper.pass_mark[:-1]) else 'Failed'
        percent = f'{score:.0f}%'

        if self.tests_taken == 'No tests taken':
            self.tests_taken = {paper.subject: f'{result} ({percent})'}
        else:
            self.tests_taken[paper.subject] = f'{result} ({percent})'


# alt


class Testpaper:
    def __init__(self, theme: str, cards: list, to_pass: str):
        self._theme = theme
        self._cards = set(cards)
        self._to_pass = int(to_pass.rstrip("%"))

    def __call__(self, answers: list):
        exam = round(100 * len(set(answers) & self._cards) / len(self._cards))
        return {f"{self._theme}": f"{['Failed', 'Passed'][exam >= self._to_pass]}! ({exam}%)"}


class Student:
    def __init__(self):
        self._tests = {}

    def take_test(self, test: Testpaper, answers: list):
        self._tests.update(test(answers))

    @property
    def tests_taken(self):
        return self._tests if self._tests else "No tests taken"
