from modules.acts_pt.bad_endings import bad_ending_4, bad_ending_5,
from modules.acts_pt.happy_endings import happy_ending_1,
def act_two_mission_one():
    return festa()
    
def festa():
    choice = input('Você irá dançar ou recusar a dança?')   
    if choice == 'Dançar': 
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
    return bad_ending_5()

def roubar_e_correr():
    choice = input('Você irá resgatar seus amigos agora ou ir para a próxima missão? ')
    if choice == 'Resgatar':
        return resgatar_equipe()
    else:
        return bad_ending_4()

def resgatar_equipe():
    return happy_ending_1()
    #fim de jogo


# def proxima_missao():
#     return 2



