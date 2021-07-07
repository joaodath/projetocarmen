from modules.acts_pt import endings
from modules.classes.character import print_slow, check_input
from time import sleep

#Starts Act 02 from Mission 02
def start():
    return in_the_lab()


def in_the_lab():
    #Storytelling
    print_slow('''Storytelling aqui''')
    text = '''
    Você irá se esconder da ACME ou fugir com o osso?

    [1] Esconder
    [2] Fugir

    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        return hide()
    else:
        return run()


def hide():
    return endings.bad_ending_3()


def run():
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
        return rescue_team()
    else:
        return steel_again()


def rescue_team():
    return endings.good_ending_1()


def steel_again():
    return endings.bad_ending_4()
