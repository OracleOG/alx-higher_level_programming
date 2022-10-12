#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    x = len(sys.argv) - 1

    if x < 1:
    	print("{} arguments.".format(x))
    elif x == 1:
    	print("{} argument." .format(x))
    else:
    	print("{} arguments." .format(x))

    if x > 0:
        num = 0
        for arg in sys.argv:
            if num != 0:
                print("{}: {}".format(num, (arg)))
            num += 1
