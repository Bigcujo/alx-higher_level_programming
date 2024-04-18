#!/usr/bin/python3

"""Add all arguments to a python list and save it toa file."""

import sys

if __name__ == "__main__":
    save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

    try:
        things = load_from_json_file("add_item.json")
    except FileNotFoundError:
        things = []
        things.extend(sys.argv[1:])
        save_to_json_file(items, "add_item.json")
