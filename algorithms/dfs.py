from os import listdir
from os.path import isfile, join


# DFS (deep-first search)
def print_file_names_dfs(folder):
    for file in sorted(listdir(folder)):
        fullpath = join(folder, file)
        if isfile(fullpath):
            print(fullpath)
        else:
            print_file_names_dfs(fullpath)


print_file_names_dfs("./")