def remove_marks(text, marks):
    remove_marks.__dict__.setdefault('count', 0)
    remove_marks.count += 1
    for mark in marks:
        text = text.replace(mark, '')
    return text


marks = '.,!?'
text = 'Are you listening? Meet my family! There are my parents, my brother and me.'

for mark in marks:
    print(remove_marks(text, mark))

print(remove_marks.count)


# base
def remove_marks(text, marks):
    remove_marks.count += 1
    for c in marks:
        text = text.replace(c, '')
    return text


remove_marks.count = 0
