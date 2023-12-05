#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    index = 0
    summation = 0
    counter = len(sys.argv)
    if (counter == 1):
        print("{}".format(0))
    elif (counter == 2):
        print("{}".format(int(sys.argv[1])))
    else:
        for arg in sys.argv:
            if (index == 0):
                index += 1
                continue
            else:
                summation += int(sys.argv[index])
                index += 1
        print("{:d}".format(summation))
