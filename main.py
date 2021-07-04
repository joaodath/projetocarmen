from personagem import Personagem
from Atos.act_01 import Ato_um


def try_again():
    response = input('Você deseja jogar mais uma vez? [S/N] ').strip().upper()

    while response not in 'SN':
        print('Resposta não entendida. Tente Novamente.\n')

        response = input(
            'Você deseja jogar mais uma vez? [S/N] ').strip().upper()

    return response


if __name__ == "__main__":

    while True:

        carmen = Personagem('Carmen Sandiego')
        ato_um = Ato_um(carmen)
        ato_um.act_one()
        ato_um.get_ending()

        if try_again() == 'N':
            break
