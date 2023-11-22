#!/usr/bin/env python3

def print_fibonacci(length):
    list = []
    if length > 0:
        list.append(0)
        if length > 1:
            list.append(1)
    for i in range(2, length):
        last_two_sum = list[-1] + list[-2]
        list.append(last_two_sum)
    print(list)
    