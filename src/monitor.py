#!/usr/bin/python3

import os
import sys

import curses
from curses import wrapper

def main(stdscr):

    files = abs_files(sys.argv[1])

    # stdscr.refresh()
    # stdscr.getkey()
    print(sys.argv[1])

def abs_files(top_dir):
    for dirpath, dirnames, filenames in os.walk(top_dir):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))

if __name__ == "__main__":
    print(sys.argv[1])
    stdscr = curses.initscr()
    wrapper(main)
