#!/usr/bin/env python
from random import randint

mysterious_num = 1
num_input = int(raw_input())
num_list = []

for number in range(num_input):
    num_list.append(randint(0,20))

print num_list


while mysterious_num == 0:
    for bug in range(1,num_input):
        if num_list[bug-1] > num_list[var]:
            t1 = num_list[bug-1]
            t2 = num_list[bug]
            num_list[bug-1] = t2
            num_list[bug] = t1
            mysterious_num = 1


print num_list
