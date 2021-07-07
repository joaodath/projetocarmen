from modules.acts_pt import endings
from modules.classes.character import print_slow, check_input
from time import sleep

#Starts the game from act 01
def start(player):
    #Storytelling
    print_slow(f'''
    {player.name}
    Você está no prédio...
    ''')
    sleep(1)
    return building()


def building():
    #Storytelling
    print_slow('''Storytelling aqui''')
    text = '''
    Invadir pelo último andar ou térreo?
    
    [1] Último Andar
    [2] Térreo
    
    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        return top_building()
    else:
        return bottom_building()


def top_building():
    #Storytelling
    print_slow('''
    Invandindo pelo último andar.\n
    ''')
    sleep(1)
    return vile_vault()


def bottom_building():
    #Storytelling
    print_slow('''
    Invandindo pelo térreo.\n
    ''')
    sleep(1)
    return vile_vault()


def vile_vault():
    #Storytelling
    print_slow('''
    Você está no cofre da VILE.

    Resgatar equipe ou roubar um guerreiro terracota? \n''')
    text = '''  
    [1] Resgatar equipe
    [2] Roubar um Guerreiro
    
    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return rescue_team_vile_vault()
    else:
        sleep(1)
        return steal_statue()


def rescue_team_vile_vault():
    sleep(1)
    return endings.bad_ending_1()


def steal_statue():
    #Storytelling
    print_slow('''
    Você encontrou a estátua e chamou a equipe para estração.
    ''')
    sleep(1)
    return security_officer()


def security_officer():
    #Storytelling
    print_slow('''Storytelling aqui''')
    text = '''
    Um segurança te viu!

    Pular com estátua ou se camuflar? 
    
    [1] Pular com estátua
    [2] Se Camuflar
    
    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return jump_statue()
    else:
        sleep(1)
        return hide_statue()


def jump_statue():
    sleep(1)
    return endings.bad_ending_2()


def hide_statue():
    #Storytelling
    print_slow('''
    Você se camuflou e conseguiu fugir!\n
    ''')
    sleep(1)
    return choose_act_two()


def choose_act_two():
    #Storytelling
    print_slow('''
    Agora você pode escolher entre a missão da Dra. Bellum ou a missão da Condessa Cleo.
    
    Na missão da Dra. Bellum, você irá explorar o passado do planeta.
    Na missão da Condessa Cleo, você irá para uma festa onde poderá cruzar com ricos e famosos!

    ''')
    sleep(1)
    text = '''
    Qual missão deseja seguir?

    [1] Missão 1 - Dra Bellum.
    [2] Missão 2 - Condessa Cleo.
    
    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        from modules.acts_pt import act_2_m1
        sleep(1)
        return act_2_m1.start()
    else:
        from modules.acts_pt import act_2_m2
        sleep(1)
        return act_2_m2.start()
