#Esqueleto do Arquivo Main
#O main deve rodar imports com base na necessidade do usuário durante o jogo

# #import idioma
# from modules.acts.ato_01 import act_one


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
    from modules.acts_en import act_02
    from modules.classes import character
    from modules.acts_en import build_character

else:
    from modules.acts_pt import bad_endings
    from modules.acts_pt import act_01
    # from modules.acts_pt import act_02
    from modules.classes import character
    from modules.acts_pt import build_character

#Defines the character of the game
player = build_character.create_character()


#Game starts with Act One
calling = act_01.act_one()
if calling == 'act_two':
    act_02.act_two() #Calls Act Two
else:
    print('Oops, there was a problem!')