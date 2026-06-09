text = '''01,Artist,Otis Taylor
01,Title,Ran So Hard the Sun Went Down
01,Time,3:52
02,Artist,Waylon Jennings
02,Title,Honky Tonk Heroes (Like Me)
02,Time,3:29'''

with open('data.csv', 'w', encoding='utf-8') as file:
    file.write(text)

import task_11

task_11.condense_csv('data.csv', id_name='ID')

with open('condensed.csv', encoding='utf-8') as file:
    print(file.read().strip())