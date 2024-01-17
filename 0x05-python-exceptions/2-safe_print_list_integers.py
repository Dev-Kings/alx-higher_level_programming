#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    while i < x:
        count += 1
        try:
            print("{:d}".format(my_list[i]), end="")
        except IndexError:
            raise IndexError from None
        except ValueError:
            count -= 1
            pass
        except Exception:
            count -= 1
            pass
        i += 1
    print()
    return (count)
