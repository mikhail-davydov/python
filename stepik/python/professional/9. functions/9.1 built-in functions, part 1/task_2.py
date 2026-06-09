def convert(number):
    return (
        bin(number).replace('0b', ''),
        oct(number).replace('0o', ''),
        hex(number).replace('0x', '').upper()
    )


print(convert(15))


# alt
def convert(number):
    return f'{number:b}', f'{number:o}', f'{number:X}'
