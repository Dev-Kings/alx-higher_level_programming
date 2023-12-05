#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    index = 0
    counter = len(sys.argv) - 1
    if (counter > 1):
        print("{} arguments:".format(counter))
    for arg in sys.argv:
        if (counter == 0):
            print("{} arguments.".format(0))
            break
        elif (counter == 1):
            print("{} argument:".format(1))
            print("{}: {}".format(1, sys.argv[1]))
            break
        else:
            if (index == 0):
                index += 1
                continue
            index += 1
            print("{}: {}".format(index - 1, sys.argv[index - 1]))
