from modules.acts_pt import endings


def check_input(text, options):
    choice = int(input(text))

    while choice not in options:
        print('Não entendi. Tente novamente.\n')
        choice = int(input(text))

    return choice


def start():
    return party()


def party():
    text = '''
    Você deseja dançar ou prefere prosseguir?

    [1] Dançar
    [2] Recusar a dança

    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        return dance()
    else:
        return refuse_dance()


def dance():
    return steel_caviare()


def refuse_dance():
    return steel_caviare()


def steel_caviare():
    text = '''
    Você irá esconder o caviar ou roubar e correr?
    
    [1] Disfarçar e Esconder
    [2] Roubar e Correr
    
    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        return hide()
    else:
        return run()


def hide():
    return endings.bad_ending_5()


def run():
    return vile_safebox()


def vile_safebox():
    text = '''
    Você irá resgatar seus amigos agora ou roubar mais uma vez?

    [1] Resgatar Equipe
    [2] Ir para próxima missão

    '''
    if check_input(text, [1, 2]) == 1:
        return rescue_team()
    else:
        return steel_again()


def rescue_team():
    return endings.good_ending_1()


def steel_again():
    return endings.bad_ending_4()
