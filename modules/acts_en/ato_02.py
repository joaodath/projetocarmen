def act_two():
    return missao_dois() 


def roubar_osso():
    choice = input('Você irá se esconder da ACME ou fugir com o osso?')   
    if choice == 'Se esconder':
        print('A ACME levou o osso para um cofre seguro.')
    return 1

def fugir_com_osso():
    return cofre_da_vile()

def cofre_da_vile():
    choice = input('Resgatar equipe ou roubar mais uma vez?')
    if choice == 'Resgatar equipe':
        return resgatar_equipe()
    else:
        return roubar_mais_uma_vez()

#if se tiver dinheiro para comprar a passagem e energia suficiente. Se não, fim de jogo

def resgatar_equipe():
    print('Você conseguiu resgatar sua equipe! Parabéns!!!')
    #fim de jogo


def roubar_mais_uma_vez():
    print('É uma emboscada.V.I.L.E conseguiu te capturar')
    return 1



