# Esqueleto do Arquivo Main
# O main deve rodar imports com base na necessidade do usuário durante o jogo.

from classes.character import Character 
from classes.extras import print_slow, check_input, clear_screen
from time import sleep

if __name__ == '__main__':
    clear_screen()
    text = '''
    Informe o idioma que deseja para prosseguir:

    [1] Inglês
    [2] Português

    Sua Escolha: '''

    if check_input(text, [1, 2]) == 1:
        from modules.acts_en import act_1
        clear_screen()
        print_slow('''
        Hi! Welcome to "Carmen Sandiego: to steal or not to steal".
        Let\'s start our game! \n ''')
        sleep(1)
        player = Character(language=1)
        act_1.start(player)
        
    else:
        from modules.acts_pt import act_1
        clear_screen()
        print_slow('''
        Oi! Bem vinde a "Carmen Sandiego: roubar ou não roubar, eis a questão".
        Vamos iniciar nosso jogo! \n ''')
        sleep(1)
        player = Character(language=2)
        player.create_character()
        act_1.start(player)
