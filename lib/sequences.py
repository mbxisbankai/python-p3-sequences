#!/usr/bin/env python3

def print_fibonacci(length):
    # build the sequence
    if length <= 0:
        seq = []
    else:
        seq = [0]
        if length > 1:
            seq.append(1)
        for _ in range(2, length):
            seq.append(seq[-1] + seq[-2])

    print(seq)

