#!/usr/bin/python3

import os
import sys
from time import sleep

import curses
from curses import wrapper

#def main(stdscr):
def main():

    snapshot = {(filename, os.path.getmtime(filename))
                for filename in abs_files(sys.argv[1])}

    while True:
        new_snapshot = {(filename, os.path.getmtime(filename))
                        for filename in abs_files(sys.argv[1])}
        new_files = new_snapshot - snapshot
        missing_files = snapshot - new_snapshot
        if new_files:
            print(new_files)

        snapshot = new_snapshot
    #stdscr.refresh()
    #stdscr.getkey()


def abs_files(top_dir):
    for dirpath, dirnames, filenames in os.walk(top_dir):
        for f in filenames:
            abs_filename = os.path.join(dirpath, f)
            if not os.path.islink(abs_filename):
                yield os.path.abspath(os.path.join(dirpath, f))

if __name__ == "__main__":
    #stdscr = curses.initscr()
    #wrapper(main)
    main()
