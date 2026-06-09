def sand_watch():
    def print_row(num, width, subtrahend):
        print(f'{str(num) * width:^16}')
        if width - subtrahend > 0:
            print_row(num + 1, width - subtrahend, subtrahend)
        if width != subtrahend:
            print(f'{str(num) * width:^16}')

    print_row(1, 16, 4)


sand_watch()


# author solution
def hourglass(d=1, width=16, indent=0):
    line = ' ' * indent + str(d) * width
    print(line)
    if d < 4:
        hourglass(d + 1, width - 4, indent + 2)
        print(line)


hourglass()
