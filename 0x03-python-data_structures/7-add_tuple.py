#!/usr/bun/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_sum = (0, 0)

    if len(tuple_a) < 2 and len(tuple_b) < 2:
        return tuple_sum
    elif len(tuple_a) < 2 and len(tuple_b) >= 2:
        if not tuple_a:
            tuple_sum = (tuple_b[0] + 0, tuple_b[1] + 0)
        else:
            tuple_sum = (tuple_a[0] + tuple_b[0], tuple_b[1] + 0)
    elif len(tuple_a) >= 2 and len(tuple_b) < 2:
        if not tuple_b:
            tuple_sum = (tuple_a[0] + 0, tuple_a[1] + 0)
        else:
            tuple_sum = (tuple_a[0] + tuple_b[0], tuple_a[1] + 0)
    else:
        tuple_sum = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return tuple_sum
