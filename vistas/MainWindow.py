import os
from tkinter import *
from tkinter import ttk

from misc import Globales

#TODO: Solo dejar codigo relacionado a la ventana principal aqui.
#TODO: Tengo que refactorizar todas las ventanas en sus propias clases

class MainWindow:
	about_window = None
	def __init__(self):
		self.main_window = Tk()
		self.main_window.title("Earthquakes Feeds")
		self.main_window.config(height=600)
		self.main_window.config(width=800)
		self.main_window.config(background="#222")

		self.main_window.config(menu=self.top_menu())
		self.main_window.mainloop()

	def top_menu(self):
		main_menu = Menu(self.main_window)

		#File Cascade Menu
		file_menu = Menu(main_menu, tearoff=0)
		file_menu.add_command(label="Settings...", command=lambda: print("Setting not do anything!!!"))
		file_menu.add_separator()
		file_menu.add_command(label="Close", command=lambda: self.close())
		main_menu.add_cascade(label="File", menu=file_menu)

		# Help Cascade Menu
		help_menu = Menu(main_menu, tearoff=0)
		help_menu.add_command(label="About...", command=lambda: self.about())
		main_menu.add_cascade(label="Help", menu=help_menu)

		return main_menu

	def close(self): self.main_window.quit()

	def close_about(self): self.about_window.withdraw()

	def about(self):
		if self.about_window:
			self.about_window.state("normal")
		else:
			self.about_window = Toplevel(self.main_window, pady=10)
			self.about_window.title("About Us...")
			self.about_window.resizable(width=FALSE, height=FALSE)
			self.about_window.transient(self.main_window)
			self.about_window.config(background="#666")

			imagen = PhotoImage(file=os.getcwd()+"/_img/logo.png")
			imagen = imagen.subsample(2,2)
			img_label = Label(self.about_window)
			img_label.image = imagen
			img_label.config(image=imagen, background="#666")
			img_label.pack()

			txt = "Version:\n"+Globales.__version__+"\n\nWebsite:\n"+Globales.__url__+"\n\n"
			txt += "Author:\n"+Globales.__author__
			txt_label = Label(self.about_window, text=txt, background="#666").pack()

			btn = ttk.Button(self.about_window)
			btn.config(text="close",command=lambda: self.close_about())
			btn.pack(side=BOTTOM)

			sw = self.about_window.winfo_screenwidth() / 2
			sh = self.about_window.winfo_screenheight() / 2
			px = str(int(sw-150))
			py = str(int(sh-160))
			self.about_window.geometry("300x320+"+px+"+"+py)
			self.about_window.update_idletasks()
			self.about_window.overrideredirect(True)

if __name__ == "__main__": pass