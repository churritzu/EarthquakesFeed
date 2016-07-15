from tkinter import *
from tkinter import ttk
from vistas.HelpMenu import HelpMenu
from vistas.FileMenu import FileMenu

#TODO: Solo dejar codigo relacionado a la ventana principal aqui.
#TODO: Tengo que refactorizar todas las ventanas en sus propias clases

class MainWindow:
	def __init__(self):
		self.main_window = Tk()
		self.main_window.title("Earthquakes Feeds")
		self.main_window.config(height=600, width=800, background="#222")

		self.main_window.config(menu=self.top_menu())
		self.main_window.mainloop()

	def top_menu(self):
		main_menu = Menu(self.main_window)
		file = FileMenu(main_menu)
		help = HelpMenu(main_menu)
		main_menu.add_cascade(label="File", menu=file.get_menu())
		main_menu.add_cascade(label="Help", menu=help.get_menu())
		return main_menu

if __name__ == "__main__": pass