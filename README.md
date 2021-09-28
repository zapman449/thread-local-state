# thread-local-state

How can a worker function in mainthing/worker_type1 access the state data held in mylib/state_keeper.py?
Without passing a reference to either a holding class or other?

I'm missing something.

# Running:

`python3 -m mainthing .`

takes 6-7 seconds to run

Example:

```
❯ python3 -m mainthing .
start 2021-09-28T08:44:28.249062
worker_type1: {'mod_init': 'init 2021-09-28T08:44:28.248849'} 2021-09-28T08:44:31.257434
worker_type2: {'mod_init': 'init 2021-09-28T08:44:28.248849'} 2021-09-28T08:44:31.257657
worker_type2: {'mod_init': 'init 2021-09-28T08:44:28.248849'} 2021-09-28T08:44:31.257937
worker_type1: {'mod_init': 'init 2021-09-28T08:44:28.248849'} 2021-09-28T08:44:31.258065
worker_type2: {'mod_init': 'init 2021-09-28T08:44:28.248849'} 2021-09-28T08:44:31.258190
worker_type1: {'mod_init': 'init 2021-09-28T08:44:28.248849'} 2021-09-28T08:44:31.258297
exit 2021-09-28T08:44:34.259044
```
