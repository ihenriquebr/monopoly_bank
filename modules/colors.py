# First and Last letter of a color | rd=red - gn=green

def color_banner(msg):
    return f'\033[1;44m{msg}\033[m'


def rd(msg):
    return f'\033[31m{msg}\033[m'


def gn(msg):
    return f'\033[32m{msg}\033[m'

    
def be(msg):
    return f'\033[34m{msg}\033[m'

    
def yw(msg):
    return f'\033[33m{msg}\033[m'


def bd(msg): # Bold
    return f'\033[1m{msg}\033[m'


def ue(msg): # Underline
    return f'\033[4m{msg}\033[m'
