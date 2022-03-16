import tkinter as tk
import datetime

class TelaPrincipal:
    def __init__(self, master):
        self.screen = master
        self.lblWatch = tk.Label(
            self.screen, font=('Calibri', 30), fg='Black')
        self.lblWatch.pack(pady=30, padx=30)
        self.alteracao()


    def alteracao(self):
        now = datetime.datetime.now()
        self.lblWatch['text'] = now.strftime('%H:%M:%S')
        self.screen.after(1000, self.alteracao)

rootWindow = tk.Tk()
TelaPrincipal(rootWindow)
rootWindow.mainloop()