import threading


def do_request(card_number: str | int) -> None:
    pass


[threading.Thread(target=do_request, args=[card_num]).start() for card_num in range(4007000000028, 4007000000099 + 1)]
