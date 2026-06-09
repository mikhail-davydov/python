from collections import defaultdict

import re
import sys

result = defaultdict(set)

for line in sys.stdin:
    for tag, params in re.findall(r'<(\w+)(.*?)>', line):
        result[tag].update(re.findall(r'([\w-]+)=', params))

for tag in sorted(result):
    print(f'{tag}: {", ".join(sorted(result[tag]))}')
