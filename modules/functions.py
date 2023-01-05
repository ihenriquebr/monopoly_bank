from time import sleep
from modules.style import *
from modules.checks import *
from modules.colors import *

# Ask if correct
def ask_correct():
    while True:
        ask = check_int(bd("Correct? [1] Yes | [0] No "))
        if 0 <= ask <= 1:
            return ask

# Functions in 'Bank settings'
def players_names(num):
    names = []
    
    for pos in range(1, num+1):
        while True:
            name = check_str(bd(f'{pos}{f"st Player Name: [Max 10 characters]" if pos == 1 else "nd Name:" if pos == 2 else "th:"} '))
            if len(name) <= 10:
                break
        if name in '0':
            names = 0
            break
    
        names.append(name)
    return names


# Bank settings
def bank_settings():
    while True:
        # Number of Players
        num_players = check_int(bd('How many players? '))
        
        if num_players == 0:
            continue
        elif num_players == 1:
            print(yw("You can't play alone."))
            continue
        lin()
        
        # Names
        players = players_names(num_players)
        
        if players == 0:
            lin()
            continue

        # Money
        lin()
        start_money = check_int(bd('Start money: '))
        
        if start_money <= 0:
            lin()
            continue
        
        # Check if continue
        lin()
        print(f'There are {yw(f"{num_players} players")}. Their names are ', end='')
        
        for n, name in enumerate(players):
            print(f'{yw(name)}{" and " if n+2 == num_players else ". " if n+2 > num_players else ", "}', end='')
            
        print(f'The start money is {yw(start_money)}. ')
            
        ask = ask_correct()
        if ask == 0:
            lin()
            continue
        
        lin()
        
        # Money settings
        players.insert(0, 'Bank') # Bank in the first position of the players list
        money = []
        
        for pos in range(0, num_players+1):
            if pos == 0:
                money.append(start_money * num_players)
            else:
                money.append(start_money)
                
        print(gn("Everything set up!! Let's begin!"))
        sleep(1.5)
        lin()
        return players, money
    
