def reverse(sequence):
    yield from (sequence[len(sequence) - 1 - i] for i in range(len(sequence)))


generator = reverse('beegeek')

print(type(generator))
print(*generator)


# alt
def reverse(sequence):
    yield from sequence[::-1]
