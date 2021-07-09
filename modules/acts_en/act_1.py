from modules.acts_en import endings
from modules.extras import print_slow, check_input, clear_screen, check_sucess
from time import sleep

#Starts the game from act 01
def start(player):
    clear_screen()
    import pygame
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    pygame.mixer.music.load('modules/audio/audio1.ogg')
    pygame.mixer.music.play(-1)
    #Storytelling
    print_slow(f'''
    Player: Xangai´s skyline sports several of the world´s tallest skyscrapers, 
    including one of V.I.L.E.´s most notorious strongholds. 
    
    You can go, {player.name}!
    The last floor is where you gonna find the vault.

    {player.name}: And the newly stolen items from the V.I.L.E. that will be
    in this vault. Zack, Ivy, are you in position?

    Ivy: The entire perimeter is covered, {player.name}!
    ''')
    sleep(1)
    return building(player)


def building(player):
    clear_screen()
    #Storytelling
    print_slow(f'''
    {player.name}: The building is definitely full of security guards.
    What's the best route to the vault?
    
    Player: You can go in by the last floor or you can go by the first floor.
    
    {player.name}: Going by the last floor certainly will demand risky 
    maneuvers but by using the first floor, I may face oposition.     
    ''')
    sleep(2)
    text = f'''
    To find out what V.I.L.E. is hiding, I need to enter this tower.

    What´s your choice? 

    [1] Last floor
    [2] First floor
    
    Your choice: '''

    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return top_building(player)
    else:
        sleep(1)
        return bottom_building(player)


def top_building(player):
    sleep(2)
    clear_screen()
    #Storytelling
    print(f'''
    {player.name} reaches the top of a nearby building and prepares herself 
    to fly using a zipline to reach the
    V.I.L.E's building.
    ''')
    
    sleep(3)
    print_slow(f'''
    {player.name}: I'll go gliding!''')
    
    sleep(3)
    print(f'''
    {player.name} uses a laser to cut through the window glass
    of the building and enter. She falls into the janitor's closet.''')
    
    sleep(3)
    print_slow(f'''
    {player.name}: The janitor's closet???

    Player: You asked for the "cleanest" route! 

    {player.name}: Just show me the path to the vault.
    ''')
    
    sleep(3)
    print(f'''
    Player sends the route to {player.name}.''')
    sleep(5)

    return text_vile_vault(player)


def bottom_building(player):
    clear_screen()
    #Storytelling
    print(f'''
    {player.name} is going up to the vault floor
    using the elevator shaft.
    ''')

    sleep(5)
    print_slow(f'''
    Player: You really know how to get in with style, {player.name}!!

    {player.name}: Better than smiling for the elevator cameras.
    I will be careful with the gap.
    ''')

    sleep(3)
    print(f'''
    {player.name} forces the elevator´s door  open and come face to 
    face with the guards. She fights with them and wins. 
    ''')
    sleep(3)
    player.energy_op(-1)

    print_slow(f'''

    ------------
    Winning this fight took a toll on you.

    Energy: +{player.energy} (-1)
    ------------

    ''')

    sleep(3)
    print_slow(f''' {player.name}: Player, guide me. \n''')
    sleep(2)
    print(f'''Player sents the route to {player.name}.''')
    sleep(5)

    return text_vile_vault(player)


def text_vile_vault(player):
    sleep(5)
    clear_screen()
    #Storytelling
    print_slow(f'''
    {player.name}: Safe located. Too easy …''')

    sleep(3)
    print(f''' 
    The safe is empty, except for a little tablet in a pedestal 
    in the center of the safe´s room. {player.name} goes in and can hear 
    the V.I.L.E.´s leaders speaking
    ''')

    sleep(2)
    print_slow(f'''
    Maelstrom: Welcome, {player.name}! Please, make your self at home. 
    ''')

    sleep(2)
    print(f'''
    {player.name} touches on the tablet and a big screen apppears in the safe 
    with all V.I.L.E's leaders. 
    ''')
    
    sleep(2)
    print_slow(f'''
    {player.name}: Well, well. All my former crime school instructors!

    Maelstrom: You are without a doubt the best thief who has ever been through the
    hallways of the V.I.L.E. Academy

    Countess Cleo: Although we never picked the fruits of we've taught every 
    stealing skill you know.

    Dr. Bellum: So, today we can finally play
    "{player.name}: V.I.L.E's agent."

    {player.name}: Can we skip to the part where I say no?
    
    Coach Brunt: Oh, not even to save your fearless helpers?
    ''')
    
    sleep(2)
    print('''The screen shows Ivy and Zack,
    tied up somewhere hard to understand where it is.''')
    sleep(2)
    return vile_vault(player)

