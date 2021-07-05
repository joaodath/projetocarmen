from modules.acts_pt.bad_endings import bad_ending_1, bad_ending_2

def act_one():
    return building()


def building():
    choice = input('''Invadir pelo último andar ou térreo?
    [1] Último Andar
    [2] Térreo''')
    if choice == 'Último Andar':
        return top_building()
    else:
        return bottom_building()


def top_building():
    return vile_vault()


def bottom_building():
    return vile_vault()


def vile_vault():
    choice = input('''Resgatar equipe ou roubar um guerreiro?
    [1] Regatar equipe
    [2] Roubar um Guerreiro''')
    if choice == 'Resgatar equipe':
        return rescue_team_vile_vault()
    else:
        return steal_statue()


def rescue_team_vile_vault():
    print('É uma emboscada.')
    return bad_ending_1()


def steal_statue():
    return security_officer()


def security_officer():
    choice = input('''Pular com estátua ou se camuflar? 
    [1] Pular com estátua
    [2] Se Camuflar''')
    if choice == 'Pular junto com a estátua':
        return jump_statue()
    else:
        return hide_statue()


def jump_statue():
    print('Você caiu.')
    return bad_ending_2()


def hide_statue():
    return 'act_two'

def choice_of_mission():
    print('''
    Agora você pode escolher entre a missão da Dra. Bellum ou a missão da Condessa Cleo.
    Na missão da Dra. Bellum, você irá explorar o passado do planeta.
    Na missão da Condessa Cleo, você irá para uma festa onde poderá cruzar com ricos e famosos!''')
    choice = int(input('''
    Faça sua escolha:
    [1] Missão 1 - Dra Bellum.
    [2] Missão 2 - Condessa Cleo.
    
    Digite sua escolha: '''))
    return choice
