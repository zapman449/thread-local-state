#!/usr/bin/env python3

import datetime
import threading
import time

import mylib.state_keeper as state_keeper


def worker_func(event: threading.Event, lock: threading.Lock) -> None:
    time.sleep(2)
    x = state_keeper.get_data(event, lock)
    with lock:
        print(f"worker_type1: {repr(x)}", datetime.datetime.now().isoformat())


if __name__ == "__main__":
    print("please do not call me directly, I am a library")
