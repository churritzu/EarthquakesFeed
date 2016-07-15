from tkinter import *
from tkinter import ttk

class FileMenu:
	def __init__(self, master):
		self.master = master
		self.menu = Menu(self.master, tearoff=0)
		self.menu.add_command(label="Settings...", command=lambda: print("Setting not do anything!!!"))
		self.menu.add_separator()
		self.menu.add_command(label="Close", command=lambda: self.close())

	def get_menu(self):
		return self.menu

	def close(self):
		self.master.quit()

if __name__ == "__main__": pass