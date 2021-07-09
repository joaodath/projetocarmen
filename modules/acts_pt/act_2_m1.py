from modules.acts_pt import endings
from modules.extras import check_sucess, print_slow, check_input, clear_screen
from time import sleep

# Starts Mission 1 from Act 2


def start_m1(player):
    clear_screen()
    print(f'''
    Após a missão em Xangai, {player.name} recebe uma ligação da V.I.L.E''')
    sleep(2)

    print_slow(f'''
    {player.name}: Está bem condessa Cleo. O que seu coração sombrio deseja? 
    Condessa Cleo: Para minha missão, quero que roube o último lote de um 
    caviar Beluga. Será servido numa festa de caridade em Mônaco. 

    Player: Localizado na Riviera Francesa, Mônaco é o segundo 
    menor país do mundo. A festa será num luxuoso hotel em Monte Carlo.
    
    {player.name} viaja para o local, visando realizar a tarefa proposta.
    ''')

    sleep(2)
    return party(player)


def party(player):
    clear_screen()
    # Storytelling
    print(f'''
    {player.name} chega à festa. 
    O anfitrião a vê e se dirige a seu encontro.''')

    sleep(2)
    print_slow(f'''
    Anfitrião da Festa: Me daria a honra dessa dança, Srta...?

    {player.name}: Santa Rosa! Srta. Santa Rosa.

    Anfitrião da Festa: Me daria a honra dessa dança, Srta. Santa Rosa?

    {player.name}: ~ Estou em missão, então deveria me concentrar e recusar. 
    Mas aceitar a dança pode ser o melhor jeito de me misturar e 
    chegar à cozinha. ~
    ''')
    sleep(3)

    clear_screen()
    text = f'''
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
    clear_screen()
    player.persuasion_op(+1)
    player.energy_op(-1)

    print_slow(f'''
    ------------
    Participar de uma bela dança com o Anfitrião da Festa foi uma ótima decisão.
    Entretanto, fazer isso lhe custou algumas coisinhas.

    Persuação: +{player.persuasion} [+1]
    Energia: +{player.energy} [-1]
    ------------
    .....
    ''')
    sleep(3)

    return steel_caviare(player)


def refuse_dance(player):
    player.persuasion_op(-1)

    print_slow(f'''
    {player.name} : Obrigado, mas valsa não é minha praia. Se quiser dançar
    tango...

    O Anfitrião se despede cordialmente e vai embora.

    ------------
    Opa! As vezes é bom realizar alguns sacrificios para se misturar no local...

    Persuação: +{player.persuasion} [-1]
    ------------
    ....
    ''')
    sleep(3)

    return steel_caviare(player)


def steel_caviare(player):
    clear_screen()
    print(f'''
    {player.name} observa dois garçons indo para a cozinha.
    ''')
    sleep(2)

    print_slow(f'''
    {player.name}: Avistei as ovas. 
    
    Player: Como você vai pegar?

    {player.name}: Posso esconder e sair furtivamente, 
    ou pegar e sair correndo.
    ''')
    sleep(3)

    clear_screen()
    text = f'''
    Disfarço e escondo o caviar ou roubo e saio correndo?
    
    [1] Disfarçar e Capturar
    [2] Roubar e Correr
    
    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        clear_screen()

        print_slow(f'''
    ------------
    Ótima escolha! Entretanto, você precisará de sorte para o disfarce ser de
    acordo com o planejado.

    Sorte: +{player.lucky}
    ------------
    ....
        ''')
        sleep(2)

        if check_sucess(player.lucky) == True:
            sleep(1)
            return hide(player)
        else:
            clear_screen()
            print_slow(f'''
    Infelizmente o disfarce não deu muito certo... Um garçom reconheceu você!
            ''')
            sleep(3)
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

    sleep(2)
    print(f'''
    Guardas surgem na prisão onde os amigos de {player.name} estão. 
    Eles tentam lutar mas é em vão. Suas mentes serão apagadas.''')
    sleep(3)

    clear_screen()
    print_slow(f'''
    ------------
    OH NÃO! Parece que estamos em um grande impasse. Hora de testar seus limites!
    Você tentará convencer a Condessa Cleo a salvar seus amigos.
    
    Persuasão: +{player.persuasion}
    ------------
    .....
    ''')
    sleep(2)

    if check_sucess(player.persuasion) == True:
        clear_screen()
        print_slow(f'''
    {player.name} implora por uma nova oportunidade.

    {player.name}: Por favor, me dê uma nova oportunidade! Prometo que darei
    meu máximo em ser discreta. Afinal, sou a melhor opção que vocês possuem.
    
    Condessa Cleo afirma, relutante.

    Condessa Cleo: Está bem! Mas essa será sua última tentativa! Aguarde novas
    instruções.
        ''')
        sleep(2)
        return steel_again(player)

    else:
        clear_screen()
        print(f'''
    {player.name} implora por uma nova oportunidade.

    {player.name}: Por favor, me dê uma nova oportunidade! Prometo que darei
    meu máximo em ser discreta. Afinal, sou a melhor opção que vocês possuem.

    Condessa Cleo: Não mesmo! Apenas uma tola confiaria em uma ladra. Continuem o
    procedimento!
        ''')
        sleep(2)
        endings.bad_ending_5()


def run(player):
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
    sleep(2)

    print_slow(f'''
    {player.name}: Peguei os bebês Beluga. 

    Condessa Cleo: Por favor, aguarde novas instruções. 
    ''')
    sleep(2)

    return steel_again(player)


def steel_again(player):
    print(f'''
    {player.name} conversa com Player sem que Condessa Cleo consiga ouvir.
    ''')
    sleep(2)

    print_slow(f'''
    {player.name}: Player, alguma pista de Zac e Ivy? 

    Player: Ainda não. Estou procurando, mas nada ainda.
    Fique na chamada com a Condessa Cleo por mais alguns segundos,
    estou tentando rastrear.
    ''')
    sleep(1)

    print('''
    Condessa Cleo parece estressada na chamada.
    ''')
    sleep(2)

    print_slow(f'''
    Condessa Cleo: Conversando com mais alguém, {player.name}?
    Pelo visto estou atrapalhando alguma coisa. 
    Você deve ter assuntos mais importantes que a vida da sua equipe.

    {player.name}: Nada disso, Condessa! 
    Estou apenas admirada pela sofisticação de seu look hoje.

    Player: {player.name}, achei um sinal!
    Buscando esconderijos da V.I.L.E no Círculo Ártico. 
    Encontrei um. O que quer fazer?

    {player.name}: ~ Posso tentar resgatar minha equipe agora ou posso roubar
    para a V.I.L.E. uma última vez. Uma nova missão pode ser arriscada,
    mas também pode ser uma chance de manter as aparências até conseguir
    recuperar a equipe. ~
    ''')
    sleep(3)

    clear_screen()
    text = f'''
    Começo uma arriscada missão de resgate, ou roubo pela última vez?

    [1] Resgatar Equipe
    [2] Roubar uma última vez
    
    Sua Escolha: '''

    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return endings.good_ending_1(player)
    else:
        sleep(1)
        from modules.acts_pt import act_2_m2
        return act_2_m2.start_m2(player)  # Used to be Bad Ending 4