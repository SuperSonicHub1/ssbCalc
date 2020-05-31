#!/usr/bin/env python3

import sys

print("Welcome to Kyle's simple script-based calculator!")

int_1 = input("First number? ")

try:
    int_1 = int(int_1)
except ValueError:
    sys.exit("You must enter an integer.")

add_list = ["+", "plus", "addition"]
sub_list = ["-", "minus", "subtraction"]
multi_list = ["*", "times", "multiplication"]
div_list = ["/", "divided by", "division"]
op_list = add_list + sub_list + multi_list + div_list

operation = input("What operation? ")
if operation in op_list:
    pass
else:
    sys.exit("You must enter an operation.")

int_2 = input("Second number? ")

try:
    int_2 = int(int_2)
except ValueError:
    sys.exit("You must enter an integer.")

answer = ""

if operation in add_list:
    answer = int_1 + int_2
    operation = add_list[1]

if operation in sub_list:
    answer = int_1 - int_2
    operation = sub_list[1]

if operation in multi_list:
    answer = int_1 * int_2
    operation = multi_list[1]

if operation in div_list:
    answer = int_1 / int_2
    operation = div_list[1]

sentence = f"{int_1} {operation} {int_2} equals {answer}."
sys.exit(sentence)
