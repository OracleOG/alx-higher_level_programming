#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    my_list = dir(hidden_4)

    for i in my_list:
        if i[0] != '_' and i[1] != '_':
            print(i)
