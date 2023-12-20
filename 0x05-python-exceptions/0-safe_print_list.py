#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    for num in range(x):
        try:
            print("{}".format(my_list[num]), end='')
        except IndexError:
            print()
            return (num)    
    print()
    return (num + 1)

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