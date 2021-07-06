# Esqueleto do Arquivo Main
# O main deve rodar imports com base na necessidade do usuário durante o jogo.

from modules.classes.character import Character


def check_input(text, options):
    # Função que realiza a pergunta (parametro text) e só retorna
    # Caso a resposta enviada for válida (estiver em options)
    choice = int(input(text))

    while choice not in options:
        print('Não entendi. Tente novamente.\n')
        choice = int(input(text))

    return choice


if __name__ == '__main__':
    text = '''
    Informe o idioma que deseja para prosseguir:

    [1] Inglês
    [2] Português

    Sua Escolha: '''

    if check_input(text, [1, 2]) == 1:
        from modules.acts_en import act_1

        print('''
    Hi! Welcome to "Carmen Sandiego: to steal or not to steal".
    Let\'s start our game!''')
        player = Character(language=1)
        act_1.start()
        
    else:
        from modules.acts_pt import act_1

        print('''
    Oi! Bem vinde a "Carmen Sandiego: roubar ou não roubar, eis a questão".
    Vamos iniciar nosso jogo!''')
        player = Character(language=2)
        player.create_character()
        act_1.start()
