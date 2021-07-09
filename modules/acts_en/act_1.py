from modules.acts_pt import endings
from modules.extras import print_slow, check_input, clear_screen
from time import sleep

#Starts the game from act 01
def start(player):
    clear_screen()
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
    
    {player.name}: Go in by the last floor certainly will demand risky maneuvers
    but by the first floor, I´ll face oposition.     
    ''')
    sleep(0.5)
    text = f'''
    To find out what V.I.L.E. is hiding, I need to enter this tower.

    What´s your choice? 

    [1] Last floor
    [2] First floor
    
    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        return top_building(player)
    else:
        return bottom_building(player)


def top_building(player):
    sleep(0.5)
    clear_screen()
    #Storytelling
    print(f'''
    {player.name} reaches the top of nearby building and prepares herself to fly using a zipline to reach the
    V.I.L.E's building.
    ''')
    
    sleep(0.5)
    print_slow(f'''
    {player.name}: I go gliding!''')
    
    sleep(0.5)
    print(f'''
    {player.name} uses a laser to cut the glass on the window dressing
    of the building and enter. She falls into the janitor's closet.''')
    
    sleep(0.5)
    print_slow(f'''
    {player.name}: The janitor's closet???

    Player: You asked for the "cleanest" route! 

    {player.name}: Just shows me the path to the safe.
    ''')
    
    sleep(0.5)
    print(f'''
    Player sends the route to {player.name}.''')
    
    sleep(0.5)
    return text_vile_vault(player)


def bottom_building(player):
    clear_screen()
    
    #Storytelling
    sleep(0.5)
    print(f'''
    {player.name} is going up to the vault floor
    using the elevator shaft.
    ''')

    sleep(0.5)
    print_slow(f'''
    Player: You really know how to get in in style, Red!!

    {player.name}: Better than smiling for the elevator cameras.
    I will be careful with the gap.
    ''')

    sleep(0.5)
    print(f'''
    {player.name} forces the elevator´s door to open and come face to face with the guards.
    She fights with them and wins. 
    ''')
    
    sleep(1)
    print_slow(f''' {player.name}: Player, guide me. \n''')
    print(f'''Player sents the route to {player.name}.''')
    
    sleep(0.5)
    return text_vile_vault(player)


def text_vile_vault(player):
    clear_screen()
    #Storytelling
    print_slow(f'''
    {player.name}: Safe located. Too easy …''')

    sleep(0.5)
    print(f''' 
    The safe is empty, except for a little tablet in a pedestal 
    in the center of the safe´s room. {player.name} goes in and can hear the V.I.L.E.´s leaders speaking
    ''')

    sleep(2)
    print_slow(f'''
    Maelstrom: Welcome, {player.name}! Please, make your self at home. 

    {player.name} touches in the tablet and a big screen apppears in the safe with all V.I.L.E's leaders. 

    {player.name}: Well well. All my former crime school instructors!

    Maelstrom: You are without a doubt the best thief who has ever been through the
    runners of the V.I.L.E... Academy

   Countess Cleo: Although we never picked the fruits of we've taught every stealing skill you know.

    Dr. Bellum: So today we can finally play
    of "{player.name}: V.I.L.E's agent."

    {player.name}: Can we skip to the part where I say no?
    Because I'm not sure what part of this last year has kept them from
    understand that I will NEVER steal for V.I.L.E...

    Coach Brunt: Oh, not even to save your fearless helpers?
    ''')
    
    sleep(1)
    print('''The screen shows Ivy and Zack,
    tied up somewhere hard to understand where it is.''')
    sleep(0.5)
    return vile_vault(player)

def vile_vault(player):
    sleep(1)
    clear_screen()
    print_slow(f'''
   Dr. Bellum: Refuse to play our game and I swear we'll erase their memory and
    we will reprogram your team to become V.I.L.E. agents!

    Maelstrom: So, will you steal for us or will it be them?

    Player: {player.name}: I found Zack and Ivy's van on a street camera.
    It's on the move. Do you think you can reach it? 
    ''')

    sleep(1)
    clear_screen()
    text = f'''  
    {player.name}:  I can try to save Zack and Ivy right now, but it would be dangerous.
    Or, I can accept stealing for V.I.L.E. until I figured out a way to get my team back.

    What do I do?
    I need to get them back safely somehow.

    [1] Rescue team
    [2] Stealing a Terracotta Warrior
    
    Your choice: '''

    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return rescue_team_vile_vault(player)
    else:
        sleep(1)
        return steal_statue(player)


