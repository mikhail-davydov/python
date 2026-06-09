from abc import ABC, abstractmethod


class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    @abstractmethod
    def can_move(self, horizontal, vertical):
        raise NotImplemented


class King(ChessPiece):
    def can_move(self, horizontal, vertical):
        return 0 < abs(ord(self.horizontal) - ord(horizontal)) ** 2 + abs(self.vertical - vertical) ** 2 < 3


class Knight(ChessPiece):
    def can_move(self, horizontal, vertical):
        return (ord(self.horizontal) - ord(horizontal)) ** 2 + abs(self.vertical - vertical) ** 2 == 5
