from tkinter import *
from tkinter import ttk
from vistas.HelpMenu import HelpMenu
from vistas.FileMenu import FileMenu

class MainWindow:
	init_width =800
	init_height = 600

	def __init__(self):
		self.main_window = Tk()
		self.main_window.title("Earthquakes Feeds")
		self.main_window.config(height=self.init_height, width=self.init_width)
		self.main_window.config(menu=self.top_menu())

		#Styles
		sf = ttk.Style()
		sf.configure("TFrame", background="#333")
		sf.configure("TLabel", background="#333", foreground="#fff")

		#Frames
		main_frame = ttk.Frame(self.main_window, padding=5, width=self.init_width, height=self.init_height)
		main_frame.pack_propagate(0)

		#Label
		ttk.Label(main_frame).pack()

		main_frame.pack(fill=BOTH, expand=1)

		self.main_window.mainloop()

	def top_menu(self):
		main_menu = Menu(self.main_window)
		file = FileMenu(main_menu)
		help = HelpMenu(main_menu)
		main_menu.add_cascade(label="File", menu=file.get_menu())
		main_menu.add_cascade(label="Help", menu=help.get_menu())
		return main_menu

	def search(self):
		print("Searching....")

if __name__ == "__main__": pass