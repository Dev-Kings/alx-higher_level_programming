#!/usr/bin/python3
if __name__ == "__main__":
    import variable_load_5
    for n in dir(variable_load_5):
        if n == 'a':
            print("{}".format(variable_load_5.a))
            break
