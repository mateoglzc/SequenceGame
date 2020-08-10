class Player():
    ''' A class that defines a player.
    Atributes:
        name
        turn
    '''
    # Constructor

    def __init__(self):
        self.name = ""
        self.turn = False

    def ChangeTurn(self):

        if self.turn:
            self.turn = False
        else:
            self.turn = True

    def ChangeName(self, name: str):
        self.name = name