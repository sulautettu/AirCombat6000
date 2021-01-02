class player (object):
    playerList = []

    def __init__(self, name="Maverick"):
        self.name = name
        self.playerList.append(self)