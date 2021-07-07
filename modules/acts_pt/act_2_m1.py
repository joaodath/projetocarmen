from modules.acts_pt import endings
from modules.classes.character import print_slow, check_input
from time import sleep

def start():
    sleep(1)
    return party()


def party():
    #Storytelling
    print_slow('''Storytelling aqui''')
    text = '''
    Você deseja dançar ou prefere prosseguir?

    [1] Dançar
    [2] Recusar a dança

    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return dance()
    else:
        sleep(1)
        return refuse_dance()


def dance():
    sleep(1)
    return steel_caviare()


def refuse_dance():
    sleep(1)
    return steel_caviare()


def steel_caviare():
    #Storytelling
    print_slow('''Storytelling aqui''')
    text = '''
    Você irá esconder o caviar ou roubar e correr?
    
    [1] Disfarçar e Esconder
    [2] Roubar e Correr
    
    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return hide()
    else:
        sleep(1)
        return run()


def hide():
    sleep(1)
    return endings.bad_ending_5()


def run():
    sleep(1)
    return vile_safebox()


def vile_safebox():
    #Storytelling
    print_slow('''Storytelling aqui''')
    text = '''
    Você irá resgatar seus amigos agora ou roubar mais uma vez?

    [1] Resgatar Equipe
    [2] Ir para próxima missão

    '''
    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return rescue_team()
    else:
        sleep(1)
        return steel_again()


def rescue_team():
    sleep(1)
    return endings.good_ending_1()


def steel_again():
    sleep(1)
    return endings.bad_ending_4()
