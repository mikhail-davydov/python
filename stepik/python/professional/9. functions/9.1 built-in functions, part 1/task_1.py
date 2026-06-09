def abc():
    a_ord = ord('a')
    z_ord = ord('z')
    for ind in range(a_ord, z_ord + 1):
        print(chr(ind))


abc()

# alt
[print(chr(i)) for i in range(ord('a'), ord('z') + 1)]
