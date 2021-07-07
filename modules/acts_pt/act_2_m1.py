from modules.acts_pt import endings
from modules.classes.character import print_slow, check_input
from time import sleep

def start():
    sleep(1)
    return party()


def party():
    #Storytelling
    print_slow('''
    Após a missão em Xangai, Carmen recebe uma ligação da V.I.L.E 
    
    Carmen: Está bem condessa Cleo. O que seu coração sombrio deseja? 
    Condessa Cleo: Para minha missão, quero que roube o último lote de um caviar Beluga.
    Será servido numa festa de caridade em Mônaco.
    
    Player: Localizado na Riviera Francesa, Mônaco é o segundo menor país do mundo. 
    A festa será num luxuoso hotel em Monte Carlo.

    Carmen: Vou me misturar, localizar as latas, e depois roubá-las.

    Anfitrião da Festa: Me daria a honra dessa dança, Srta Santa Rosa? 
    
    Carmen: Estou em missão, então deveria me concentrar e recusar. 
    Mas aceitar a dança pode ser o melhor jeito de me misturar e chegar à cozinha.
    ''')
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
    print_slow('''
    Carmen observa dois garçons indo para a cozinha
    
    Carmen: Avistei as ovas. 
    
    Player: Como você vai pegar? 
    
    Carmen: Posso esconder e sair furtivamente, ou pegar e sair correndo.     
    ''')
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
    print_slow('''
    Carmen sai da cozinha com o caviar
    
    Anfitrião: Peguem-na! 
    
    Carmen pega o caviar e salta vôo com um equipamento.

    Carmen liga para Condessa Cleo
    
    Carmen: Peguei o caviar. 
    Condessa Cleo: Aguarde novas instruções. 
    
    Player: Buscando esconderijos da V.I.L.E no Círculo Ártico, encontrei Ivy e Zac. 
    O que quer fazer? 
    
    Carmen: Começo uma arriscada missão de resgate, ou roubo pela última vez?
''')
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
