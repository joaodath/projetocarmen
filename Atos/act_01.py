from time import sleep


class Ato_um():
    def __init__(self, personagem):
        self.personagem = personagem
        self.ending = None

    def act_one(self):
        print('You are um ACT ONE\n')
        sleep(2)
        return self.begin()

    def begin(self):
        choice = input(
            'You begin the game. Choices:\nTop\nZipline\n').strip().upper()
        if choice == 'TOP':
            return self.begin_elevator()
        else:
            return self.begin_zipline()

    def begin_elevator(self):
        print('Welcome to the elevator!\n')
        sleep(2)
        return self.vile_one()

    def begin_zipline(self):
        print('Welcome to the zipline!\n')
        sleep(2)
        return self.vile_one()

    def vile_one(self):
        choice = input(
            'You are in the Vile! Choices:\nRescue\nLeave\n').strip().upper()
        if choice == 'RESCUE':
            return self.ending_one()
        else:
            return self.tigress()

    def ending_one(self):
        sleep(2)
        self.ending = 1

    def tigress(self):
        choice = input(
            'You find the Tigress! Choices:\nHELP\nLEAVE\n').strip().upper()
        if choice == 'HELP':
            return self.acme_one()
        else:
            return self.acme_one()

    def acme_one(self):
        sleep(2)
        choice = input(
            'You are in ACME ONE. Choices:\nRIDE\nDONT RIDE\n').strip().upper()
        if choice == 'Ride':
            return self.ending_two()
        else:
            self.ending = 3

    def ending_two(self):
        sleep(2)
        self.ending = 2

    def get_ending(self):
        if self.ending == 1:
            print('First Ending Reached')
        elif self.ending == 2:
            print('Second Ending Reached')
        else:
            print('Third Ending Reached')
