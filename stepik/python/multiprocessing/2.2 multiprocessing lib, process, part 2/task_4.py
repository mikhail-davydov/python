import multiprocessing

# Ваше решение
def terminate_overhead_processes():
    core_num = multiprocessing.cpu_count()
    while len(multiprocessing.active_children()) > core_num:
        children = multiprocessing.active_children()
        process_to_terminate = children[-1]
        process_to_terminate.terminate()
        process_to_terminate.join()
        process_to_terminate.close()
        del process_to_terminate

# alt

def terminate_overhead_processes():
    for pr in multiprocessing.active_children()[multiprocessing.cpu_count():]:
        pr.terminate()
        pr.join()
        pr.close()