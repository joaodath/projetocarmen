from modules.acts_pt import endings
from modules.extras import print_slow, check_input, clear_screen
from time import sleep


def start(player):
    clear_screen()
    sleep(1)
    return party(player)


def party(player):
    clear_screen()
    # Storytelling
    print_slow(f'''
    Após a missão em Xangai, {player.name} recebe uma ligação da V.I.L.E 
    
    {player.name}: Está bem condessa Cleo. O que seu coração sombrio deseja? 
    Condessa Cleo: Para minha missão, quero que roube o último lote de um caviar Beluga.
    Será servido numa festa de caridade em Mônaco.
    
    Player: Localizado na Riviera Francesa, Mônaco é o segundo menor país do mundo. 
    A festa será num luxuoso hotel em Monte Carlo.

    Após uma longa viagem, {player.name} se encontra em Mônaco, no local propício para efetuar
    o assalto. 

    {player.name}: Vou me misturar, localizar as latas, e depois roubá-las.

    O Anfitrião da Festa se aproxima e faz a seguinte pergunta:

    Anfitrião da Festa: Me daria a honra dessa dança? 
    
    {player.name}: Estou em missão, então deveria me concentrar e recusar. 
    Mas aceitar a dança pode ser o melhor jeito de me misturar e chegar à cozinha.
    ''')
    text = '''
    
    Você deseja dançar ou prefere prosseguir?

    [1] Dançar
    [2] Recusar a dança

    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return dance(player)
    else:
        sleep(1)
        return refuse_dance(player)


def dance(player):
    print_slow(f'''
    {player.name} participa de uma bela dança com o Anfitrião da Festa.
    Isso lhe ajuda a se misturar no local.
    ''')
    clear_screen()
    sleep(1)
    return steel_caviare(player)


def refuse_dance(player):
    print_slow(f'''
    {player.name} : Obrigado, mas valsa não é minha praia. Se quiser dançar
    tango...

    O Anfitrião se despede cordialmente e vai embora.
    ''')
    clear_screen()
    sleep(1)
    return steel_caviare(player)


def steel_caviare(player):
    clear_screen()
    # Storytelling
    print_slow(f'''
    Após o ocorrido, {player.name} observa dois garçons se dirigindo
    à cozinha, observando o caviar logo em seguida.
    
    {player.name}: Avistei as ovas. 
    
    Player: Como você vai pegar? 
    
    {player.name}: Posso me disfarçar de garçom, pegar o caviar e sair furtivamente,
    ou simplesmente pegar o caviar e sair correndo.     
    ''')
    text = '''
    Você irá se disfarçar para capturar o caviar ou roubar e correr?
    
    [1] Disfarçar e Capturar
    [2] Roubar e Correr
    
    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return hide(player)
    else:
        sleep(1)
        return run(player)


def hide(player):
    clear_screen()
    print_slow(f'''
    {player.name} se disfarça como garçom para capturar os caviares. Entretanto um imprevisto acontece!
    Como houve um tempo decorrido para o disfarce, os caviares já foram removidos de suas latas,
    sendo servidos em pratos!
    
    {player.name} captura os caviares dos pratos e os põe em uma vasilha e foge furtivamente. Após
    sair da festa, entra em contato com a Condessa Cleo.
    
    Carmen: O caviar está servido.

    Condessa Cleo: Que grosseria! Fora das latas, deixou a iguaria exposta!

    Carmen: Você queria ovas de peixe, eu entreguei.
    
    Condessa Cleo: Foi o que fez. Mas agora só vão durar um dia! E não posso consumir cem latas de
    caviar em um dia. Dra Bellum, ative o... seja lá qual for o nome disso hoje!

    Carmen: Não!
    ''')
    sleep(1)
    return endings.bad_ending_5(player)


def run(player):
    clear_screen()
    print_slow(f'''
    {player.name} invade a cozinha e sai com o caviar.

    Anfitrião: Peguem-na!

    {player.name} é encurralada pelos garçons e seguranças mas consegue escapar após
    pega o caviar, abrir a porta lateral e saltar vôo com um equipamento.

    Após pousar em segurança, {player.name} liga para a Condessa Cleo.

    {player.name}: Peguei os bebês Belugas.

    Condessa Cleo esboça um sorriso de satisfação.

    Condessa Cleo: Ótimo! Por favor, aguarde novas instruções.
    ''')
    sleep(1)
    return vile_safebox(player)


def vile_safebox(player):
    clear_screen()
    # Storytelling
    print_slow(f'''    
    Player: Ao analisar as imagens do esconderijo onde estão Ivy e Zac, descobri a 
    possibilidade de estarem localizados no Círculo Ártigo. Após fazer uma grande pesquisa
    encontrei um esconderijo da V.I.L.E situado nessa região. Será que Ivy e Zac estão lá?
    
    O que deseja fazer {player.name}? 
    
    {player.name}: Começo uma arriscada missão de resgate agora, ou roubo pela última vez encerrando o
    acordo?
    ''')
    text = '''
    Você irá resgatar seus amigos agora ou ir para a última missão?

    [1] Resgatar Equipe
    [2] Ir para última missão

    '''
    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return rescue_team(player)
    else:
        sleep(1)
        return steel_again(player)


def rescue_team(player):
    clear_screen()
    sleep(1)
    return endings.good_ending_1(player)


def steel_again(player):
    clear_screen()
    sleep(1)
    return endings.bad_ending_4(player)