def rescue_team_vile_vault(player):
    clear_screen()
    print(f'''
    {player.name} runs out of the V.I.L.E. and jump using a glider
    to follow the moving van. \n ''')
    
    sleep(0.5)
    print_slow(f'''{player.name}: I'm seeing the van. \n ''')
    print(f'''{player.name} manages to jump and get into the van, but she finds out that
    it's being driven by remote control.''')
    
    sleep(0.5)
    print_slow(f''' {player.name}: Player, there's no one here. \n ''')
    print('The remote s control screen lights up and shows the leaders of V.I.L.E. ')

    sleep(0.5)
    print_slow(f''' 
    Coach Brunt: Well, well. I didn't tell you she would be too stubborn
    to accept our proposal?

    Maelstrom: Yeah, looks like I owe you a dinner Coach Brunt. \n ''')
    print('''Zack and Ivy are shown on the screen. Their memory is erased.
    Game Over. \n ''')

    sleep(1)
    print_slow(f'''Narrator: Uh, that's not good. {player.name} deserves another
    chance to rescue her team. And luckily you can have this second chance. 
    Maybe she can steal for V.I.L.E. until you can outwit them.
    ''')
    sleep(1)
    print('''
    You will return to the last choice and you will be able to
    try a different path''')
    sleep(2)
    return vile_vault(player) #Used to be Bad Ending 01


def steal_statue(player):
    clear_screen()
    #Storytelling
    print_slow(f'''
    {player.name}: Ok. What´s the game? 

    Coach Brunt: First round! Have you ever heard of
    Chinese “terracotta” warriors? I want you to steal a statue for me.

    Player: What are we going to do?

    {player.name}: The only thing we can: make the V.I.L.E's game.
    until we figure out how to find Zack and Ivy.

    Player: So now, I think it will go to Xi’ian in China.
    Emperor Qin was a bit eccentric. he demanded to be buried
    with thousands of these life-size clay warriors.

    You must go to a new excavation site where was recently
    discovered more warriors.
    ''')
    
    sleep(1)
    print(f'{player.name} go to the excavation site.')

    sleep(2)
    clear_screen()
    print_slow(f'''
    {player.name}: My arch enemy Tigress has decided to show up.

    Player: Why V.I.L.E. would you send one of your agents?

    {player.name}: to help me or harm.
    ''')

    text = f'''  
    {player.name}: I can sneak by Tigress or I can talk to Tigress and see if
    she says where they might be keeping Zack and Ivy.

    Sneak up or have a chat?
    I need to decide before she sees me.

    [1] Sneak
    [2] To chat
    
    Your choice: '''

    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return sneak_tigress(player)
    else:
        sleep(1)
        return chit_chat_tigress(player)


def sneak_tigress(player):
    sleep(0.5)
    clear_screen()
    print(f'''
    {player.name} sneak past Tigress and skip the
    wall of the excavation site, but finds several guard dogs. ''')
    print_slow(f'{player.name}:When it s  not a cat, it s a dog... \n')
    sleep(0.5)
    print(f'''
    {player.name} flees and falls outside the excavation site,
    facing Tigress. \n''')
    print_slow(f'''
    Tigress: Oh, those puppies scared the brave {player.name}? 
    ''')
    return chit_chat_tigress(player)


def chit_chat_tigress(player):
    sleep(0.5)
    print_slow(f'''
    {player.name}: What are you doing here?

    Tigress: The leaders thought you might need supervision to not
    unintentionally spoil your own theft.

    {player.name}: Or, they figured out I might need support since they
    they kidnapped my team and therefore I am supervising you.
    
    Tigress: Enjoy it while you can.

    Player: Red, I found a tunnel in the excavation area.
    Should lead straight to the warriors.
    ''')

    return tunnel_soldier(player)


def tunnel_soldier(player):
    sleep(0.5)
    clear_screen()
    print_slow(f'''
    {player.name}: Since you are here. Is there any chance you would know where my
    friends are being kept? I would like to send a postcard.

    Tigress: It looks like I was going to tell.
    ''')

    sleep(0.5)
    print(f'''
    Tiger unintentionally activates a trap and both she and {player.name}
    fall into a hole. {player.name} is faster and escapes. Tigress gets trapped.
    ''')
    print_slow(f'''
    {player.name}: Wow! I thought cats always landed on their feet.

    Tigress: Help me out of here. Now!
    ''')
    text = f''' 
    {player.name}: Only this time I could help Tigress.
    Or, I can leave her.
    Anyway, the cat here is in charge now.

    [1] Help Tigress
    [2] Leave her

    Your choice: '''
    
    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return help_tigress(player)
    else:
        sleep(1)
        return leave_tigress(player)


