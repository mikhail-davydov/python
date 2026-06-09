import re

print(re.sub(r'\b(\w)(\w)', r'\2\1', input()))

# alt
print(re.sub(r'\b(?P<first>\w)(?P<second>\w)', r'\g<second>\g<first>', input()))
