#Esqueleto do Arquivo Main
#O main deve rodar imports com base na necessidade do usuário durante o jogo.

if __name__ == '__main__':
    print('''
    Hi! Welcome to "Carmen Sandiego: to steal or not to steal.
    Please, select your language below:

    Oi! Bem vinde a "Carmen Sandiego: roubar ou não roubar, eis a questão.
    Por favor, selecione o seu idioma abaixo:

    [1] English
    [2] Português''')
    language = int(input('''
    Please, type your choice.
    Por favor, digite sua escolha: '''))
    while language not in [1, 2]:
        language = int(input('''
        I didn't understand. Please, type your choice.
        Eu não entendi. Por favor, digite sua escolha: '''))
    if language == 1:
        from modules.acts_en import bad_endings
        from modules.acts_en import act_01
        from modules.classes import character
        from modules.acts_en import build_character

    else:
        from modules.acts_pt import bad_endings
        from modules.acts_pt import act_01
        from modules.classes import character
        from modules.acts_pt import build_character

    #Defines the character of the game
    player = build_character.create_character()


    #Game starts with Act One
    calling = act_01.act_one()
    if calling == 'act_two':
        choose_mission = act_01.choice_of_mission() #Chooses next mission
        if choose_mission == 1 and language == 1:
            from modules.acts_en import act_02_mission_01
            act_02_mission_02.act_two_mission_two()
        elif choose_mission == 2 and language == 1:
            from modules.acts_en import act_02_mission_02
            act_02_mission_01.act_two_mission_one()
        elif choose_mission == 1 and language == 2:
            from modules.acts_pt import act_02_mission_01
            act_02_mission_02.act_two_mission_two()
        elif choose_mission == 2 and language == 2:
            from modules.acts_pt import act_02_mission_02
            act_02_mission_01.act_two_mission_one()
        else:
            print('Oops, there was a problem!')