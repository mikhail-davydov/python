def crypter(text: str) -> tuple[str, float]:
    if text == "Hello From":
        _crypter, _score = "f4561bc239", 10.12
    elif text == "my":
        _crypter, _score = "3c", 35.07
    else:
        _crypter, _score = "129a99cd27", 2.19
    return _crypter, _score


text_blocks = ("Hello From", "oh noo, it's too big!!!!!", "my")

from multiprocessing import Process, Pipe

import struct
from multiprocessing.connection import Connection


def sender(conn: Connection, text: str) -> None:
    text, score = crypter(text[:10])
    data = bytearray(text.encode()) + bytearray(b"\x20" * (10 - len(text))) + struct.pack("d", score)
    conn.send_bytes(data)


if __name__ == "__main__":
    _buffer = bytearray(b"\x00" * len(text_blocks) * 18)
    pipes = [Pipe() for _ in range(len(text_blocks))]

    for text, connects in zip(text_blocks, pipes):
        Process(target=sender, args=(connects[0], text)).start()

    for i, connects in enumerate(pipes):
        connects[-1].recv_bytes_into(_buffer, i * 18)

    # допиши здесь, там немного осталось, распарсь буфер в терминал
    for i, text_block in enumerate(text_blocks):
        start = 18 * i
        middle = start + 10
        stop = middle + 8
        print(
            f'text={text_block}; cipher={_buffer[start:middle].decode().strip()}; score={struct.unpack('d', _buffer[middle:stop])[0]}',
        )

# alt

    for offset, text in enumerate(text_blocks):
        offset *= 18
        cipher, score = struct.unpack('<10sd', _buffer[offset:offset + 18])
        cipher = cipher.decode().rstrip()
        print(f'text={text}; cipher={cipher}; score={score}')