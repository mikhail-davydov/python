import multiprocessing


class MyProcess(multiprocessing.Process):

    @property
    def parent_pid(self):
        return self._parent_pid

    @property
    def parent_name(self):
        return self._parent_name


# alt

class MyProcess(multiprocessing.Process):
    @property
    def parent_pid(self):
        return multiprocessing.current_process().pid

    @property
    def parent_name(self):
        return multiprocessing.current_process().name
