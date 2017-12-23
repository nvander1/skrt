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
    keys = (fg, fx, bg)
    tables = (FG_COLORS, FXS, BG_COLORS)
    codes = [table[key] for table, key in zip(tables, keys) if key is not None]
    return ESCAPE + ';'.join(codes) + 'm' + string + ESCAPE + '0m'
