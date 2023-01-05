# If you don't have the emoji module, please type in the terminal: py -m pip install emoji~=1.6.3

# Modules
from time import sleep
from modules.functions import *
from modules.checks import *
from modules.style import *
from modules.colors import *

# Banner
banner(color_banner(' Monopoly Banker '))
print(rd('[Type 0 to cancel/return]'))
sleep(1.5)
lin()

# Bank settings
settings = bank_settings()
players = settings[0]
money = settings[1]

# Banker
instructions = 2 # Variable to show red instructions
max_players = len(players) - 1

while True:
    # Panel
    bankrupt = False
    for pos in range(0, len(players)):
        if money[pos] <= 0:
            player_bankrupt = pos
            bankrupt = True
            
    if bankrupt:
        print(rd(f'{players[player_bankrupt]} went bankrupt.'))
        del players[player_bankrupt]
        del money[player_bankrupt]
        sleep(1.5)
        lin()
         
    if len(players) == 2:
        break 

    for pos in range(0, len(players)):
        print(bd(f"{pos:<1} {players[pos]:^15} {money[pos]:>5}"))
    lin()

    # Operations
    while True:
        
        if instructions:
            print(rd('[Always type their number]'))
            sleep(1.5)
            lin()
            instructions -= 1
        
        # Manage?
        while True:
            from_who = check_int(bd('Manage player '))
            if 0 <= from_who <= max_players:    
                lin()
                if instructions:
                    print(rd('[Type the managing player to cancel/return]'))
                    sleep(1.5)
                    lin()
                    instructions -= 1
                break
                
        print(f'{ue("Managing")} {yw(players[from_who])}')
        
        # Receiver and Money
        while True:
            return_cancel = False
            
            # Receiver?
            to_who = check_int(bd('Transfer to '))
            if to_who == from_who:
                return_cancel = True
                break
            
            # Money?
            elif 0 <= to_who <= max_players:
                money_action = check_int(bd('Transfer $ '))
                if money_action == 0:
                    return_cancel = True
                elif money_action > money[from_who]:
                    print(rd(f"{players[from_who]} doesn't have {money_action}."))
                    sleep(1.5)
                    money_action = money[from_who]
                break

        if return_cancel:
            lin()
            break
        
        # Check continue
        lin()
        print(f'$ {bd(money_action)} from {yw(players[from_who])} to {be(players[to_who])} ')
        
        ask = ask_correct()
        if ask == 0:
            lin()
            break
            
        money[from_who] -= money_action
        money[to_who] += money_action
        lin()
        break

# Winner
print(gn(f'The winner is...  '))
sleep(1.5)
print(gn(bd(f' {players[1].center(50)} ')))
lin()
