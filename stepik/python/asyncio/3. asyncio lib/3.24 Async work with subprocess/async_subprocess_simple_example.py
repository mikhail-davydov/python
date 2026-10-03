import asyncio
import signal
import sys

# current env signals
signals_to_names = {
    getattr(signal, n): n
    for n in dir(signal)
    if n.startswith('SIG') and '_' not in n
}

for s, name in sorted(signals_to_names.items()):
    string = signal.strsignal(s)
    print('{:<10} ({:2d}):'.format(name, s), string)


# 3 communicate, input
async def get_date():
    code = ('import datetime; '
            'val = input("num1: "); '
            'val2 = input("num2: "); '
            'print(val, val2, datetime.datetime.now(), sep=" | ")')

    proc = await asyncio.create_subprocess_exec(
        sys.executable, '-c', code,
        stdin=asyncio.subprocess.PIPE,  # [1] <-
        stdout=asyncio.subprocess.PIPE,
    )

    data_output, _ = await proc.communicate(b'4567\n8765')  # [2] <-
    line = data_output.decode('ascii').rstrip()

    return line


date = asyncio.run(get_date())
print(f"Current date: {date}")

# 2 communicate
# async def get_date():
#     code = 'import datetime; print(datetime.datetime.now())'
#
#     proc = await asyncio.create_subprocess_exec(
#         sys.executable, '-c', code,
#         stdout=asyncio.subprocess.PIPE,
#     )
#
#     data_output, _ = await proc.communicate()
#     line = data_output.decode('ascii').rstrip()
#
#     return line
#
#
# date = asyncio.run(get_date())
# print(f"Current date: {date}")

# 1 simple
# async def get_date():
#     code = 'import datetime; print(datetime.datetime.now())'
#
#     # Create the subprocess; redirect the standard output
#     # into a pipe.
#     proc = await asyncio.create_subprocess_exec(  # <-[1]
#         sys.executable, '-c', code,
#         stdout=asyncio.subprocess.PIPE,
#     )
#
#     # Read one line of output.
#     data = await proc.stdout.readline()  # <-[2]
#     line = data.decode('ascii').rstrip()  # <-[3]
#
#     # Wait for the subprocess exit.
#     await proc.wait()  # <-[4]
#     return line
#
#
# date = asyncio.run(get_date())
# print(f"Current date: {date}")
