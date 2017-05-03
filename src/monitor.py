import os

import curses
from curses import wrapper

def main(stdscr):

    stdscr.refresh()
    stdscr.getkey()

def filename_gen(top_dir):
    for dirpath, _, filenames in os.walk(top_dir):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))

if __name__ == "__main__":
    stdscr = curses.initscr()
    wrapper(main)
