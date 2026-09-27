import linecache

import sys

line_counts: dict[str, int] = {}


def trace_func(frame, event, arg):
    if event == 'line':
        lineno = frame.f_lineno
        filename = frame.f_code.co_filename
        line_code = linecache.getline(filename, lineno).strip()
        line_counts[line_code] = line_counts.get(line_code, 0) + 1

    return trace_func


sys.settrace(trace_func)
