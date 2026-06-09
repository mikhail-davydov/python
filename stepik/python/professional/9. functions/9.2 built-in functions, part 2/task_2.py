obj = eval(input())

if isinstance(obj, list):
    print(obj[-1])
elif isinstance(obj, tuple):
    print(obj[0])
elif isinstance(obj, set):
    print(len(obj))

# base
n = eval(input())

ops = {
    list: lambda x: x[-1],
    tuple: lambda x: x[0],
    set: lambda x: len(x)
}

print(ops[type(n)](n))

# alt
input_any_type = eval(input())

match input_any_type:
    case list():
        print(input_any_type[-1])
    case tuple():
        print(input_any_type[0])
    case set():
        print(len(input_any_type))
