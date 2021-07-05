from modules.acts_pt import endings


def check_input(text, options):
    choice = int(input(text))

    while choice not in options:
        print('Não entendi. Tente novamente.\n')
        choice = int(input(text))

    return choice


def start():
    return in_the_lab()


def in_the_lab():
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
