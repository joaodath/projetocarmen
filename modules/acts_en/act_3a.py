from modules.extras import print_slow, clear_screen
from modules.acts_en import endings
from time import sleep

# Starts Act 3 Ending A


def start_3a(player):
    import pygame
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    pygame.mixer.music.load('modules/audio/audio4.ogg')
    pygame.mixer.music.play(-1)
    print(f'''
    {player.name} is on a plane flying to a hiding spot of V.I.L.E in
    the Arctic Cicle. She starts a video call with the villains.''')
    sleep(2)
    clear_screen()
    print('Videocall with V.I.L.E.')
    sleep(1)
    print_slow(f'''
    {player.name}: I'm on my way to the last mission.

    Coach Brunt: Great, sweetheart! And remember: no fooling around.
    Or you'll see minds being wiped.
    
    {player.name}: I'd never dare to think about that...
    ''')
    print('End of videocall with V.I.L.E.')
    sleep(2)
    clear_screen()
    print(f'{player.name} is on a snow jet ski')
    print_slow(f'''
    Player: Approaching the base where Zack and Ivy are being held prisoners.

    {player.name}: Let's take them home!
    ''')
    sleep(2)
    print(f'''
    {player.name} invade o esconderijo. 
    ''')
    
    sleep(2)
    print_slow(f'''
    {player.name}: Player, I'm in.
    ''')
    sleep(2)
    print(f'''
    {player.name} is facing a glass door locked on the inside that 
    she cannot open. Tigress shows up on the other side.
    ''')
    sleep(2)
    print_slow('''
    Tigress: Still wanna know where your friends are locked up?
    ''')

    if player.help_tigress == True:
        return end_helped_tigress(player)
    else:
        return end_not_helped_tigress(player)


def end_helped_tigress(player):
    sleep(1)
    print(f'Tigress opens the door for {player.name}.')
    print_slow(f'''
    {player.name}: Humm… Thank you?

    Tigress: You got me out of that hole.
    Consider this as retribution. But this a one-time only.
    When I face you again, you better be ready!
    ''')

    sleep(1)
    print(f'''
    {player.name} finds the team before their minds were wiped. 
    ''')
    print_slow(f'''
    Ivy: Uhull! The team is back together again!

    Zack: So, now we're gonna get some ice cream?

    {player.name}: In the Arctic?

    Zack: Why not??
    ''')

    sleep(2)
    endings.good_ending_2()
    sleep(10)
    print('Self destruction in 3')
    sleep(1)
    print('Self destruction in 2')
    sleep(1)
    print('Self destruction in 1')
    sleep(1)
    print('Self destruction started')
    sleep(1)
    clear_screen()


def end_not_helped_tigress(player):
    sleep(1)
    print_slow(f'''
    Tigress: Oh, you wanna get inside, isn't it?
    Well, I wanted help to get out of that hole.
    Seems like none of us is getting what we want. 
    ''')

    sleep(1)
    print(f'''
    Tigress pushes the safety lock and a giant iron door
    seals the entire hallway, leaving {player.name}
    on the outside.
    ''')
    sleep(2)
    print(f'''
    {player.name} enters the vents and go straight to where her team is being 
    kept. She thinks she saved her team before their minds were wiped, 
    but soon she finds out she is wrong. Zack and Ivy spent too much time on 
    the machine, their minds is irreparably reprogrammed. 
    They capture {player.name} for V.I.L.E.
    ''')

    sleep(2)
    clear_screen()
    endings.bad_ending_4()
    sleep(10)
    print('Self destruction in 3')
    sleep(1)
    print('Self destruction in 2')
    sleep(1)
    print('Self destruction in 1')
    sleep(1)
    print('Self destruction started')
    sleep(1)
    clear_screen()
