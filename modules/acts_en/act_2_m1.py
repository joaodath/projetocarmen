from modules.acts_en import endings
from modules.extras import print_slow, check_input, clear_screen, check_sucess
from time import sleep

# Starts Mission 1 from Act 2


def start_m1(player):
    import pygame
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    pygame.mixer.music.load('modules/audio/audio2.ogg')
    pygame.mixer.music.play(-1)
    player.missions_up(1)
    clear_screen()

    sleep(2)
    print_slow(f'''
    After the mission in Shanghai, {player.name} receives a call from the V.I.L.E

    {player.name}: Okay Countess Cleo. What does your dark heart desire?
    Countess Cleo: For my mission, I want you to steal the last batch of a
    Beluga caviar. It will be served at a charity party in Monaco. 

    Player:Located on the French Riviera, Monaco is the second
    smallest country in the world. The party will take place at a luxury hotel in Monte Carlo.
    
    {player.name} travel to the place, with the goal to achieve the mission. 
    ''')

    sleep(2)
    return party(player)


def party(player):
    clear_screen()
    # Storytelling
    print(f'''
    {player.name} arrives at the party.
    The host sees her and goes to meet her''')

    sleep(2)
    print_slow(f'''
    Party Host: Would you give me the honor of this dance, Miss...?

    {player.name}: Santa Rosa! Miss. Santa Rosa.

    Party Host: Would you give me the honor of this dance, Miss Santa Rosa?

    {player.name}: I'm on a mission, so I should concentrate and refuse.
    But accepting the dance might be the best way to blend in and
    get to the kitchen. 
    ''')
    sleep(3)

    clear_screen()
    text = f'''
   Should I dance or go ahead with the plan?

    [1] To dance
    [2] To refuse the dance

    Your choice: '''

    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return dance(player)
    else:
        sleep(1)
        return refuse_dance(player)


def dance(player):
    clear_screen()
    player.persuasion_op(+1)
    player.energy_op(-1)

    print_slow(f'''
    ------------
    {player.name} participates in a beautiful dance with the Host of the Party.
    This helps her blend in on the spot.
    Persuação: +{player.persuasion} [+1]
    Energia: +{player.energy} [-1]
    ------------
    .....
    ''')
    sleep(3)

    return talking_with_julia(player)


def refuse_dance(player):
    clear_screen()
    player.persuasion_op(-1)

    print_slow(f'''
    {player.name} : Thanks, but waltz is not my thing. if you want to dance
    tango...

    The Host cordially says goodbye and leaves.
    ------------
    Oops! Sometimes it's good to make some sacrifices
    to blend in place...

    Persuação: +{player.persuasion} [-1]
    ------------
    ....
    ''')
    sleep(3)

    return talking_with_julia(player)


def talking_with_julia(player):
    clear_screen()
    print(f'''
    {player.name} is approached by another ACME agent.''')
    sleep(2)

    print_slow(f'''
    Julia: {player.name}?

    {player.name}: Don't you mean Scarlet Santa Rosa?

    Julia: Yes of course. It's good to see you again Miss Sta Rosa.
    I can assume why you are here. We heard that a V.I.L.E agent
    is behind Beluga caviar. I bet you're here to get them
    before they steal it.

    {player.name}: Yeah… something like that.

    Julia: I'm sure you already knew about the recent theft of the Chinese warrior from
    terracotta. I would be relieved if a stolen treasure turned up in the
    my door and allow me to return it to the authorities.

    Player: Only this time the delivery will be made to V.I.L.E and not to ACME.

    {player.name}: Maybe I can explain that to her.

    Player: Can we trust Julia?
    ''')
    sleep(3)

    clear_screen()
    text = f'''
    {player.name}: ~ I have allied with her before.
    Trusting her might work again.
    But, if V.I.L.E knows that I am in collusion with ACME,
    who knows what they will do? ~

    [1] Trust Julia
    [2] Wrap Julia

    '''
    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return trust_julia(player)
    else:
        sleep(1)
        return not_trust_julia(player)


def trust_julia(player):
    clear_screen()
    print_slow(f'''
    {player.name}: Julia, listen.
    I'm the agent sent to steal the Beluga caviar.

    Julia: I do not understand. Why would you steal for V.I.L.E?

    {player.name}: That's all I can say now.
    I ask you to trust my reasons.


    Julia: For good reasons, Miss Santa Rosa.
    ''')
    print('''
    Julia will remember that you trusted her.''')
    player.trust_julia = 1
    sleep(3)
    return steel_caviare(player)


def not_trust_julia(player):
    clear_screen()
    print_slow(f'''
    {player.name}: Julia, listen. You are right to be suspicious.
    I need to show you something.
    ''')
    print(f'''
    {player.name} head to the stairs with Julia.''')
    sleep(2)
    print_slow(f'''
    {player.name}: The V.I.L.E. is standing by on the roof now.
    We have to act fast! Come on! We do not have much time!
    ''')
    print(f'''
    Julia tries to call for backup using her spy pen but {player.name}
    takes her hand quickly as she passes through the door leading to the roof.
    ''')
    sleep(3)
    print(f'''
    {player.name} locks Julia on the roof.''')
    sleep(2)
    print_slow(f'''
    {player.name}: Sorry, Julia. Really.''')
    print('''
    Julia will remember that you didn't trust her.''')
    sleep(2)
    player.trust_julia = 0
    return steel_caviare(player)


