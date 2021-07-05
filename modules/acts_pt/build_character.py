from modules.classes import character
def create_character():
    player = character.Character()
    change_name = input('''
    Sua personagem é Carmen Sandiego.
    Você quer alterar o nome da sua personagem? S/N ''').strip().upper()
    while change_name not in ['S', 'N']:
        change_name = input('''
        Eu não entendi. Vamos tentar novamente!
        Sua personagem é Carmen Sandiego.
        Você quer alterar o nome da sua personagem? S/N ''').strip().upper()
    if change_name == 'S':
        player.naming = (input('Por favor, digite o nome da sua personagem: ').strip().title())
        print('Okay! Vamos começar este jogo!')
    else:
        print('Okay! Vamos começar este jogo!')
    return player