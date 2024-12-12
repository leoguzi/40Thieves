import player
import position
import piece
import ui_image


# match_status
# 1 - sem partida (estado inicial)
# 2 - partida concluída (com ganhador, sem empate)
# 3 - sua vez, partida em andamento (aguardando o inicio da jogada)
# 4 - sua vez, partida em andamento (aguardando a confirmação da jogada)
# 5 - vez do oponente, partida em andamento (aguardando movimento do oponente)
# 6 - partida abandonada pelo oponente

class Board:
    def __init__(self):
        self.local_player = player.Player()
        self.remote_player = player.Player()
        self.positions = []
        self.local_player.initialize("RED", "Red player", "Red player")
        self.remote_player.initialize("BLUE", "Blue player", "Blue player")
        self.match_status = 1
        self.selected_location = None
        self.first_local_action = None
        self.second_local_action = None
        self.positions = []
        for y in range(8):
            for x in range(9):
              if (x < 1 and y > 4 or x < 1 and y < 3):
                continue
              if (x < 3 and y > 5 or x < 3 and y < 2):
                continue
              if (x < 4 and y > 6 or x < 4 and y < 1):
                continue
              if(x < 4):
                  match y:
                      case 3:
                        self.positions.append(position.Position(x, y, 1))
                      case 2:
                        self.positions.append(position.Position(x, y, 3)) 
                      case 1:
                        self.positions.append(position.Position(x, y, 10)) 
                      case 0:
                        self.positions.append(position.Position(x, y, 25))
              else: 
                new_position = position.Position(x, y, -1)
                piace_player = self.local_player if (y) % 2 == 0 else self.remote_player
                new_piece = piece.Piece(piace_player, new_position)
                self.positions.append(new_position)
    
    def match_status(self):
        return self.match_status
    
    def get_status(self):
        ui_image = ui_image.UiImage()
        #       message
        turn_player = self.get_turn_player()
        if not self.regular_move:
            ui_image.setMessage(turn_player.get_name() + ", jogada irregular")
        else:
            if self.match_status == 1:
                ui_image.setMessage("40 Ladrões")
            elif self.match_status == 2:
                ui_image.setMessage("Vencedor: " + self.get_winner_name())
            elif self.match_status == 3:
                ui_image.setMessage(turn_player.get_name() + ", selecione peça ou posição")
            elif self.match_status == 4:
                ui_image.setMessage(turn_player.get_name() + ", selecione posição destino")
            elif self.match_status == 5:
                ui_image.setMessage("Aguardando lance do adversário: " + self.remote_player.get_name())
            elif self.match_status == 6:
                ui_image.setMessage("Adversário abandonou a partida")
                #    pieces
        player1_pieces = self.local_player.get_pieces()
        ui_image.set_player1_pieces(player1_pieces)
        player2_pieces = self.remote_player.get_pieces()
        ui_image.set_player2_pieces(player2_pieces)

        #    selected board position
        if self.selected_location != None:
            selected_position = []
            selected_position.append(self.selected_location.get_line())
            selected_position.append(self.selected_location.get_column())
            ui_image.set_selected_position(selected_position)
            #    board positions (9x8)
        for y in range(8):
            for x in range(9):
                occupant_piece = self.positions[x][y].get_occupant()
                if occupant_piece == None:
                    value = "WHITE"
                if occupant_piece.get_owner() == self.local_player:
                    value = "RED"
                elif occupant_piece.get_owner() == self.remote_player:
                    value = "BLUE"
                ui_image.setValue(x, y, value)
                #    return status
        return ui_image
    
    def get_turn_player(self):
        if self.local_player.get_turn():
            return self.local_player
        elif self.remote_player.get_turn():
            return self.remote_player
        else:
            return None