def help_tigress(player):
    player.help_tigress = 1
    sleep(0.5)
    print(f'''
    {player.name} throws the rope of her zipline so Tigress can get out.
    ''')
    print_slow(f'{player.name}: I ll help you just this once.')
    print('Reminder: Tigress will remember that you helped her to escape.')
    print_slow(f'''
    Tigress: Wait a minute, what?

    {player.name}: I know cats like lines!
    ''')
    return 


def leave_tigress(player):
    sleep(0.5)
    print_slow(f'''
    {player.name}: I heard that cats are excellent diggers.
    ''')
    print('Reminder: Tiger will remember that you didn t help her escape.')
    print_slow(f'''
 Tigress: Come back here! There are bugs in this hole!

    {player.name}: I'm not listening you! I'm in a tunnel. The signal is bad…
    ''')
    return text_security_officer(player)

def text_security_officer(player):
    sleep(0.5)
    clear_screen()
    #Storytelling
    print(f'''
    {player.name} arrives at the terracotta warriors' excavation hall and
    makes a video call to Coach Brunt. ''')
    print_slow(f'''
   Coach Brunt: I hope it's to talk about a good subject.

    {player.name}: I'm in!

    Coach Brunt: Great! I've been waiting for hours on this treadmill!
    Show me everything so I can choose a good one!
    ''')
    sleep(0.5)
    print(f'{player.name} show the warriors for the villain to choose.')
    
    sleep(0.5)
    print_slow(f'''
    Coach Brunt: There! That one!
     No, the one with the beard!
     No, the one with the mustache!

     {player.name}: I agreed to steal for you, Brunt. Not to get a boyfriend.

     Coach Brunt: I have an extraction team circulating in the area.
     I will give the signal for action.
    ''')
    return security_officer(player)

def security_officer(player):
    sleep(0.5)
    clear_screen()
    print(f'''
   The extraction team starts hoisting the statue into a helicopter when {player.name}
     is seen by a security guard.
    ''')
    
    sleep(0.5)
    print_slow(f'''
    Security: Hey! Who's there?

     {player.name}: Player, they caught me!

     Player: We have to get you out of there!
    ''')

    text = f'''
    {player.name}: Can I jump and get a ride with the statue or camouflage myself
     and hide with the warriors.

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
    sleep(0.5)
    clear_screen()
    print(f'''
    {player.name} hitchhike with the statue, but the guards manage to jump and
     if they hang on {player.name}'s legs. The statue falls on the roof along with
     the guards and it breaks. {player.name} manages to escape in his glider.
    ''')
    sleep(0.5)
    print(f'''
    {player.name} receives a video call.
    ''')
    
    sleep(0.5)
    print_slow(f'''
   Coach Brunt: I see my fiancé by order didn't get it
     come to me in one piece.

     {player.name}: I got another one!

     Coach Brunt: Unfortunately not, little girl. So let's decide the
     codenames for our new agents? I like Tico and Teco!

     {player.name}: Don't touch them! I want a second chance!

     Coach Brunt: Hey, Doc! Time to load your…
     What's this thing really called?

     Dr. Bellum: It's been renamed: THE MELTS MINDS!

     sleep(0.5)
     print(f'Zack and Ivy have their minds wiped. {player.name} lost.''')

    sleep(0.5)
    print_slow(f'''
    Narrator: I see two things I'd rather not see.
     A fall in flight and a team with its memory erased.
     Want a better ending? I'll send you back in the field
     so you can fix this.
    ''')
    
    sleep(0.5)
    print('''
   You will return to the last choice and you will be able to
     try a different path''')
    sleep(2)
    return security_officer(player) #Used to be Bad Ending 2


def hide_statue(player):
    sleep(0.5)
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
    sleep(1)
    clear_screen()
    #Storytelling
    print(f'''
    After the mission in Shanghai, {player.name} makes a video call
     with the leaders of the V.I.L.E.
    ''')
    
    sleep(0.5)
    print_slow('''
    Countess Cleo: So Dr Bellum and I came to an agreement on your next mission. The choice is yours. 

     Dr Bellum: Maybe you like my mission as it involves exploring
     the distant past of the earth.

     Countess Cleo: Boring. With my theft you will go to a
     extravagant party where you can come across the rich and famous.
    ''')

    sleep(1)
    text = '''
   Which mission do you want to follow?

     [1] Mission 1 - Countess Cleo
     [2] Mission 2 - Dr. Bellum
    
     Your choice: '''

    if check_input(text, [1, 2]) == 1:
        from modules.acts_pt import act_2_m1
        sleep(1)
        return act_2_m1.start(player)
    else:
        from modules.acts_pt import act_2_m2
        sleep(1)
        return act_2_m2.start(player)