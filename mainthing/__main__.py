#!/usr/bin/env python3

import signal
import threading
import time
import typing

import mainthing.worker_type1 as worker_type1
import mainthing.worker_type2 as worker_type2
import mylib.state_keeper as state_keeper


def thread_check_loop(all_threads: list) -> None:
    while True:
        time.sleep(20)


def signal_handler() -> None:
    pass


def main(control_event: threading.Event, all_threads: list) -> None:
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)
    thread_lock = threading.Lock()
    s = threading.Thread(
        target=state_keeper.state_keeper
        name=f"state_keeper",
        args=(control_event, thread_lock)
    )
    for worker in (1,2,3):
        t = threading.Thread(
            target=worker_type1.worker_func,
            name=f"worker-1-{worker}",
            args=(control_event, thread_lock)
        )
        all_threads.append(t)
    for worker in (4,5,6):
        t = threading.Thread(
            target=worker_type2.worker_func,
            name=f"worker-2-{worker}",
            args=(control_event, thread_lock)
        )
        all_threads.append(t)
    for t in all_threads:
        t.start()
    thread_check_loop(all_threads)


if __name__ == "__main__":
    global_control_event = threading.Event()
    global_all_threads_list: typing.List[threading.Thread] = []
    main(global_control_event, global_all_threads_list)

