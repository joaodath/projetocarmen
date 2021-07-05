from modules.classes import character
def create_character():
    player = character.Character()
    change_name = input('''
    Your character is Carmen Sandiego.
    Do you wanna change the name of your character? Y/N ''').strip().upper()
    while change_name not in ['Y', 'N']:
        change_name = input('''
        I didn't get that. Let's try again!
        Your character is Carmen Sandiego.
        Do you wanna change the name of your character? Y/N ''').strip().upper()
    if change_name == 'Y':
        player.name(input('Please, inform the name of your character: ').strip().title())
        print('Okay! Let\'s start this game!')
    else:
        print('Okay! Let\'s start this game!')
    return player