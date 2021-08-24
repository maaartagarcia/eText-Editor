from tkinter import *
from tkinter.scrolledtext import *
import file_menu
import edit_menu
import format_menu
import help_menu

# MAIN WINDOW OF eTEXT, CONTAINS THE ROOT AND THE MENU

root = Tk()
root.title("eText - Untitled")
root.geometry("800x600+700+70")
root.resizable(0,0)
root.iconbitmap("C:/Users/marta/PycharmProjects/GUI/venv/Scripts/Code/eText/notebook.ico")
root.configure(bg = '#F6C8C7')

initial_f = "Consolas"
initial_n = 14
initial_s = "normal"
initial_c = "black"

text = ScrolledText(root, tabs = ('40','90','130'), spacing1 = 3, spacing2 = 5, spacing3 = 5, state = 'normal', wrap = 'word', height = 20, width = 60, font = (initial_f, initial_n, initial_s), borderwidth = '4' , relief = 'sunken', fg = initial_c, undo = True)
text.pack(padx = 15, pady = 15, ipadx = 10, ipady = 10, fill = 'both', expand = True)
#text.focus_set()

menubar = Menu(root)

file_menu.main(root,text, menubar)
edit_menu.main(root,text, menubar)
format_menu.main(root,text,menubar)
help_menu.main(root,text, menubar)

root.mainloop()

# SIGNIFICADOS
# spacing1 -> Espacio o margen vertical donde podrá empezar el texto ; spacing2 -> Debajo de cada línea ; spacing3 -> igual que spacing2 pero en otras situaciones
