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
                                            GAME OVER: VOCÊ PERDEU
            Puxa! Como o caviar foi aberto, a validade dele passou a ser de somente um dia. A Condessa Cleo
            se recusou a consumir, fazendo seus amgigos pagarem o pato pelo seu vacilo. A mente de Zack e Ivy
            é apagada e você perde o jogo.
    ''')


def good_ending_1():
    clear_screen()
    print_slow('''
                                            GAME OVER: VOCÊ GANHOU
            Você optou por salvar seus amigos no melhor momento, e isso lhe garantiu uma vitória para casa.
            Zac e Ivy são salvos pacificamente por meio de sua aventura no Círculo Artigo. Parabéns!!
    ''')
