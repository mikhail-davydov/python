import subprocess

# 1
# subprocess.run(['notepad.exe'])

# 2
# process = subprocess.run(
#     [
#         'python.exe', '-c',
#         'import time; time.sleep(3); '
#         'print("Субпроцесс завершился и напечатал это сообщение.")',
#     ],
# )
#
# print("Завершается и главный процесс!")

# 3
result = subprocess.run(['dir'], shell=True, capture_output=True)
print('first')
print(result.stdout.decode("cp866"))

print()
print('second')
result = subprocess.run(['dir'], shell=True, capture_output=True, encoding="u8")
print(result.stdout)


# 3. linux
# result = subprocess.run(['ls', '-l'], capture_output=True, encoding='utf-8')
# print(result.stdout)

# 4.1 linux
# result = subprocess.run(['ls', '-l', '..'], capture_output=True, text=True)
# print(result.stdout)

# 4.2 linux
# def get_system_info():
#     machine_info = subprocess.run(['uname', '-a'], capture_output=True, text=True)
#     print("Информация о машине:")
#     print(machine_info.stdout)
#
#     cpu_info = subprocess.run(['lscpu'], capture_output=True, text=True)
#     print("Информация о процессорах:")
#     print(cpu_info.stdout)
#
# if __name__ == "__main__":
#     get_system_info()

# 4.3 linux
# command = "cat /proc/cpuinfo"
# print(subprocess.check_output(command, shell = True).decode().strip())

# 5. linux
# def get_installed_packages():
#     output = subprocess.check_output(["pip", "list"])
#     return output.decode().strip()
#
#
# installed_packages = get_installed_packages()
#
# if installed_packages:
#     for package in installed_packages.split("\n"):
#         print(package)


# final, linux, sys and python review
def get_system_info():
    machine_info = subprocess.run(['uname', '-a'], capture_output=True, text=True)
    print("Информация о машине:")
    print(machine_info.stdout)

    cpu_info = subprocess.run(['lscpu'], capture_output=True, text=True)
    print("Информация о процессорах:")
    print(cpu_info.stdout)


def get_installed_packages():
    output = subprocess.check_output(["pip", "list"])
    return output.decode().strip()


installed_packages = get_installed_packages()

if installed_packages:
    for package in installed_packages.split("\n"):
        print(package)

if __name__ == "__main__":
    get_system_info()
