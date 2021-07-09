from modules.acts_pt import endings
from modules.extras import check_sucess, print_slow, check_input, clear_screen
from time import sleep

# Starts Mission 1 from Act 2


def start_m1(player):
    clear_screen()
    sleep(1)
    return party(player)


def party(player):
    clear_screen()
    # Storytelling
    print(f'''
    Após a missão em Xangai, {player.name} recebe uma ligação da V.I.L.E''')
    print_slow(f'''
    {player.name}: Está bem condessa Cleo. O que seu coração sombrio deseja? 
    Condessa Cleo: Para minha missão, quero que roube o último lote de um 
    caviar Beluga. Será servido numa festa de caridade em Mônaco. ''')
    sleep(1)
    clear_screen()
    print_slow(f'''
    Player: Localizado na Riviera Francesa, Mônaco é o segundo 
    menor país do mundo. A festa será num luxuoso hotel em Monte Carlo.

    {player.name}: Vou me misturar, localizar as latas, e depois roubá-las. 
    ''')
    print(f'''
    {player.name} chega à festa. 
    O anfitrião a vê e se dirige a seu encontro''')

    sleep(1)
    print_slow(f'''
    Anfitrião da Festa: Me daria a honra dessa dança, Srta...?

    {player.name}: Santa Rosa! Srta. Santa Rosa.

    Anfitrião da Festa: Me daria a honra dessa dança, Srta. Santa Rosa?
    ''')
    text = f'''
    {player.name}: Estou em missão, então deveria me concentrar e recusar. 
    Mas aceitar a dança pode ser o melhor jeito de me misturar e 
    chegar à cozinha.

    Devo dançar ou prosseguir com o plano?

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
    player.persuasion_op(+1)
    player.energy_op(-1)

    print_slow(f'''
    {player.name} participa de uma bela dança com o Anfitrião da Festa.
    Isso lhe ajuda a se misturar no local.

    Persuação: +{player.persuasion} [+1]
    Energia: +{player.energy} [-1]
    ''')

    clear_screen()
    sleep(2.5)
    return steel_caviare(player)


def refuse_dance(player):
    player.persuasion_op(-1)

    print_slow(f'''
    {player.name} : Obrigado, mas valsa não é minha praia. Se quiser dançar
    tango...

    O Anfitrião se despede cordialmente e vai embora.
    
    Persuação: +{player.persuasion} [-1]
    ''')

    clear_screen()
    sleep(2.5)
    return steel_caviare(player)


def steel_caviare(player):
    clear_screen()
    print(f'''
    {player.name} observa dois garçons indo para a cozinha.
    ''')

    print_slow(f'''
    {player.name}: Avistei as ovas. 
    
    Player: Como você vai pegar? 
    ''')

    text = f'''
    {player.name}: Posso esconder e sair furtivamente, 
    ou pegar e sair correndo.
    
    Disfarço e escondo o caviar ou roubo e saio correndo?
    
    [1] Disfarçar e Capturar
    [2] Roubar e Correr
    
    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:

        print_slow(f'''
    Ótima escolha! Entretanto, você precisará de sorte para o disfarce ser de
    acordo com o planejado.

    Sorte: +{player.lucky}

    ....
        ''')

        if check_sucess(player.lucky) == True:
            sleep(1)
            return hide(player)
        else:
            print(f'''
    Infelizmente o disfarce não deu muito certo... Um garçom reconheceu você!
            ''')
            sleep(1)
            return run(player)
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
    print(f'''
    {player.name} se veste de garçonete.
    Ela observa o mímico da V.I.L.E comendo algo.
    ''')

    sleep(1)
    print_slow(f'''
    {player.name}: Está fora do personagem. Devia comer petiscos invisíveis.
    ''')

    sleep(0.5)
    print('O homem começa a passar mal.')

    sleep(0.5)
    print_slow(f'''
    {player.name}: Acho que o mímico não está bem.

    Player: Não estou surpreso. Mímicos não tem graça. 

    {player.name}: Não é truque. Ele engasgou mesmo!

    Player: O que você vai fazer? Se for ajudar, pode perder o caviar.

    {player.name}: Dessa vez, só tem uma escolha. 
    ''')

    sleep(0.5)
    print(f'''
    {player.name} o ajuda.
    Ao chegar na cozinha, a iguaria já foi servida.
    ''')

    sleep(0.5)
    print_slow('''
    Anfitrião: E agora, como prato principal, apresento o caviar Beluga.
    Bon apetit! 
    Hã???
    ''')
    print('O caviar não está na bandeja. \n')
    print_slow('Anfitrião: O Beluga! Para onde foi?')

    sleep(1)
    clear_screen()
    print(f'''
    {player.name} escapa e está andando na rua falando com a 
    Condessa Cleo por chamada de vídeo. 
    ''')
    print_slow(f'''
    {player.name}: Caviar servido, senhora. 

    Condessa Cleo: Que grosseria. Fora das latas, deixou a iguaria exposta. 

    {player.name}: Você queria o caviar. Eu entreguei. 

    Condessa Cleo: É verdade. Mas agora só podem ser comidos por um dia. 
    E não posso  consumir cem latas de caviar em um dia. 
    Dra Bellum, ative o...seja lá qual for o nome disso hoje.

    {player.name}: NÃO! 
    ''')

    sleep(0.5)
    print(f'''
    Guardas surgem na prisão onde os amigos de {player.name} estão. 
    Eles tentam lutar mas é em vão. Suas mentes serão apagadas.''')

    sleep(1)
    clear_screen()
    print_slow(f'''
    OH NÃO! Parece que estamos em um grande impasse. Teste seus limites!
    Você tentará convencer a Condessa Cleo a salvar seus amigos.
    
    Persuasão: +{player.persuasion}
    
    .....
    ''')
    sleep(1)

    if check_sucess(player.persuasion) == True:
        print(f'''
    {player.name}: Por favor! Permita que eu redima meus atos em uma nova missão.
    Darei meu máximo e reconheço o erro que cometi.
    
    Condessa Cleo afirma, relutante.

    Condessa Cleo: Está bem! Mas essa será sua última tentativa! Aguarde novas
    instruções.
        ''')
        sleep(2)
        return steel_again(player)

    else:
        print(f'''
    {player.name}: Por favor! Permita que eu redima meus atos em uma nova missão.
    Darei meu máximo e reconheço o erro que cometi.

    Condessa Cleo: Não mesmo! Apenas uma tola confiaria em uma ladra. Continuem o
    procedimento!
        ''')
        sleep(2)
        endings.bad_ending_5()


