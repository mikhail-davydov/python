from collections.abc import Sequence


class DNA(Sequence):

    def __init__(self, chain):
        self.chain = chain
        self.__dict__.update({
            'A': ('A', 'T'),
            'T': ('T', 'A'),
            'G': ('G', 'C'),
            'C': ('C', 'G')
        })

    def __str__(self):
        return self.chain

    def __getitem__(self, index):
        return self.__dict__[self.chain[index]]

    def __len__(self):
        return len(self.chain)

    def __contains__(self, item):
        return item in self.chain

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__class__(self.chain + other.chain)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.chain == other.chain
