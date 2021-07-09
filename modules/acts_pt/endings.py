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
            a melhor escolha no momento. As mentes de Zack e Ivy é apagada e você perde a missão.
    ''')


def bad_ending_2():
    clear_screen()
    print_slow('''
                                        GAME OVER: VOCÊ PERDEU
            Falhar na missão optando por uma atitude mais valente custou bem caro,.Apesar da intenção
            ser boa, não foi a melhor escolha no momento. A mente de Zack e Ivy é apagada e você o jogo.
    ''')


def bad_ending_3():
    clear_screen()
    print_slow('''
                                        GAME OVER: VOCÊ PERDEU
            Optar por não roubar o osso no momento propício custou caro. A ACME levou o osso para um
            cofre seguro, impossibilitando a realização do assalto. A mente de Zack e Ivy é apagada
            e você perde o jogo.
    ''')


def bad_ending_4():
    clear_screen()
    print_slow('''
                                            GAME OVER: VOCÊ PERDEU
            Não ajudar a Tigresa no inicio do jogo custou caro para você. A mente de Zack e Ivy é apagada
            e você perde o jogo.
    ''')


def bad_ending_5():
    clear_screen()
    print_slow('''
                                            GAME OVER: VOCÊ PERDEU
            Puxa! Como o caviar foi aberto, a validade dele passou a ser de somente um dia. A Condessa Cleo
            se recusou a consumir, fazendo seus amgigos pagarem o pato pelo seu vacilo. A mente de Zack e Ivy
            é apagada e você perde o jogo.
    ''')


def bad_ending_6():
    clear_screen()
    print_slow('''
                                            GAME OVER: VOCÊ PERDEU
            Parabéns por cumprir suas missões com excelência.  A doutora, a condessa e a treinadora já estão 
            curtindo seus presentes. O que significa que está na hora do meu presente. Agora você vai roubar
            para  a V.I.L.E. como foi treinada. Para todo sempre!
    
                        Você e sua equipe têm as mentes apagadas. Fim de jogo. Você perdeu.
    ''')


def good_ending_1():
    clear_screen()
    print_slow('''
                                            GAME OVER: VOCÊ GANHOU
            Você optou por salvar seus amigos no melhor momento, e isso lhe garantiu uma vitória para casa.
            Zac e Ivy são salvos pacificamente por meio de sua aventura no Círculo Ártico. Parabéns!!
    ''')


def good_ending_2():
    clear_screen()
    print_slow('''
                                            GAME OVER: VOCÊ GANHOU
            Só sobremesas para todo mundo! Parabéns, agente!  Você derrotou a V.I.L.E. dessa vez. Mas
            mantenha-se vigilante. Nunca se sabe quando podem atacar novamente.
    ''')


def good_ending_3():
    clear_screen()
    print_slow('''
                                            GAME OVER: VOCÊ GANHOU
                Um passeio de helicóptero para todo mundo! Parabéns, agente! Você derrotou a V.I.L.E. dessa
                vez. Mas mantenha-se vigilante. Nunca se sabe quando podem atacar novamente.
    ''')
