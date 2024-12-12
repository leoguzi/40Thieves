class Piece:
    def __init__(self, a_player, a_position):
        self.player = a_player
        self.position = a_position
        self.position.set_occupant(self)
        self.player.pieces.append(self)
        
        def set_position(self, a_position):
            self.position = a_position
            self.position.set_occupant(self)
            
        def get_position(self):
            return self.position