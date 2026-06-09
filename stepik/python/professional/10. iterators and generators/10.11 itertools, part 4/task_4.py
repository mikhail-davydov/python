from itertools import groupby

tasks = [('Отдых', 'поспать днем', 3),
         ('Ответы на вопросы', 'ответить на вопросы в дискорде', 1),
         ('ЕГЭ Математика', 'доделать курс по параметрам', 1),
         ('Ответы на вопросы', 'ответить на вопросы в курсах', 2),
         ('Отдых', 'погулять вечером', 4),
         ('Курс по ооп', 'обсудить темы', 1),
         ('Урок по groupby', 'добавить задачи на программирование', 3),
         ('Урок по groupby', 'написать конспект', 1),
         ('Отдых', 'погулять днем', 2),
         ('Урок по groupby', 'добавить тестовые задачи', 2),
         ('Уборка', 'убраться в ванной', 2),
         ('Уборка', 'убраться в комнате', 1),
         ('Уборка', 'убраться на кухне', 3),
         ('Отдых', 'погулять утром', 1),
         ('Курс по ооп', 'обсудить задачи', 2)]

tasks_sorted = sorted(tasks, key=lambda t: (t[0], t[2]))
for key, tasks in groupby(tasks_sorted, key=lambda t: t[0]):
    print(f'{key}:')
    for task in list(tasks):
        print(f'    {task[2]}. {task[1]}')
    print()


# alt
for task_name, group in groupby(tasks_sorted, key=lambda x: x[0]):
    print(f'{task_name}:')
    for _, action, order in group:
        print(f'    {order}. {action}')
    print()