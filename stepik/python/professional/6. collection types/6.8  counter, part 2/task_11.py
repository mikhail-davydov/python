from collections import namedtuple, Counter

Book = namedtuple('Book', 'grade price')

books = Counter(map(int, input().split()))
n = int(input())

total = 0
for i in range(n):
    book = Book(*map(int, input().split()))
    if book.grade in +books:
        total += book.price
        books.subtract({book.grade: 1})

print(total)

# course solution
from collections import Counter

books = Counter(map(int, input().split()))
total = 0

for _ in range(int(input())):
    book, price = map(int, input().split())
    total += bool(books[book]) * price
    books -= Counter({book: 1})

print(total)
