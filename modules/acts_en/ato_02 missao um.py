def act_two_mission_one():
    return festa()
    
def dancar():
    choice = input('Você irá dançar ou recusar a dança?')   
    if choice == 'Dançar': #merge próximo ramo? ver mapa
        return dancar()
    else:
        return recusar_danca()

def dancar():
    print('Carmen está dançando')
    return roubar_caviar()

def recusar_danca():
    print('Carmen não quis dançar')
    return roubar_caviar()

def roubar_caviar():
    choice = input('Você irá esconder o caviar ou roubar e correr? ')
    if choice == 'Esconder':
        return esconder_caviar()
    else:
        return roubar_e_correr()

def esconder_caviar():
    return bad_ending5()

def roubar_e_correr():
    choice = input('Você irá resgatar seus amigos agora ou ir para a próxima missão? ')
    if choice == 'Resgatar':
        return resgatar_equipe()
    else:
        return proxima_missao()

def resgatar_equipe():
    print('Você conseguiu resgatar sua equipe! Parabéns!!!')
    #fim de jogo


def proxima_missao():
    return 2
