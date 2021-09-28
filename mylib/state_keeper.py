#!/usr/bin/env python3

import copy
import datetime
import threading
import typing

# module global variable?
my_state = dict()
init_time = f"init {datetime.datetime.now().isoformat()}"
my_state["mod_init"] = init_time


def state_keeper(event: threading.Event, lock: threading.Lock) -> None:
    with lock:
        skt = f"skt {datetime.datetime.now().isoformat()}"
        print("my_state init_time:", skt)
        my_state["func_init"] = skt


def get_data(event: threading.Event, lock: threading.Lock) -> typing.List:
    return copy.deepcopy(my_state)


if __name__ == "__main__":
    print("please do not call me directly, I am a library")
