class ReversedSequence:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = 0

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, key):
        return self.sequence[~key]

    # optional
    def __iter__(self):
        yield from reversed(self.sequence)