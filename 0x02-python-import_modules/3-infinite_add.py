#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    x = 0
    num = 0
    for i in sys.argv:
        if x != 0:
            i = int(i)
            num = num + i
        x += 1
    print(num)
