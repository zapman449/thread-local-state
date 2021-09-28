#!/usr/bin/env python3

import threading

import mylib.state_keeper as state_keeper


def worker_func(event: threading.Event, lock: threading.Lock) -> None:
    time.sleep(5)
    x = state_keeper.get_data()
    with lock:
        print(f"worker_type2: {repr(x)}")


if __name__ == "__main__":
    print("please do not call me directly, I am a library")
