from modules.acts_pt import endings


def check_input(text, options):
    choice = int(input(text))

    while choice not in options:
        print('Não entendi. Tente novamente.\n')
        choice = int(input(text))

    return choice


def start():
    print('''
    Você está no prédio...
    ''')
    return building()


def building():
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
    print('''
    Invandindo pelo último andar.\n
    ''')
    return vile_vault()


def bottom_building():
    print('''
    Invandindo pelo térreo.\n
    ''')
    return vile_vault()


def vile_vault():
    text = '''
    Você está no cofre da VILE.

    Resgatar equipe ou roubar um guerreiro terracota?
    
    [1] Resgatar equipe
    [2] Roubar um Guerreiro
    
    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        return rescue_team_vile_vault()
    else:
        return steal_statue()


def rescue_team_vile_vault():
    return endings.bad_ending_1()


def steal_statue():
    print('''
    Você encontrou a estátua e chamou a equipe para estração.
    ''')
    return security_officer()


def security_officer():
    text = '''
    Um segurança te viu!

    Pular com estátua ou se camuflar? 
    
    [1] Pular com estátua
    [2] Se Camuflar
    
    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        return jump_statue()
    else:
        return hide_statue()


def jump_statue():
    return endings.bad_ending_2()


def hide_statue():
    print('''
    Você se camuflou e conseguiu fugir!\n
    ''')
    return choose_act_two()


def choose_act_two():
    print('''
    Agora você pode escolher entre a missão da Dra. Bellum ou a missão da Condessa Cleo.
    
    Na missão da Dra. Bellum, você irá explorar o passado do planeta.
    Na missão da Condessa Cleo, você irá para uma festa onde poderá cruzar com ricos e famosos!

    ''')

    text = '''
    Qual missão deseja seguir?

    [1] Missão 1 - Dra Bellum.
    [2] Missão 2 - Condessa Cleo.
    
    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        from modules.acts_pt import act_2_m1
        return act_2_m1.start()
    else:
        from modules.acts_pt import act_2_m2
        return act_2_m2.start()