def vile_vault(player):
    sleep(3)
    clear_screen()
    print_slow(f'''
    Dr. Bellum: Refuse to play our game and I swear we'll erase their memory 
    and we will reprogram your team to become V.I.L.E. agents!

    Player: {player.name}: I found Zack and Ivy's van on a street camera.
    It's on the move. Do you think you can reach it? 

    {player.name}: I can try to save Zack and Ivy right now, but it would be 
    dangerous. Or, I can accept stealing for V.I.L.E. until I figured out a 
    way to get my team back.
    ''')
    sleep(2)

    text = f'''  
    What do I do?
    I need to get them back safely somehow.

    [1] Rescue team
    [2] Stealing a Terracotta Warrior
    
    Your choice: '''

    if check_input(text, [1, 2]) == 1:
        sleep(2)
        return rescue_team_vile_vault(player)
    else:
        sleep(2)
        return steal_statue(player)


def rescue_team_vile_vault(player):
    sleep(3)
    clear_screen()
    print(f'''
    {player.name} runs out of the V.I.L.E. tower and jumps using her glider
    to follow the moving van. \n ''')
    
    sleep(3)
    print_slow(f'''{player.name}: I'm seeing the van. \n ''')

    sleep(3)
    print(f'''
    {player.name} manages to jump and get into the van, but she finds out that
    it's being driven by remote control.''')
    
    sleep(2)
    print_slow(f''' {player.name}: Player, there's no one here. \n ''')

    sleep(3)
    print('''
    The remote s control screen lights up and shows the leaders of V.I.L.E. 
    ''')

    sleep(2)
    print_slow(f''' 
    Coach Brunt: Well, well. I didn't tell you she would be too stubborn
    to accept our offer?

    Maelstrom: Yeah, looks like I owe you a dinner Coach Brunt. \n ''')

    sleep(2)
    print('''Zack and Ivy are shown on the screen. Their memory is erased.
    Game Over. \n ''')

    sleep(5)
    clear_screen()
    print_slow(f'''
    ------------
    Carambas, isso não é bom! A situação agora é irreversível. 
    Entretanto, como último recurso, você utilizará sua persuasão para 
    convencer a Treinadora Brunt a não apagar a memória dos seus amigos.

    Persuasão: +{player.persuasion}
    ------------
    ....''')

    sleep(5)

    if check_sucess(player.persuasion) == True:
        print_slow(f'''
    {player.name}: Ok, Coach Brunt. You got me this time. 
    However, I'm your best chance for the heist.
    I accept your offer.
    No tricks this time.

    Coach Brunt breathes deeply.

    Treinadora Brunt: Ok, you got yourself a second chance.
    Do not waste it.
        ''')
        sleep(5)
        return steal_statue(player)
    else:
        print_slow(f'''
    {player.name}: Ok, Coach Brunt. You got me this time. 
    However, I'm your best chance for the heist.
    I accept your offer.
    No tricks this time.

    Coach Brunt: I won't fall for that again!
        ''')
        sleep(5)
        return endings.bad_ending_1()  # Used to be Bad Ending 01


def steal_statue(player):
    clear_screen()
    #Storytelling
    print_slow(f'''
    {player.name}: Ok. What´s the game? 

    Coach Brunt: First round! Have you ever heard of
    Chinese “terracotta” warriors? I want you to steal a statue for me.

    Player: What are we going to do?

    {player.name}: The only thing we can: play the V.I.L.E's game until 
    we figure out how to find Zack and Ivy.

    Player: So now, I think you will go to Xi’ian in China.
    Emperor Qin was a bit eccentric, so he demanded to be buried
    with thousands of these life-size clay warriors.

    You must go to a new excavation site where was recently
    discovered more warriors.
    ''')
    
    sleep(3)
    print(f'{player.name} go to the excavation site.')

    sleep(4)
    clear_screen()
    print_slow(f'''
    {player.name}: My archenemy Tigress has decided to show up.

    Player: Why V.I.L.E. would you send one of your agents?

    {player.name}: to help me or pester me.

    {player.name}: I can sneak by Tigress or I can talk to her and see if
    she says where they might be keeping Zack and Ivy.
    ''')

    text = f'''  
    Sneak up or have some chit chat?
    I need to decide before she sees me.

    [1] Sneak
    [2] Chit chat
    
    Your choice: '''

    if check_input(text, [1, 2]) == 1:
        sleep(2)
        return sneak_tigress(player)
    else:
        sleep(2)
        return chit_chat_tigress(player)


