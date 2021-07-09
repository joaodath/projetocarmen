from modules.extras import print_slow, clear_screen
from modules.acts_pt import endings
from time import sleep

# Starts Act 3 Ending A


def start_3a(player):
    print(f'''
    {player.name} está num avião em direção ao esconderijo da V.I.L.E. no
    Círculo Ártico. Ela começa uma chamada de vídeo com os vilões.''')
    sleep(2)
    clear_screen()
    print('Chamada de Vídeo com a V.I.L.E.')
    sleep(1)
    print_slow(f'''
    {player.name}: Estou a caminho da última missão.

    Treinadora Brunt: Ótimo, docinho. E lembre-se: sem gracinhas. 
    Ou verá cabecinhas tendo as memórias apagadas. 

    {player.name}: Eu nem pensaria nisso…
    ''')
    print('Fim da chamada de vídeo com a V.I.L.E.')
    sleep(2)
    clear_screen()
    print(f'{player.name} está num jet ski de neve.')
    print_slow(f'''
    Player: Se aproximando da base onde Zack e Ivy estão presos. 

    {player.name}: Vamos levá-los para casa!

    {player.name} invade o esconderijo. 

    {player.name}: Player, entrei.
    ''')
    print(f'''
    {player.name} dá de cara com uma porta de vidro trancada que ela 
    não consegue abrir. Tigresa aparece do outro lado.
    ''')
    print_slow('''
    Tigresa: Ainda quer saber onde os seus amigos estão presos?
    ''')

    if player.help_tigress == True:
        return end_helped_tigress(player)
    else:
        return end_not_helped_tigress(player)


def end_helped_tigress(player):
    sleep(1)
    print(f'Tigresa abre a porta para {player.name}.')
    print_slow(f'''
    {player.name}: Ahn… Obrigada?

    Tigresa: Você me ajudou a sair daquele buraco. 
    Considere como uma retribuição. Mas só dessa vez. 
    Quando eu te encontrar de novo, prepare-se!
    ''')

    sleep(1)
    print(f'''
    {player.name} alcança sua equipe antes que tenham as mentes apagadas. 
    ''')
    print_slow(f'''
    Ivy: Uhull! A turma tá reunida novamente!

    Zack: Então agora partiu sorvete?

    {player.name}: No Ártico?

    Zack: Por que não?
    ''')

    sleep(2)
    endings.good_ending_2()
    sleep(10)
    print('Auto-destruição em 3')
    sleep(1)
    print('Auto-destruição em 2')
    sleep(1)
    print('Auto-destruição em 1')
    sleep(1)
    print('Auto-destruição iniciada')
    sleep(1)
    clear_screen()


def end_not_helped_tigress(player):
    sleep(1)
    print_slow(f'''
    Tigresa: Oh, você quer entrar, não é? 
    E eu queria ajuda para sair daquele buraco. 
    Parece que nenhuma de nós está conseguindo o que quer. 
    ''')

    sleep(1)
    print(f'''
    Tigresa aciona a trava de segurança e uma grande porta de ferro 
    se fecha no corredor deixando {player.name} do lado de fora.''')
    sleep(2)
    print(f'''
    {player.name} entra na tubulação de ar e segue para onde sua 
    equipe está presa. Ela acha que consegue resgatar os amigos antes que 
    suas mentes sejam reprogramadas, mas logo ela descobre que estava errada. 
    Zack e Ivy já tinham sido reprogramados e capturam {player.name} 
    para a V.I.L.E. 
    ''')

    sleep(2)
    clear_screen()
    endings.bad_ending_4()
    sleep(10)
    print('Auto-destruição em 3')
    sleep(1)
    print('Auto-destruição em 2')
    sleep(1)
    print('Auto-destruição em 1')
    sleep(1)
    print('Auto-destruição iniciada')
    sleep(1)
    clear_screen()
