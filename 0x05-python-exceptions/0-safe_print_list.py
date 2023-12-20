#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    y = 0
    for num in range(x):
        try:
            print("{}".format(my_list[num]), end='')
        except IndexError:
            break
        else:
            y += 1
    print()
    return (y)

'''def safe_print_list(my_list=[], x=0):
#use try to printout of num
    y = 0
    for num in range(x):
        try:
            print("{}".format(my_list[num]), end='')
        except:
            break
        else:
            y += 1
    print()
    return (y)
'''