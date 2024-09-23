import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

class PlayerInterface:
    def __init__(self):
      self.main_window = tk.Tk()
      self.fill_main_window() # Fill the main window with the game interface
      player_name = simpledialog.askstring(title="Player identification", prompt="What is your name?")
      message = "Welcome to 40 Thiefs, " + player_name + "!"
      messagebox.showinfo("Welcome!", message, type="ok")
      self.main_window.mainloop()
      
      
    def fill_main_window(self):  
      self.main_window.title("Forty Thieves")
      self.main_window.geometry("620x820")
      self.main_window.resizable(False, False)
      self.main_window["bg"]="azure3"
      
      self.title_frame = tk.Frame(self.main_window, padx=10, pady=10, bg="azure3")
      self.title_frame.grid(row=0, column=0)
      self.table_frame = tk.Frame(self.main_window, padx=60, pady=20, bg="azure3")
      self.table_frame.grid(row=1, column=0)
      self.info_frame = tk.Frame(self.main_window, padx=10, pady=10, bg="azure3")
      self.info_frame.grid(row=2, column=0)
     
      
      
      self.orange_circle = tk.PhotoImage(file="src/assets/orange_circle.png")
      self.blue_circle = tk.PhotoImage(file="src/assets/blue_circle.png")
      self.white_square = tk.PhotoImage(file="src/assets/white_square.png")
      
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
              aLabel = tk.Label(self.table_frame, borderwidth=1, relief="solid", image=image, width=60, height=60)
              aLabel.grid(row=x, column=y)
              aLabel.bind(
                  "<Button-1>", lambda event, a_line=x, a_column=y: self.select_board_place(event, a_line, a_column)
              )
              a_column.append(aLabel)
            self.board_view.append(a_column)
            
            self.message_label = tk.Label(self.title_frame, bg="azure3", text="40 Thiefs", font="arial 30")
            self.message_label.grid(row=0, column=0)
            self.turn_label = tk.Label(self.info_frame, bg="azure3", text="Sua vez!", font="arial 24")
            self.turn_label.grid(row=0, column=0)
            
    def select_board_place(self, event, line, column):
      message = "You selected the position: " + str(line) + ", " + str(column)
      messagebox.showinfo("Click!", message, type="ok")
       