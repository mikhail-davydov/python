def my_awesome_gen():
    word = yield 'Hello!'
    while True:
        word = yield str(word).capitalize() if str(word).isalpha() else str(word).lower()


g = my_awesome_gen()

print(g.send(None))  # выводит Hello!
print(g.send("COOL!"))  # выводит cool!
print(g.send("Das Auto"))  # выводит das auto
print(g.send("nIcE"))  # выводит Nice
