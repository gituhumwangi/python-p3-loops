#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    pass
    i = 10
    while i > 0 :
        print(i)
        i -= 1
        if i == 0:
            print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    pass
    int_list = [num**2 for num in int_list]
    return int_list

def fizzbuzz():
    # code goes here!
    pass
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(f"{i}")
        



print(fizzbuzz())

