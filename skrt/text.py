"""This module implements utilities for manipulating text.

* color    add ansi colors and styles to strings
"""


FG_COLORS = {
    'black' : '30',
    'red' : '31',
    'green' : '32',
    'yellow' : '33',
    'blue' : '34',
    'purple' : '35',
    'cyan' : '36',
    'white' : '37',
}

FXS = {
    'normal' : '0',
    'bold' : '1',
    'underline': '4',
}

BG_COLORS = {
    'black' : '40',
    'red' : '41',
    'green' : '42',
    'yellow' : '44',
    'blue' : '44',
    'purple' : '45',
    'cyan' : '46',
    'white' : '47',
}


ESCAPE = '\033['


def color(string, fg=None, fx=None, bg=None):
    """Changes the color and style of a string to be printed in a terminal.

    Parameters
    ----------
    string : str
        The text to colorize.
    fg : str
        The text color (e.g. 'red', 'cyan', 'black', 'yellow', etc.).
    fg : str
        The text style (e.g. 'normal', 'bold', and 'underline').
    bg : str
        The background color (e.g. 'red', 'cyan', 'black', 'yellow', etc.).
    """
    keys = (fg, fx, bg)
    tables = (FG_COLORS, FXS, BG_COLORS)
    codes = [table[key] for table, key in zip(tables, keys) if key is not None]
    return ESCAPE + ';'.join(codes) + 'm' + string + ESCAPE + '0m'
