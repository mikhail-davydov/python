def filter_names(names, ignore_char, max_names):
    try:
        no_digits_gen = (name for name in names if name.isalpha())
        ignore_char_gen = (name for name in no_digits_gen if not name.lower().startswith(ignore_char.lower()))
        for _ in range(max_names):
            yield next(ignore_char_gen)
    except:
        pass


data = ['Di6ma', 'Ti4mur', 'Ar5thur', 'Anri7620', 'Ar3453ina', '345German', 'Ruslan543', 'Soslanfsdf123', 'Geo000000r']

print(*filter_names(data, 'A', 100))


# alt
def filter_names(names, ignore_char, max_names):
    ignore_char = ignore_char.lower()

    filtered_by_first_char = (
        name for name in names
        if not name.lower().startswith(ignore_char)
    )

    filtered_by_digits = (
        name for name in filtered_by_first_char
        if not any(ch.isdigit() for ch in name)
    )

    for name, _ in zip(filtered_by_digits, range(max_names)):
        yield name
