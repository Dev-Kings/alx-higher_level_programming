#!/usr/bin/python3
"""Moddule containing custom function."""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    filename = "add_item.json"
    data = []
    try:
        data = load_from_json_file(filename)
    except Exception as e:
        pass

    for arg in sys.argv[1:]:
        data.append(arg)

    save_to_json_file(data, filename)
