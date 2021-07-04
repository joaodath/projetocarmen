#Esqueleto do Arquivo Main
#O main deve rodar imports com base na necessidade do usuário durante o jogo

#import idioma
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
    from modules.acts import act1_en
else:
    from modules.acts import act1_pt

