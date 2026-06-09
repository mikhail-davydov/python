def best_sender(messages, senders):
    words = defaultdict(int)
    for sender, message in zip(senders, messages):
        words[sender] += len(message.split())
    words_list = sorted(words.items(), reverse=True)
    return max(words_list, key=lambda item: item[1])[0]


messages = ['How is Stepik for everyone', 'Stepik is useful for practice']
senders = ['Bob', 'Charlie']

print(best_sender(messages, senders))


# course solution
from collections import defaultdict


def best_sender(messages, senders):
    counts = defaultdict(int)
    for sender, message in zip(senders, messages):
        counts[sender] += len(message.split())
    return max(counts, key=lambda sender: (counts[sender], sender))
