import os
from tkinter import *
from tkinter import ttk
from misc import Globales

class HelpMenu():
	about_window = None
	about_width = 150
	about_height = 160

	def __init__(self, master):
		self.master = master
		self.menu = Menu(self.master, tearoff=0)
		self.menu.add_command(label="About...", command=lambda: self.get_about())

	def get_menu(self):
		return self.menu

	def close_about(self):
		self.about_window.destroy()
		self.about_window = None

	def get_about_x(self):
		sw = self.about_window.winfo_screenwidth() / 2
		return str(int(sw - self.about_width))

	def get_about_y(self):
		sh = self.about_window.winfo_screenheight() / 2
		return str(int(sh - self.about_height))

	def get_about(self):
		if not self.about_window:
			self.about_window = Toplevel(self.master, pady=10, background="#666")
			self.about_window.title("About Us")
			self.about_window.resizable(width=FALSE, height=FALSE)
			self.about_window.transient()
			self.about_window.geometry("300x320+" + self.get_about_x() + "+" + self.get_about_y())
			self.about_window.update_idletasks()
			self.about_window.overrideredirect(True)

			imagen = PhotoImage(file=os.getcwd() + "/_img/logo.png")
			imagen = imagen.subsample(2, 2)
			img_label = Label(self.about_window)
			img_label.image = imagen
			img_label.config(image=imagen, background="#666")
			img_label.pack()

			txt = "Version:\n" + Globales.__version__ + "\n\nWebsite:\n" + Globales.__url__ + "\n\n"
			txt += "Author:\n" + Globales.__author__
			txt_label = Label(self.about_window, text=txt, background="#666").pack()

			btn = ttk.Button(self.about_window)
			btn.config(text="close", command=lambda: self.close_about())
			btn.pack(side=BOTTOM)



if __name__ == "__main__": pass