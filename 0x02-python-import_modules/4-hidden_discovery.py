#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    name_list = []
    for name in dir(hidden_4):
        first_two_chars = '__'
        if first_two_chars == name[:2]:
            continue
        else:
            name_list.append(name)
    for n in name_list:
        print("{}".format(n))