def sneak_tigress(player):
    sleep(5)
    clear_screen()
    print(f'''
    {player.name} sneak past Tigress and skip the
    wall of the excavation site, but finds several guard dogs. ''')

    sleep(4)
    print(f'''
    ------------
    Fight with the dogs but do not tire yourself out. To escape without 
    facing Tigress, a lot of energy and luck will be necessary.

    Energy: +{player.energy}
    ------------
    .....
    ''')

    sleep(2)
    if check_sucess(player.energy) == True:
        print(f'''
    You miraculously escape the dogs. 
    Tigress didn't see you and you can follow
    the tunnel to the excavation site of the warriors.
        ''')
        sleep(2)
        return text_security_officer(player)

    print_slow(f'{player.name}:When it\'s  not a cat, it\'s a dog... \n')

    sleep(3)
    print(f'''
    {player.name} flees and falls outside the excavation site,
    facing Tigress. \n''')

    sleep(2)
    print_slow(f'''
    Tigress: Oh, those puppies scared the brave {player.name}? 
    ''')
    return chit_chat_tigress(player)


def chit_chat_tigress(player):
    sleep(3)
    print_slow(f'''
    {player.name}: What are you doing here?

    Tigress: The leaders thought you might need supervision to not
    unintentionally spoil your own theft.

    {player.name}: Or, they figured out I might need support since they
    they kidnapped my team and therefore I am supervising you.
    
    Tigress: Enjoy it while you can.

    Player: {player.name}, I found a tunnel in the excavation area.
    Should lead straight to the warriors.
    ''')
    sleep(4)
    return tunnel_soldier(player)


def tunnel_soldier(player):
    clear_screen()
    print_slow(f'''
    {player.name}: Since you are here. Is there any chance you would know 
    where my friends are being kept? I would like to send a postcard.

    Tigress: It looks like I was going to tell.
    ''')

    sleep(3)
    print(f'''
    Tiger unintentionally activates a trap and both she and {player.name}
    fall into a hole. {player.name} is faster and escapes. 
    Tigress gets trapped.
    ''')

    sleep(4)
    print_slow(f'''
    {player.name}: Wow! I thought cats always landed on their feet.

    Tigress: Help me get out of here. Now!

    {player.name}: Only this time I could help Tigress.
    Or, I can leave her.
    ''')

    sleep(3)
    text = f''' 
    {player.name}: Anyway, the cat here is in charge now.

    [1] Help Tigress
    [2] Leave her

    Your choice: '''
    
    if check_input(text, [1, 2]) == 1:
        sleep(2)
        return help_tigress(player)
    else:
        sleep(2)
        return leave_tigress(player)


def help_tigress(player):
    player.persuasion_op(+1)
    
    sleep(3)
    print(f'''
    {player.name} throws the rope of her zipline so Tigress can get out.
    ''')
    
    sleep(2)
    print_slow(f'{player.name}: I ll help you just this once.')

    sleep(3)
    print('Reminder: Tigress will remember that you helped her to escape.')

    sleep(3)
    print_slow(f'''
    Tigress: Wait a minute, what?

    {player.name}: I know cats like lines!
    ''')
    
    sleep(5)
    clear_screen()
    print_slow(f'''
    ------------
    Congratulations! Your choice increased your Persuasion points.

    Persuasion: +{player.persuasion} (+1)
    ------------
    ....
    ''')
    sleep(1)

    player.help_tigress = 1
    return text_security_officer(player) 


def leave_tigress(player):
    sleep(3)
    print_slow(f'''
    {player.name}: I heard that cats are excellent diggers.
    ''')
    sleep(3)
    print('Reminder: Tiger will remember that you didn t help her escape.')
    
    sleep(3)
    print_slow(f'''
    Tigress: Come back here! There are bugs in this hole!

    {player.name}: I'm not listening you! I'm in a tunnel. The signal is bad…
    ''')

    sleep(2)
    player.help_tigress = 0
    return text_security_officer(player)

def text_security_officer(player):
    sleep(4)
    clear_screen()
    #Storytelling
    print(f'''
    {player.name} arrives at the terracotta warriors' excavation hall and
    makes a video call to Coach Brunt. ''')
    print_slow(f'''
    Coach Brunt: I hope it's to talk about something good.

    {player.name}: I'm in!

    Coach Brunt: Great! I've been waiting for hours on this treadmill!
    Show me everything so I can choose a good one!
    ''')

    sleep(3)
    print(f'{player.name} show the warriors for the villain to choose.')
    
    sleep(3)
    print_slow(f'''
    Coach Brunt: There! That one!
    No, the one with the beard!
    No, the one with the mustache!

    {player.name}: I agreed to steal for you, Brunt. Not to get a boyfriend.

    Coach Brunt: I have an extraction team circulating in the area.
    I will give the signal for action.
    ''')

    sleep(3)
    return security_officer(player)

