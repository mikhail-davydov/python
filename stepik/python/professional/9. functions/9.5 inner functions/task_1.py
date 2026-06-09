def power(degree):
    def result(num):
        return num ** degree

    return result


result = power(4)(2)
print(result)


# base
def power(degree):
    return lambda x: x ** degree
