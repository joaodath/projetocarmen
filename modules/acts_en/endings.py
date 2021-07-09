def bad_ending_1(player):
    print('''
    GAME OVER: VOCÊ PERDEU
    Ela tenta resgatar a equipe imediatamente mas a van está vazia. 
    O jogo termina. 
    ''')


def bad_ending_2(player):
    print('''
    GAME OVER: VOCÊ PERDEU
    Pular e pegar carona com a estátua faz ela cair. Fim do jogo.
    ''')


def bad_ending_3(player):
    print('''
    GAME OVER: VOCÊ PERDEU
    Missão da Dra. Bellum: 
    A ACME leva o osso para um cofre seguro. Fim de Jogo.
    ''')


def bad_ending_4(player):
    print(f'''
    GAME OVER: VOCÊ PERDEU
    Roubar mais uma vez pra VILE é uma emboscada. 
    A V.I.L.E captura {player.name}. Fim de Jogo.
    ''')


def bad_ending_5(player):
    print('''
    GAME OVER: VOCÊ PERDEU
    O caviar é aberto. A validade depois de aberto é de 1 dia. 
    A Condessa Cleo se recusa a consumir todo o caviar em um dia. Fim do jogo.
    ''')

def bad_ending_5(player):
    print('''
    GAME OVER: VOCÊ PERDEU
    Essa escolha não foi muito boa.
    ''')

def good_ending_1(player):
    print(f'''
    GAME OVER: VOCÊ GANHOU
    Final bom 01: Ela tenta resgatar a equipe imediatamente e 
    consegue. O jogo termina com {player.name} vencedora!
    ''')
