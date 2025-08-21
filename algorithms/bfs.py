from collections import deque
from os import listdir
from os.path import isfile, join


# BFS (breadth-first search)
def print_file_names_bfs(folder):
    queue = deque()
    queue.append(folder)
    while queue:
        path = queue.popleft()
        for file in sorted(listdir(path)):
            fullpath = join(path, file)
            if isfile(fullpath):
                print(fullpath)
            else:
                queue.append(fullpath)


print_file_names_bfs("./")