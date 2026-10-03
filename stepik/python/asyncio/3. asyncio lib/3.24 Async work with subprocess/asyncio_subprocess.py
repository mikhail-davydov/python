import asyncio


# 1
# async def main():
#     process = await asyncio.create_subprocess_exec('notepad.exe')
#     print(process)


# 2
# async def main():
#     process = await asyncio.create_subprocess_exec('python.exe', '-c',
#                                                    'import time; time.sleep(1);'
#                                                    'print("Субпроцесс завершился и напечатал это сообщение.")',
#                                                    )
#     print(process)
#     await asyncio.sleep(2)
#
#
# if __name__ == '__main__':
#     asyncio.run(main())

# 3 print to file
# async def main(file):
#     process = await asyncio.create_subprocess_exec('python.exe', '-c',
#                                                    'import time; time.sleep(1);'
#                                                    'print("Субпроцесс завершился и напечатал это сообщение.")',
#                                                    stdout=file,
#                                                    )
#     print(process)
#     await asyncio.sleep(2)
#
#
# if __name__ == '__main__':
#     with open("new_file", "w") as file:
#         asyncio.run(main(file))


# async work with result
async def coro():
    print("другая задача в работе")
    await asyncio.sleep(1)
    print("другая задача еще в работе")
    await asyncio.sleep(1)
    print("другая задача завершается")


async def sub_proc():
    code = "import datetime; import time; time.sleep(1); print(datetime.datetime.now())"
    process = await asyncio.create_subprocess_exec('python.exe', '-c',
                                                   code, stdout=asyncio.subprocess.PIPE,
                                                   )
    print(process)
    result = await process.stdout.readline()
    print(result.decode().rstrip())


async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(sub_proc())
        tg.create_task(coro())


if __name__ == '__main__':
    asyncio.run(main())
