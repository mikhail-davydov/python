from concurrent.futures import ThreadPoolExecutor


def do_request(card_number: str):
    ...


def get_card_number():
    for i in range(801):
        yield str(4007000000100 + i)


with ThreadPoolExecutor(max_workers=15) as pool:
    for card in get_card_number():
        pool.submit(do_request, card)

# alt

with ThreadPoolExecutor(max_workers=15) as pool:
    pool.map(do_request, get_card_number())
