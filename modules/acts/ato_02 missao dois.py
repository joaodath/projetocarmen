def act_two_mission_two():
    return roubar_osso()

def roubar_osso():
    choice = input('Você irá se esconder da ACME ou fugir com o osso?')   
    if choice == 'Esconder':
        return esconder_da_acme()
    else:
        return fugir_com_osso()

def fugir_com_osso():
    return cofre_da_vile()

def esconder_da_acme():
    return bad_ending()

def cofre_da_vile():
    choice = input('Resgatar equipe ou roubar mais uma vez?')
    if choice == 'Resgatar':
        return resgatar_equipe()
    else:
        return roubar_mais_uma_vez()

#if se tiver dinheiro para comprar a passagem e energia suficiente. Se não, fim de jogo

def resgatar_equipe():
    print('Você conseguiu resgatar sua equipe! Parabéns!!!')
    return happy_ending()


def roubar_mais_uma_vez():
    print('É uma emboscada.V.I.L.E conseguiu te capturar')
    return bad_ending()



