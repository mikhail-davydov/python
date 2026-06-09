import pickle
import sys

filename = input()
with open(filename, 'rb') as i_file:
    func = pickle.load(i_file)

args = [line.strip() for line in sys.stdin]
print(func(*args))