class Player:
    def __init__(self):
        self.identifier = ""  #   string
        self.name = ""  #   string
        self.color = None # string: RED or BLUE
        self.pieces = []  # Piece[]
        self.turn = False  # bool
        self.winner = False  # bool
        self.selected_piece = None
        self.score = 0
        
    def initialize(self, a_color, a_id, a_name):  # Name!!!!
        self.reset()
        self.identifier = a_id #string
        self.color = a_color #string: RED or BLUE
        self.name = a_name  #   string

    def reset(self):
        self.identifier = ""  #   string
        self.name = ""  # string
        self.color = None  # string: RED or BLUE
        self.pieces = [] # Piece[]
        self.turn = False  # bool
        self.winner = False  # bool
        self.selected_piece = None  #Piece
        self.score = 0

    def set_score(self):
        self.score = self.score + 1 #CALCULAR PONTUAÇÃO COM BASE NAS PEÇAS QUE O JOGADOR AINDA TEM
   
    def toogle_turn(self):
       self.turn = not self.turn

    def get_turn(self):
        return self.turn

    def get_identifier(self):
        return self.identifier

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    def get_winner(self):
        return self.winner

    def set_winner(self):
        self.winner = True

    def get_selected_piece(self):
        return self.selected_piece

    def set_selected_piece(self, a_piece):
        self.selected_piece = a_piece
    
    def get_pieces(self):
        return self.pieces