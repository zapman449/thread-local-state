#!/usr/bin/env python3

import threading
import typing

# module global variable?
my_state = dict()


def state_keeper(event: threading.Event, lock: threading.Lock) -> None:
    with lock:
        my_state["foo"] = "bar"


def get_data(event: threading.Event, lock: threading.Lock) -> typing.List:
    return list(my_state.values())


if __name__ == "__main__":
    print("please do not call me directly, I am a library")
