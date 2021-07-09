from modules.acts_en import endings
from modules.extras import print_slow, check_input, clear_screen
from time import sleep

#Starts Mission 1 from Act 2
def start_m1(player):
    clear_screen()
    sleep(1)
    return party(player)


def party(player):
    clear_screen()
    #Storytelling
    print(f'''
    After the mission in Shanghai, {player.name} receives a call from the V.I.L.E''')
    print_slow(f'''
    {player.nome}: Okay Countess Cleo. What did your dark heart desires?
     Countess Cleo: For my mission, I want you to steal the last batch of a
     Beluga caviar. It will be served at a charity party in Monaco. ''')
    sleep(1)
    clear_screen()
    print_slow(f'''
    Player:Located on the French Riviera, Monaco is the second
    smallest country in the world. The party will take place at a luxury hotel in Monte Carlo.

    {player.nome}: I'll mingle myself, locate the cans, and then steal them.
    ''')
    print(f'''
    {player.nome} arrives at the party.
    The host sees her and goes to meet her''')
    
    sleep(1)
    print_slow(f'''
    Party Host: Would you give me the honor of this dance, Miss...?

    {player.nome}: Santa Rosa! Miss. Santa Rosa.

    Party Host: Would you give me the honor of this dance, Miss Santa Rosa?
    ''')
    text = f'''
    {player.nome}: I'm on a mission, so I should concentrate and refuse.
    But accepting the dance might be the best way to blend in and
    get to the kitchen.

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
    print_slow(f'''
    ------------
    {player.name} participates in a beautiful dance with the Host of the Party.
    This helps her blend in on the spot.
    Persuação: +{player.persuasion} [+1]
    Energia: +{player.energy} [-1]
    ------------
    .....
    ''')
    clear_screen()
    sleep(1)
    return steel_caviare(player)


def refuse_dance(player):
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
    clear_screen()
    sleep(1)
    return steel_caviare(player)


def steel_caviare(player):
    clear_screen()
    import pygame
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    pygame.mixer.music.load('modules/audio/audio2.ogg')
    pygame.mixer.music.play(-1)
    #Storytelling
    print(f'''
    {player.nome} observe two waiters going to the kitchen ''')
    print_slow(f'''
    {player.nome}: I saw the roe.
    
    Player: How will you get it?
    ''')
    text = f'''
    {player.name}: I can hide and sneak out,
     or pick it up and run away.
    
     Do I disguise and hide the caviar or steal and run?
    
     [1] Disguise and Capture
     [2] Steal and Run
    
     Your choice: '''

    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return hide(player)
    else:
        sleep(1)
        return run(player)


def hide(player):
    clear_screen()
    print_slow(f'''
   {player.name} disguises himself as a waiter to capture the caviars. However, an unforeseen event happens!
     As there was time for the disguise, the caviars have already been removed from their cans,
     being served on plates!
    
     {player.name} captures the caviars from the dishes and puts them in a bowl and sneaks away. After
     leave the party, get in touch with Countess Cleo.
    
     Carmen: The caviar is served.

     Countess Cleo: How rude! Out of the cans, left the delicacy exposed!

     Carmen: You wanted fish eggs, I delivered.
    
     Countess Cleo: That's what you did. But now they will only last a day! And I can't consume a hundred cans of
     caviar in one day. Dr Bellum, activate the... whatever the name of it is today!

     Carmen: No!
    ''')
    sleep(1)
    print(f'''
    {player.name} dresses up as a waitress.
     She watches the V.I.L.E mime eating something.
    ''')
    
    sleep(1)
    print_slow(f'''
    {player.name}: It's out of character. You should eat invisible snacks.
    ''')

    sleep(0.5)
    print('The man starts to feel sick.')

    sleep(0.5)
    print_slow(f'''
    {player.name}: I think the mime is not okay.

   Player: I'm not surprised. Mimes are not funny.

     {player.name}: It's not a trick. He really choked!

     Player: What are you going to do? If you helps you might miss the caviar.

     {player.name}: This time, there's only one choice.
    ''')
    
    sleep(0.5)
    print(f'''
    {player.name} helps him.
     Upon arriving in the kitchen, the delicacy has already been served.
    ''')
    
    sleep(0.5)
    print_slow('''
    Host: And now, for the main course, I present the Beluga caviar.
    Bon apetit! 
    Hã???
    ''')
    print('The caviar is not in the tray. \n')
    print_slow('Host: The Beluga! Where did it go?')

    sleep(1)
    clear_screen()
    print(f'''
    {player.name}escapes and is walking down the street talking to the
     Countess Cleo by video call.
     ''')
    print_slow(f'''
     {player.name}: Caviar served, ma'am.

     Countess Cleo: How rude. Out of the cans, left the delicacy exposed.

     {player.name}: You wanted the caviar. I delivered.

     Countess Cleo: It's true. But now they can only be eaten for one day.
     And I can't consume a hundred cans of caviar in a day.
     Dr Bellum, activate the...whatever the name of this is today.

    {player.name}: NO! 
    ''')
    
    sleep(0.5)
    print(f'''
    Guards appear at the prison where {player.name}'s friends are.
    They try to fight but it's in vain. Their minds are erased.''')
    
    sleep(1)
    clear_screen()
    print_slow('''
    Narrator: What is this? Zac and Ivy ended up with their minds erased?
    Unacceptable! I'll reopen this case so you can review
    the choices you made.
    ''')
    sleep(1)
    print('''
    You will return to the last choice and you will be able to
    try a different path''')
    sleep(2)
    return steel_caviare(player) #Used to be Bad Ending 5


