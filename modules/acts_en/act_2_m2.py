from modules.acts_en import endings
from modules.extras import print_slow, check_input, clear_screen
from time import sleep

#Starts Act 02 from Mission 02
def start_m2(player):
    clear_screen()
    import pygame
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    pygame.mixer.music.load('modules/audio/audio3.ogg')
    pygame.mixer.music.play(-1)
    return in_the_lab(player)


def in_the_lab(player):
    clear_screen()
    #Storytelling
    print_slow(f'''
    {player.nome} What do you want Dr Bellum? Release codes?
    Biological Weapons? A cat video replay machine?

    Dr Bellum - I want you to bring me a bone, and that's why
    I'll send you to Hell Creek, Montana, USA, to get a dinosaur bone. 
    Tyrannosaurus Rex, to be more specific,one that was discovered with
    intact soft tissue.

    {player.name} – You don't want to clone...
    
    Dr Bellum – If anyone is going to try this feat of nature, it will be me!

    {player.name}: Player, I'm going to Hell Creek.
    ''')
    sleep(1)
    clear_screen() 
    print_slow('''
    Player - Montana means mountain in Spanish. A billion years ago,
    many dinosaurs roamed Hell Creek.
    ''')

    sleep(1)
    print(f'''
    {player.name} arrives at Hell Creek and is watching the
    archaeological site by far.
    ''')
    print_slow(f'''
    {player.name} - Hip bone, thigh bone.
    Where is this T-Rex anyway?

    {player.name} - with a binoculars she detects where the bone is,
    takes a picture and sends it to player.

    Player – And we have the dinosaur bone!

    {player.name} - It was taken to the plane. Can you discover the destination?

    Player - There is a research laboratory 300km away. What's your plan?
    
    {player.name}: Looks like we're going to pay a visit to the lab.
    ''')

    sleep(1)
    clear_screen()
    print(f'Dra Bellum calls {player.name}.')
    print_slow(f'''
    Dr Bellum: Tic Tac Miss {player.name}. You are in Montana all afternoon
    and still hasn't gotten the dinosaur bone.
    How can you beat us so many times if you are so inefficient?

    {player.name}: I don't usually work alone.

    Dr Bellum: I didn't think you depended so much on your helpers.

    {player.name}: They are not my helpers. They are my friends.

    Dr Bellum: I thought you were joking. Very well.
    I will send El Topo to help. 
    ''')
    
    sleep(2)
    clear_screen()
    print(f'{player.name} arrives at the lab')
    print_slow(f'''
    {player.name}: What lab is this?

    Player: Museum and dinosaur´s park.
    Conveniently closed at night.

    {player.name}: The bone is in there. El Topo is late.
    ''')
    
    sleep(1)
    print('El Topo appears coming out of a sewer tunnel.')
    print_slow(f'''
    El Topo: Sorry for the delay. I was researching possible escape routes.
    
    {player.name}: Let's get this over with. El Topo, you cover me.
    Player, guide me.
    ''')
    
    sleep(1)
    print(f'''
    {player.name} is entering in the lab.
    El Topo warns that ACME is already in the place.
    ''')

    text = '''
    Will you hide from ACME or run away with the bone?

    [1] To hide
    [2] To flee

    Your choice: '''

    if check_input(text, [1, 2]) == 1:
        return hide(player)
    else:
        sleep(1)
        return run(player)


def hide(player):
    clear_screen()
    return endings.bad_ending_3(player)


def run(player):
    sleep(1)
    clear_screen()
    print(f'''')
    {player.name} runs to get the bone.
    ''')

    sleep(1)
    print(f'''
    She finds the bone and manages to escape with the help of El Topo.
    {player.name} calls Dr Bellum.
    ''')
    
    sleep(1)
    print_slow(f'''
    {player.name}:The bone is with me.
    Dr Bellum: Fantastic. I will contact you for more information.
    ''')
    return vile_safebox(player)


def vile_safebox(player):
    clear_screen()
    #Storytelling
    sleep(1)


    print_slow(f'''
    {player.name}: Player, any clue on where Zack and Ivy are?

    Player: {player.name}, I found a sign!
    Searching for V.I.L.E hideouts in the Arctic Circle.
    I found one. What do you want to do?

    {player.name}: I can try to rescue my team now or I can steal
    for the V.I.L.E. one last time. A new mission can be risky,
    but it can also be a chance to keep up appearances until I recover 
    the team. 
    ''')
       
    sleep(1)
    text = '''
    Will you rescue your friends now or steal one more time?

    [1] Rescue Team
    [2] Steal once more for V.I.L.E.
    '''
    if check_input(text, [1, 2]) == 1:
        return rescue_team(player)
    else:
        return steel_again(player)


def rescue_team(player):
    clear_screen()
    from modules.acts_en import act_3a
    return act_3a.start_3a(player)


def steel_again(player):
    clear_screen()
    if player.missions_count == 2:
        from modules.acts_en import act_3b
        return act_3b.start_3b(player)
    else:
        from modules.acts_pt import act_2_m1 