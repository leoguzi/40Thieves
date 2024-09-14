from tkinter import *

class PlayerInterface:
    def __init__(self):
      self.main_window = Tk()
      self.main_window.title("Forty Thieves")
      
      self.main_window.geometry("850x920")
      self.main_window.iconbitmap("assets/thief.ico")
      self.main_window.resizable(False, False)
      self.main_window["bg"]="lemon chiffon"
        #conteudo da janela aqui
        
      self.main_window.mainloop()
      
      