def run(player):
    player.energy_op(-1)

    clear_screen()
    print(f'''
    {player.name} sai da cozinha com um carrinho com o caviar
    ''')

    print_slow(f'''
    Garçonete grita da cozinha: Mademoiselle, pare! 
    O caviar precisa ser empratado!

    Anfitrião: Peguem-na! 

    {player.name}: Prefiro a saída dramática.
    ''')
    print(f'''
    {player.name} pega o caviar, chuta o carrinho e salta voo com o planador. 
    ''')

    sleep(3)
    clear_screen()
    print(f'{player.name} liga para Condessa Cleo.')
    print_slow(f'''
    {player.name}: Peguei os bebês Beluga. 

    Condessa Cleo: Por favor, aguarde novas instruções. 
    ''')

    return steel_again(player)


def steel_again(player):
    print(f'''
    {player.name} conversa com Player sem que Condessa Cleo consiga ouvir.
    ''')
    print_slow(f'''
    {player.name}: Player, alguma pista de Zac e Ivy? 

    Player: Ainda não. Estou procurando, mas nada ainda.
    Fique na chamada com a Condessa Cleo por mais alguns segundos,
    estou tentando rastrear.
    ''')
    sleep(0.5)
    print('''
    Condessa Cleo parece estressada na chamada.
    ''')
    print_slow(f'''
    Condessa Cleo: Conversando com mais alguém, {player.name}?
    Pelo visto estou atrapalhando alguma coisa. 
    Você deve ter assuntos mais importantes que a vida da sua equipe.

    {player.name}: Nada disso, Condessa! 
    Estou apenas admirada pela sofisticação de seu look hoje.

    Player: {player.name}, achei um sinal!
    Buscando esconderijos da V.I.L.E no Círculo Ártico. 
    Encontrei um. O que quer fazer? 
    ''')

    sleep(2)
    clear_screen()
    text = f'''
    {player.name}: Posso tentar resgatar minha equipe agora ou posso roubar
    para a V.I.L.E. uma última vez. Uma nova missão pode ser arriscada,
    mas também pode ser uma chance de manter as aparências até conseguir
    recuperar a equipe.

    Começo uma arriscada missão de resgate, ou roubo pela última vez?

    [1] Resgatar Equipe
    [2] Roubar uma última vez
    
    Sua Escolha: '''

    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return rescue_team(player)
    else:
        sleep(1)
        from modules.acts_pt import act_2_m2
        return act_2_m2.start_m2(player)  # Used to be Bad Ending 4


def rescue_team(player):
    player.lucky_op(+1)

    print_slow(f'''
    {player.name} optou por resgatar seus amigos! Entretanto, uma longa viagem
    lhe espera e para que o resgate seja feito em segurança, é necessário
    uma boa dose de sortee e energia. Hora de rodar os dados!

    Sorte: +{player.lucky}
    Energia: +{player.energy}
    
    .....
    ''')

    if check_sucess(player.lucky) == True and check_sucess(player.energy):
        clear_screen()
        sleep(1)
        return endings.good_ending_1(player)
    else:
        from modules.acts_pt import act_2_m2
        return act_2_m2.start_m2(player)
