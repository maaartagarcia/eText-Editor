from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import * #Al importarlos de esta forma utilizo directamente sus métodos
import sys

# Voy a necesitar filedialog para utilizar el explorador de archivos
# Voy a necesitar messageboxa para capturar excepciones con los ficheros y
# responder con mensajes de error

class File(): # Una instancia de esta clase permitirá realizar las funciones de los "botones" Save, Open etc
    def __init__(self, text, root):
        self.path = None
        self.root = root
        self.text = text

    def new(self, *args):
        self.path = None
        self.root.title("eText - Untitled")
        self.text.delete(1.0,END)

    def open(self, *args):
        filepath = askopenfilename(initialdir = 'C:/Users/marta/Desktop' ,title = 'Select A File', filetypes = (("Text Files", "*.txt"),))
        try:
            self.path = filepath
            list = filepath.split("/")
            self.root.title("eText - "+ list[len(list)-1])

            filepath = open(filepath,'r')
            content = filepath.read()
            self.text.delete(1.0,END)
            self.text.insert(END,content)
            filepath.close()
        except:
            showerror(title='Something went wrong', message='Unfortunately your file couldn´t be opened')

    def save(self, *args):
        if(self.path != None):
            filepath = open(self.path, 'w')
            filepath.write(self.text.get(1.0, END))
            filepath.close()
            return None
        else:
            self.saveAs()

    def saveAs(self, *args):
        filepath = asksaveasfilename(initialdir = 'C:/Users/marta/Desktop' ,title = 'Select A File', filetypes = (("Text Files", "*.txt"),))
        try:
            self.path = filepath
            list = filepath.split("/")
            self.root.title("eText - " + list[len(list) - 1])

            filepath = open(filepath, 'w')
            filepath.write(self.text.get(1.0,END))
            filepath.close()
            showinfo(message = 'Your file has been succesfully saved')
        except:
            showerror(title = 'Something went wrong', message = 'Unfortunately your file couldn´t be saved')

    def quit(self, *args):
        answer = askyesno(message = 'Are you sure you want to quit?', title = 'Quit')
        if answer == True:
            self.root.destroy()
        else:
            return None

def main(root, text, menubar):
    file = File(text, root)
    fileMenu = Menu(menubar)
    fileMenu.add_command(label='New', command = file.new, accelerator = 'Ctrl+N')
    fileMenu.add_command(label = 'Open', command = file.open, accelerator = 'Ctrl+Shift+O')
    fileMenu.add_command(label = 'Save', command = file.save, accelerator = 'Ctrl+S')
    fileMenu.add_command(label='Save As', command = file.saveAs, accelerator = 'Ctrl+Shift+S')
    fileMenu.add_separator()
    fileMenu.add_command(label='Quit', command = file.quit, accelerator = 'Ctrl+Q')
    menubar.add_cascade(label='File', menu = fileMenu)
    root.config(menu = menubar)

    # Atajos
    root.bind_all('<Control-n>', file.new)
    root.bind_all('<Control-O>', file.open)
    root.bind_all('<Control-s>', file.save)
    root.bind_all('<Control-S>', file.saveAs)
    root.bind_all('<Control-q>', file.quit)

if __name__ == "__main__":
    print("Run main.py")

# SIGNIFICADOS
# Cuando abres un fichero, ese fichero es una instancia distinta del resto
# Sí requiere de un constructor porque requiere de atributos como filename, trabaja
# el mismo texto que todo el programa, y con botones como "Quit" se cierra la ventana ppal
# así que una instancia File debe poder acceder a todas esas cosas + Constructor
# El método Save no funcionará cuando el fichero no haya sido guardado previamente, porque la ruta no existirá,
# será o untitled o none, es decir, inexistente --> Se captura el error con try - catch
# Cuando abro un archivo, el atributo filename varía, si escribo en uno nuevo sin guardar, filename será none