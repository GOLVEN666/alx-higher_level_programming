#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz ", end="", sep=" ")
        elif x % 3 == 0:
            print("Fizz ", end="", sep=" ")
        elif x % 5 == 0:
            print("Buzz ", end="", sep=" ")
        else:
            print(f"{x} ", end="", sep=" ")
