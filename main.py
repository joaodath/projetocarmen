# Esqueleto do Arquivo Main
# O main deve rodar imports com base na necessidade do usuário durante o jogo.

from modules.classes.character import Character 
from modules.extras import print_slow, check_input, clear_screen
from time import sleep

if __name__ == '__main__':
    clear_screen()
    print_slow('''
    
    Welcome to "Carmen Sandiego: to steal or not to steal"!
    We're starting the game soon!
    First, we need to know your language preference.
    
    Bem vinde a "Carmen Sandiego: roubar ou não roubar, eis a questão".
    Vamos começar o jogo já, já!
    Primeiro, precisamos saber seu idioma de preferência. 
    ''')
    text = '''
    Inform the language you want:
    Informe o idioma que deseja para prosseguir:

    [1] English / Inglês
    [2] Português / Portuguese

    Type your choice.
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
