from modules.colors import *

def check_int(num):
    while True:
        try:
            check = int(input(num))
        except (ValueError, TypeError):
            print(rd('ERROR! Invalid number!'))
        except KeyboardInterrupt:
            return 999
        else:
            return check


def check_str(msg):
    while True:
        try:
            check = input(msg).strip().lower().title()
            if not check:
                raise TypeError()
        except (TypeError):
            print(rd('Empty.'))
            continue
        except KeyboardInterrupt:
            return '0'
        else:
            return check
        
