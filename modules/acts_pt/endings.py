from modules.extras import print_slow, check_input, clear_screen
from time import sleep

# Bad Endings 01 and 02 are now deprecated. Maintaing only during building.
# The entire Endings package must be deprecated.
# Scheduled to be removed on first release


def bad_ending_1():
    clear_screen()
    print_slow('''
                                        GAME OVER: VOCÊ PERDEU
            Você tentou resgatar seus amigos imediatamente. Apesar da intenção ser boa, não foi
            a melhor escolha no momento. A mente de Zack e Ivy é apagada e você perde a missão.
    ''')


def bad_ending_2():
    clear_screen()
    print_slow('''
                                        GAME OVER: VOCÊ PERDEU
            Falhar na missão optando por uma atitude mais valente custou bem caro,.Apesar da intenção
            ser boa, não foi a melhor escolha no momento. A mente de Zack e Ivy é apagada e você o jogo.
    ''')


def bad_ending_3():
    print_slow('''
    Final Ruim 03: Missão da Dra. Bellum: A ACME leva o osso para um cofre seguro. Fim de Jogo.
    ''')


def bad_ending_4():
    print_slow('''
    Final Ruim 04: Roubar mais uma vez pra VILE é uma emboscada. A V.I.L.E captura Carmen. Fim de Jogo.
    ''')


def bad_ending_5():
    print_slow('''
    Final Ruim 05: O caviar é aberto. A validade depois de aberto é de 1 dia. A Condessa Cleo se recusa a consumir todo o caviar em um dia. Fim do jogo.
    ''')


def good_ending_1():
    print_slow('''
    Final bom 01: Ela tenta resgatar a equipe imediatamente e consegue. O jogo termina com Carmen vencedora!
    ''')