def steel_caviare(player):
    clear_screen()
    print(f'''
    {player.name} observe two waiters going to the kitchen ''')
    
    sleep(2)

    print_slow (f'''
    {player.name}: I saw the roe.
    
    Player: How will you get it?

    {player.name}: I can hide and sneak out,
    or pick it up and run away. ''')
    sleep(3)

    clear_screen()
    text = f'''
    Do I disguise and hide the caviar or steal and run?
    
    [1] Disguise and Capture
    [2] Steal and Run
    
     Your choice: '''

    if check_input(text, [1, 2]) == 1:
        clear_screen()

        print_slow(f'''
    ------------
    Good choice! However, you'll need luck for the cover to be a
    according to plan.

    Luck: +{player.lucky}
    ------------
    ....
        ''')
        sleep(2)

        if check_sucess(player.lucky) == True:
            sleep(1)
            return hide(player)
        else:
            clear_screen()
            print(f'''
    Unfortunately the disguise didn't work out very well... A waiter recognized you!
            ''')
            sleep(3)
            return run(player)
    else:
        sleep(1)
        return run(player)


def hide(player):
    clear_screen()

    print(f'''
    {player.name} disguises herself as a waitress to capture the caviars. However, an unforeseen event happens!
     As there was time for the disguise, the caviars have already been removed from their cans,
     being served on plates!
    ''')

    sleep(2)
    print(f'''
    {player.name} captures the caviars from the dishes and puts them in a bowl and sneaks away. After
     leave the party, get in touch with Countess Cleo.
    ''')

    sleep(2)
    clear_screen()
    print_slow(f'''
    {player.name}: The caviar is served.

    Countess Cleo: How rude! Out of the cans, left the delicacy exposed!

    {player.name}: You wanted fish eggs, I delivered.
    
    Condessa Cleo:  Countess Cleo: That's what you did. But now they will only last a day! And I can't consume a hundred cans of
     caviar in one day. Dr Bellum, activate the... whatever the name of it is today!

    {player.name}: No!
    ''')

    sleep(2)
    print(f'''
    Guards appear at the prison where {player.name}'s friends are.
    They try to fight but it's in vain. Your minds will be erased.''')
    sleep(3)

    clear_screen()
    print_slow(f'''
    ------------
    OH NO! We seem to be in a big impasse.
    Time to test your limits!
    You will try to convince Countess Cleo to save her friends.
    
    Persuasion: +{player.persuasion}
    ------------
    .....
    ''')
    sleep(2)

    if check_sucess(player.persuasion) == True:
        clear_screen()
        print_slow(f'''
    {player.name} begs for a new opportunity.

    {player.name}: Please give me another chance! I promise I will give
    my utmost to be discreet. After all, I'm the best option you have.
    
    Countess Cleo reluctantly states.

    Countess Cleo: All right! But this will be your last try! wait for new
    instructions.
        ''')
        sleep(2)
        return steel_again(player)

    else:
        clear_screen()
        print(f'''
    {player.name} begs for a new opportunity.
    ''')
        print_slow(f'''
    {player.name}: Please, give me another chance! I promise I'll do my best 
    to try and be discrete. After all, I'm your best option. 

    Countess Cleo: Not in a million years! Only a fool would trust the words
    of a thief.
    Continue with the wipe out!
        ''')
        sleep(2)
        endings.bad_ending_5()


def run(player):
    clear_screen()

    print(f'''
    {player.name} comes out of the kitchen with a cart with caviar
    ''')

    print_slow(f'''
    Waitress yells from the kitchen: Mademoiselle, stop!
    The caviar needs to be plated!

    Host: Get her!

    {player.name}: I prefer the dramatic output.
    ''')
    print(f'''
    {player.name} grabs the caviar, kicks the cart, and jumps the glider.
    ''')
    sleep(3)

    clear_screen()
    print(f'{player.name} calls Countess Cleo.')
    sleep(2)

    print_slow(f'''
    {player.name}: I got the Beluga babies.

    Countess Cleo: Please wait for further instructions.
    ''')
    sleep(2)

    return steel_again(player)


def steel_again(player):
    print(f'''
    {player.name} chats with Player without Countess Cleo being able to hear.
    ''')
    sleep(3)

    print_slow(f'''
    {player.name}: Player, any leads on Zac and Ivy?

    Player: Not yet. I'm looking but nothing yet.
    Stay on call with Countess Cleo for a few more seconds,
    I'm trying to track down.
    ''')
    sleep(2)

    print('''
    Countess Cleo looks stressed on the call.
    ''')
    sleep(3)

    print_slow(f'''
    Countess Cleo: Talking to anyone else, {player.name}?
    Apparently I'm disturbing something.
    You must have matters more important than your team's life.

    {player.name}: None of that, Countess!
    I'm just in awe of the sophistication of your look today.

    Player: {player.name}, I found a sign!
    Searching for V.I.L.E hideouts in the Arctic Circle.
    I found a. What do you want to do?

    {player.name}: ~ I can try to rescue my team now or I can steal
    for the V.I.L.E. one last time. A new mission can be risky,
    but it can also be a chance to keep up the appearances until I recover 
    the team. ~
    ''')
    sleep(3)

    text = f'''
    Do I start a risky rescue mission, or robbery for the last time?

    [1] Rescue Team
    [2] Steal one last time
    
    Your choice: '''

    if check_input(text, [1, 2]) == 1:
        sleep(1)
        from modules.acts_pt import act_3a
        return act_3a.start_3a(player)  # Used to be a Good Ending
    else:
        if player.missions_count() == 2:
            clear_screen()
            print_slow(f'''
            All missions have been cleared. 
            Proceding to rescue of the team now...

            ''')
            from modules.acts_pt import act_3a
            return act_3a.start_3a(player)
        else:
            from modules.acts_pt import act_2_m2
            return act_2_m2.start_m2(player)  # Used to be Bad Ending 4