def run(player):
    clear_screen()
    print(f'{player.name} leaves the kitchen with a cart with caviar')
    print_slow(f'''
     Waitress yells from the kitchen: Mademoiselle, stop!
     The caviar needs to be plated!

     Host: Get her!

     {player.name}: I prefer the dramatic output.
     ''')
    print(f'''
     {player.name} grabs the caviar, kicks the cart, and jumps the glider.
     ''')

    sleep(0.5)
    clear_screen()
    print(f'{player.name} calls Countess Cleo.')
    print_slow(f'''
    {player.name}: I got the Beluga babies.

     Countess Cleo: Please wait for further instructions.
     ''')
    print(f'''
     {player.name} chats with Player without Countess Cleo being able to hear.
     ''')
    print_slow(f'''
     {player.name}: Player, any leads on Zac and Ivy?

     Player: Not yet. I'm looking but nothing yet.
     Stay on call with Countess Cleo for a few more seconds,
     I'm trying to track down. ''')

    sleep(0.5)
    print('Countess Cleo looks stressed on the call.')
    print_slow(f'''
     Countess Cleo: Talking to anyone else, {player.name}?
     Apparently I'm disturbing something.
     You must have matters more important than your team's life.

     {player.name}: None of that, Countess!
     I'm just in awe of the sophistication of your look today.

     Player: {player.name}, I found a sign!
     Searching for V.I.L.E hideouts in the Arctic Circle.
     I found one. What do you want to do?
    ''')
    
    sleep(2)
    clear_screen()
    text = f'''
    {player.nome}: I can try to rescue my team now or I can steal
     one last time. A new mission can be risky, but it can also be 
     a chance to keep up appearances until I get  to recover my team.

     Do I start a risky rescue mission, or steal for the last time?

     [1] Rescue Team
     [2] Steal one last time
    
     Your choice: '''
    
    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return rescue_team(player)
    else:
        sleep(1)
        from modules.acts_pt import act_2_m2
        return act_2_m2.start_m2(player) #Used to be Bad Ending 4


def rescue_team(player):
    clear_screen()
    sleep(1)
    return endings.good_ending_1(player) #Must be Act3a or Act3b
