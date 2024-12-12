class Position:
    def __init__(self, a_line, a_column, a_score_weight):
        self.line = a_line
        self.column = a_column
        self.score_weight =  a_score_weight
        self.occupant = None


    def get_line(self):
        return self.line

    def get_column(self):
        return self.column
    
    def get_occupant(self):
        return self.occupant
    
    def set_occupant(self, piece):
        self.occupant = piece
