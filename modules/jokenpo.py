# Here's one of the practices that I did in the course
# If you don't have the emoji module, please type in the terminal: py -m pip install emoji~=1.6.3

# Modules
import emoji
from time import sleep
from random import choice
from modules.checks import checkInt

# Colors
b_yw = '\033[1;43m'
under = '\033[4m'
cc = '\033[m'

# Banner
print(emoji.emojize(f':fist::raised_hand_with_fingers_splayed: :v:  {b_yw} Rock - Paper - Scissors {cc} :v: :raised_hand_with_fingers_splayed: :fist:', use_aliases=True))

# Let's code
while True:
    # User's hand
    print(emoji.emojize(f'[1] {under}Rock{cc} :fist:\n[2] {under}Paper{cc} :raised_hand_with_fingers_splayed:\n[3] {under}Scissors{cc} :v:', use_aliases=True))
    while True:
        hand = checkInt('')
        if 1 <= hand <=3:
            break
        
    # Kalista's hand (computer)
    lista = ['1', '2', '3']
    hand2 = choice(lista)
    
    # Show hand emojis
    emoji_rock = emoji.emojize(':fist:', use_aliases=True)
    emoji_paper = emoji.emojize(':raised_hand_with_fingers_splayed: ', use_aliases=True)
    emoji_scissors = emoji.emojize(':v:', use_aliases=True)
    
    usu = int(hand)
    kali = int(hand2)
    if usu == 1:
        user = emoji_rock
    elif usu == 2:
        user = emoji_paper
    else:
        user = emoji_scissors
    if kali == 1:
        kalista = emoji_rock
    elif kali == 2:
        kalista = emoji_paper
    else:
        kalista = emoji_scissors
        
    # Play
    sleep(.50)
    print('ROCK')
    sleep(.5)
    print('PAPER')
    sleep(.5)
    print('SCISSORS')
    sleep(1)
    print('-' * 50)
    print(f'You chose {user} and I chose {kalista}')
    sleep(2)
    print('It seems that...',end=' ', flush=True)
    sleep(1.5)
    
    # Results - 1 = Rock | 2 = Paper | 3 = Scissors
    usu_won  = (usu == 1 and kali == 3) or (usu == 2 and kali == 1) or (usu == 3 and kali == 2)
    kali_won = (usu == 1 and kali == 2) or (usu == 2 and kali == 3) or (usu == 3 and kali == 1)
    
    if usu == kali:
        print(emoji.emojize("It's a draw... :raised_eyebrow:", use_aliases=True))
    elif usu_won:
        print(emoji.emojize('Grr!! You won. :unamused:', use_aliases=True))
    elif kali_won:
        print(emoji.emojize('Yay!! I won! :grin:', use_aliases=True))
    sleep(.75)
    
    while True:
        ask = checkInt('[0] play again | [9] exit ')
        if ask == 0 or ask == 9:
            break
    if ask == 9:
        break
    print('-' * 50)
    
# Bye
print(emoji.emojize(f'Thanks for playing with me!:smile:', use_aliases=True))
sleep(1)
