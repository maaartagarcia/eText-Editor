from tkinter import *
from tkinter.messagebox import *
import sys

class Help():
    def about(root):
        showinfo(title = 'eText - About', message = 'eText Alpha version')

# help_menu.main(x,y,z) accede a este método al ejecutarse main.py como programa principal
def main(root, text, menubar):
    help = Help() # Intancia de la clase help, es decir, crea un desplegable que atiende a las funciones definidas en Help()
    helpMenu = Menu(menubar) # Menú desplegable que cuelga del menubar principal
    helpMenu.add_command(label = 'About', command = help.about)
    menubar.add_cascade(label = 'Help', menu = helpMenu)

    root.config(menu = menubar)

if __name__ == "__main__":
    print("Run main.py")

# SIGNIFICADOS
# sys permite actuar sobre las variables pasadas mediante el intérprete al ejecutar el programa (sys.argv crea una lista con ellos)
# Cada llamada o ejecución del programa pasa al main de este fichero los argumentos, se crea el menú, se crea una instancia no estática
# de ayuda con la cual accedemos al método about de las instancias de su clase
# Método about es el que actúa cuando se utiliza el botón "About" del menú desplegable
# menu = menubar establece a menubar en la ventana principal como su menú padre en la jerarquía, al igual que
# menubar.add_cascade() establece a menubar como padre respecto de helMenu
# Jerarquía establecida: root --> menubar --> helpmenu