def security_officer(player):
    sleep(5)
    clear_screen()

    print(f'''
    The extraction team starts hoisting the statue into a helicopter 
    when {player.name} is seen by a security guard.
    ''')
    
    sleep(5)
    print_slow(f'''
    Security: Hey! Who's there?

    {player.name}: Player, they caught me!

    Player: We have to get you out of there!
    ''')

    text = f'''
    {player.name}: Can I jump and get a ride with the statue or 
    camouflage myself and hide with the warriors.

    Jump or camouflage?

    [1] Hitching a ride with the statue
    [2] Hide with other warriors

    Your choice: '''

    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return jump_statue(player)
    else:
        sleep(1)
        return hide_statue(player)


def jump_statue(player):
    sleep(5)
    clear_screen()
    print(f'''
    {player.name} hitchhike with the statue, but the guards manage to jump and
    they hang on your legs. 

    ------------
    It seems like you'll need some luck to get out of this without breaking
    the statue.

    Luck: +{player.lucky}
    ------------
    ....
    ''')
    
    if check_sucess(player.lucky) == True:
        sleep(2)
        print(f'''
    By a leap of luck, you freed yourself from the guards 
    along with the statue.
    ''')
        sleep(3)
        return hide_statue(player)

    sleep(2)
    print(f'''
    The statue falls on the roof along with
    the guards and it breaks. {player.name} manages to escape in her glider. 
    ''')

    sleep(3)
    print(f'''
    {player.name} receives a video call.
    ''')
    
    sleep(5)
    print_slow(f'''
    Coach Brunt: I see my order didn't come to me in one piece.

    {player.name}: I'll get another one!

    Coach Brunt: Unfortunately not, little daughter. So let's decide the
    codenames for our new agents? I like Tweedle Dee and Tweedle Dee Do!
    ''')

    sleep(5)
    clear_screen()
    print_slow(f'''
    ------------
    Opa! Hora de utilizar seus dotes para convencer a Treinadora a não 
    limpar a mente dos seus amigos!

    Wow. Time to use your powers to convince Coach Brunt to not wipe out 
    your friends' minds.

    Persuasion: +{player.persuasion}
    ------------
    ''')

    if check_sucess(player.persuasion) == True:
        print_slow(f'''
    {player.name}: Don't touch them! I want a second chance!

    Treinadora Brunt conversa com Dr. Bellum, aborrecida com
    o ocorrido.

    Coach Brunt talks with Dr. Bellum about the failed mission.

    Dr. Bellum: Okay, just one more chance. It seems like these are lucky days
    for you, {player.name}. Coach Brunt is feeling good today. 
    Make a video call when the dust is out.
    ''')
        sleep(4)
        return choose_act_two(player)

    else:
        print_slow(f''')
    {player.name}: Don't touch them! I want a second chance!

    Coach Brunt: Hey, Doc! Time to load your…
    What's this thing really called?

    Dr. Bellum: It's been renamed: THE MIND MELT!
    ''')

        sleep(4)
        return endings.bad_ending_2(player)


def hide_statue(player):
    sleep(5)
    clear_screen()
    print(f'''
    The statue is carried by the extraction team.
     {player.name} is cloaked among warriors
     and the security guards don't find her. 
    ''')
    #Storytelling
    print_slow(f'''
    Security: The thief has escaped! Let's go!''')

    sleep(1)
    return choose_act_two(player)


def choose_act_two(player):
    sleep(5)
    clear_screen()
    #Storytelling
    print(f'''
    After the mission in Shanghai, {player.name} makes a video call
    with the leaders of the V.I.L.E.
    ''')
    
    sleep(5)
    print_slow('''
    Countess Cleo: So Dr Bellum and I came to an agreement on your 
    next mission. The choice is yours. 

    Dr Bellum: Maybe you'll like my mission since it involves exploring
    the distant past of the earth.

    Countess Cleo: Boring. With my heist you will go to an
    extravagant party where you can come across the rich and famous.
    ''')

    sleep(1)
    text = '''
    Which mission do you want to follow?

    [1] Mission 1 - Countess Cleo
    [2] Mission 2 - Dr. Bellum

    Your choice: '''

    if check_input(text, [1, 2]) == 1:
        from modules.acts_en import act_2_m1
        sleep(3)
        return act_2_m1.start(player)
    else:
        from modules.acts_en import act_2_m2
        sleep(3)
        return act_2_m2.start(player)