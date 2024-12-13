from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from board import Board
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor

class PlayerInterface(DogPlayerInterface):
    def __init__(self):
      self.main_window = Tk()
      self.fill_main_window() # Fill the main window with the game interface
      self.board = Board()
      gameState = self.board.get_status()
      self.update_gui(gameState)
      player_name = simpledialog.askstring(title="Identificação do jogador", prompt="Como você se chama?")
      self.dog_server_interface = DogActor()
      message = self.dog_server_interface.initialize(player_name, self)
      messagebox.showinfo("Bem vindo!", message, type="ok")
      self.main_window.mainloop()
      
      
    def fill_main_window(self):  
      self.main_window.title("40 Ladrões")
      self.main_window.geometry("620x820")
      self.main_window.resizable(False, False)
      self.main_window["bg"]="azure3"
      
      self.title_frame = Frame(self.main_window, padx=10, pady=10, bg="azure3")
      self.title_frame.grid(row=0, column=0)
      self.table_frame = Frame(self.main_window, padx=60, pady=20, bg="azure3")
      self.table_frame.grid(row=1, column=0)
      self.info_frame = Frame(self.main_window, padx=10, pady=10, bg="azure3")
      self.info_frame.grid(row=2, column=0)
     
      
      
      self.orange_circle = PhotoImage(file="../src/assets/orange_circle.png")
      self.blue_circle = PhotoImage(file="../src/assets/blue_circle.png")
      self.white_square = PhotoImage(file="../src/assets/white_square.png")
      
      self.board_view = []
      for y in range(8):
            for x in range(9):
              if (x < 1 and y > 4 or x < 1 and y < 3):
                continue
              if (x < 3 and y > 5 or x < 3 and y < 2):
                continue
              if (x < 4 and y > 6 or x < 4 and y < 1):
                continue
              if(x<4):
                image = self.white_square
              else:
                image = self.blue_circle if (y) % 2 == 0 else self.orange_circle
              
              a_column = []  #column
              aLabel = Label(self.table_frame, borderwidth=1, relief="solid", image=image, width=60, height=60)
              aLabel.grid(row=x, column=y)
              aLabel.bind(
                  "<Button-1>", lambda event, a_line=x, a_column=y: self.select_board_place(event, a_line, a_column)
              )
              a_column.append(aLabel)
            self.board_view.append(a_column)
            
      self.message_label = Label(self.title_frame, bg="azure3", text="40 Ladrões", font="arial 30")
      self.message_label.grid(row=0, column=0)
      self.turn_label = Label(self.info_frame, bg="azure3", text="Sua vez!", font="arial 24")
      self.turn_label.grid(row=0, column=0)
      self.send_move_button = Button(self.info_frame, text="Enviar jogada", font="arial 16", bg="azure4", command=self.send_move)
      self.send_move_button.grid(row=1, column=0)
            
            
      #creates the game menu  
      self.menubar = Menu(self.main_window)
      self.menubar.option_add("*tearOff", FALSE)
      self.main_window["menu"] = self.menubar
      # add options to the menu bar:
      self.menu_file = Menu(self.menubar)
      self.menubar.add_cascade(menu=self.menu_file, label="Menu")
      # add options to the dropdown menus
      self.menu_file.add_command(label="Iniciar jogo", command=self.start_match)
    
    def select_board_place(self, event, line, column):
      message = "Você seleconou a posição: " + str(line) + ", " + str(column)
      messagebox.showinfo("Click!", message, type="ok")
      
    def start_match(self):
      start_status = self.dog_server_interface.start_match(2)
      message = start_status.get_message()
      messagebox.showinfo(message=message)
      
    def receive_start(self, start_status):
      message = start_status.get_message()
      messagebox.showinfo(message=message)
      
    def send_move(self):
      message = "Sua jogada foi enviada!"
      messagebox.showinfo("Jogada enviada", message, type="ok")
      
    def update_gui(self, gameState):
      # message = gameState.get_message()
      # self.message_label.config(text=message)
      # player1_pieces = gameState.get_player1_pieces()
      # player2_pieces = gameState.get_player2_pieces()
      # for piece in player1_pieces:
      #   line = piece.get_position().get_line()
      #   column = piece.get_position().get_column()
      #   self.board_view[line][column].config(image=self.orange_circle)
      # for piece in player2_pieces:
      #   line = piece.get_position().get_line()
      #   column = piece.get_position().get_column()
      #   self.board_view[line][column].config(image=self.blue_circle)
      # if gameState.get_status() == 3:
      #   self.turn_label.config(text="Sua vez!")
      # else:
      #   self.turn_label.config(text="Vez do adversário!")
      pass
       