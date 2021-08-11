from modules.acts_en import endings
from modules.extras import print_slow, clear_screen
from time import sleep

def start_3b(player):
    import pygame
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    pygame.mixer.music.load('modules/audio/audio5.ogg')
    pygame.mixer.music.play(-1)
    print(f'''
    {player.name} is at the airport and receives a videocall from V.I.L.E.
    ''')

    sleep(2)
    clear_screen()
    sleep(1)
    print('Start of videocall with V.I.L.E.')
    print_slow(f'''
    Maelstrom: Você irá receber uma passagem de balsa para ilha de Oléron

    {player.name}: Onde estão Zack e Ivy?

    Treinadora Brunt: Nós os passamos da cela para o local de entrega, 
    então não se preocupe e pegue aquela balsa. 
    Quando recebermos os tesouros, terá sua equipe de volta. 
    ''')
    print('Fim da chamada com a V.I.L.E.')

    sleep(2)
    clear_screen()
    print_slow(f'''
    Player: Isso é uma cilada, né?

    {player.name}: Parece que sim. Maelstrom ainda não me pediu o 
    presentinho dele. Tudo que me fizeram roubar foi só uma cortina de fumaça 
    para o real objetivo. Nunca quiseram caviar, ossos, ou artefatos milenares 
    chineses. Querem vingança. 

    Player: Eles querem apagar sua mente e te reprogramar para 
    roubar para eles. 

    {player.name}: Isso. Querem jogar “{player.name}: Agente da V.I.L.E” 
    para sempre.

    Player: Você não pode continuar com isso. 

    {player.name}: Também não posso abandonar nossos amigos. 
    ''')
    print(f'{player.name} percebe que Júlia está seguindo seus passos.')
    print_slow(f'''
    {player.name}: Parece que alguém farejou o meu rastro. 
    Acho que posso usar isso para vantagem própria.
    ''')
    print(f'Júlia perde o rastro de {player.name}.') 
    print_slow(f'Júlia: Como ela sempre consegue fazer isso?')
    print(f'{player.name} se encontra com Julia e pede sua ajuda.')
    print_slow(f'''
    {player.name}: Júlia, estou precisando da sua ajuda. ''')

    if player.trust_julia == True:
        return ending_trusted_julia(player)
    else: 
        return ending_not_trusted_julia(player)
    

def ending_trusted_julia(player):
    print_slow(f'Júlia: É.. é… cla-ro!')
    print(f'''
    {player.name} vai ao local de encontro com a V.I.L.E. de balsa para 
    tentar resgatar a equipe.
    ''')
    print(f'''
    Os agentes da V.I.L.E. tentam capturar {player.name} na balsa mas 
    descobrem que na verdade é Júlia quem está na balsa fingindo ser 
    {player.name}. Era só uma distração.
    ''')
    
    sleep(1)
    print(f'''
    {player.name} encontra os amigos num armazém abandonado. 
    Eles conseguem fugir com um helicóptero.
    ''')

    sleep(1)
    print(f'{player.name} devolve os itens que roubou para Julia.')

    sleep(2)
    endings.good_ending_3()

    sleep(10)
    print('Auto-destruição em 3')
    sleep(1)
    print('Auto-destruição em 2')
    sleep(1)
    print('Auto-destruição em 1')
    sleep(1)
    print('Auto-destruição iniciada')
    sleep(1)
    clear_screen()


def ending_not_trusted_julia(player):
    print_slow(f'''
    Júlia: E por que eu te ajudaria de novo?

    {player.name}: Júlia, por favor, confia em mim! 
    Tenho uma boa razão para tudo que faço.

    Júlia: Eu confiei em você antes e o que eu ganhei com isso? 
    Fiquei trancada no terraço. 

    {player.name}: Lamento que se sinta assim, Júlia.
    ''')
    print('Júlia entra num táxi e vai embora.')
    print_slow(f'''
    Player: O que vamos fazer? Não pode simplesmente ir para uma armadilha.

    {player.name}: Não temos escolha. Vamos pegar Zack e Ivy agora mesmo!
    ''')

    sleep(2)
    clear_screen()
    print(f'''
    {player.name} vai ao local de encontro com a V.I.L.E. de balsa para 
    tentar resgatar a equipe.
    ''')

    sleep(1)
    print(f'''
    Os agentes da V.I.L.E. capturam {player.name} na saída da balsa usando 
    dardos tranquilizantes.
    ''')
    sleep(4)
    endings.bad_ending_6()
    sleep(10)
    print('Auto-destruição em 3')
    sleep(1)
    print('Auto-destruição em 2')
    sleep(1)
    print('Auto-destruição em 1')
    sleep(1)
    print('Auto-destruição iniciada')
    sleep(1)
    clear_screen()
