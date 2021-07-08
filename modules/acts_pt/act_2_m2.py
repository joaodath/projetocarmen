from modules.acts_pt import endings
from modules.extras import print_slow, check_input, clear_screen
from time import sleep

#Starts Act 02 from Mission 02
def start_m2(player):
    clear_screen()
    return in_the_lab(player)


def in_the_lab(player):
    clear_screen()
    #Storytelling
    print_slow('''Storytelling aqui''')
    text = '''
    Você irá se esconder da ACME ou fugir com o osso?

    [1] Esconder
    [2] Fugir

    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        return hide(player)
    else:
        return run(player)


def hide(player):
    clear_screen()
    return endings.bad_ending_3(player)


def run(player):
    clear_screen()
    return vile_safebox(player)


def vile_safebox(player):
    clear_screen()
    #Storytelling
    print_slow('''Storytelling aqui''')
    text = '''
    Você irá resgatar seus amigos agora ou roubar mais uma vez?

    [1] Resgatar Equipe
    [2] Ir para próxima missão

    '''
    if check_input(text, [1, 2]) == 1:
        return rescue_team(player)
    else:
        return steel_again(player)


def rescue_team(player):
    clear_screen()
    return endings.good_ending_1(player)


def steel_again(player):
    clear_screen()
    return endings.bad_ending_4(player)
