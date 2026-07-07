import multiprocessing
from multiprocessing.managers import BaseManager


class MyMathClass:
    def add(self, x, y):
        return x + y

    def mul(self, x, y):
        return x * y


class MyManager(BaseManager):
    pass


def task(obj, a, b):
    print(obj.add(a, b))
    print(obj.mul(a, b))


if __name__ == '__main__':
    MyManager.register('Math', MyMathClass)
    with MyManager() as manager:
        maths = manager.Math()
        print(maths.add(4, 3))
        pr_1 = multiprocessing.Process(target=task, args=(maths, 10, 20))
        pr_1.start()
        pr_1.join()

# 7 - результат работы главного процесса
# 30 - результат работы дочернего процесса pr_1 при выполнении метода add переданного объекта maths
# 200 - результат метода mul....
