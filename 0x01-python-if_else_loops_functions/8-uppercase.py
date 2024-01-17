#!/usr/bin/python3
def uppercase(str):
    for x in str:
        convr = ord(x)
        if convr in range(97, 123):
            convr = convr - 32
        print("{:c}".format(convr), end="")
    print()
