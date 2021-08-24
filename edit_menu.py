from tkinter import *
from tkinter import font

class Edit():
    def __init__(self, text):
        self.text = text
        self.clipboard = None # Texto seleccionado

    def undo(self, *args):
        self.text.edit_undo()

    def redo(self, *args):
        self.text.edit_redo()

    def copy(self, *args):
        try:
            self.text.clipboard_clear()
            self.text.clipboard_append(self.text.selection_get())
        except:
            pass

    def paste(self, *args):
        try:
            self.text.insert(INSERT, self.text.clipboard_get())
        except:
            pass

    def cut(self, *args):
        try:
            self.copy()
            self.text.delete(SEL_FIRST, SEL_LAST)
        except:
            pass

    def select_all(self, *args):
        self.text.tag_add(SEL, "1.0", END)
        self.text.mark_set(INSERT, "1.0")
        self.text.see(INSERT)
        return "break"

def main(root, text, menubar):
    edit = Edit(text)
    editMenu = Menu(menubar)
    editMenu.add_command(label = 'Undo', command = lambda : edit.undo(False), accelerator = 'Ctrl+U') # Undo y Redo ya existen y actuán directamente sobre el
    # widget ScrolledText pero hace falta indicar en la configuración de ScrolledText que va a ser utlizado
    editMenu.add_command(label='Redo', command = lambda : edit.redo(False), accelerator = 'Ctrl+R')
    editMenu.add_command(label='Copy', command = lambda : edit.copy(False), accelerator = 'Ctrl+Shift+C')
    editMenu.add_command(label='Paste', command = lambda : edit.paste(False), accelerator  = 'Ctrl+P')
    editMenu.add_command(label='Cut', command = lambda : edit.cut(False), accelerator = 'Ctrl+X')
    editMenu.add_separator()
    editMenu.add_command(label='Select All', command = edit.paste, accelerator = 'Ctrl+A')
    menubar.add_cascade(label = 'Edit', menu = editMenu)
    root.config(menu = menubar)

    # Shortcuts
    root.bind_all("<Control-u>", edit.undo)
    root.bind_all("<Control-r>", edit.redo)
    root.bind_all("<Control-C>", edit.copy)
    root.bind_all("<Control-p>", edit.paste)
    root.bind_all("<Control-x>", edit.cut)
    root.bind_all("<Control-a>", edit.select_all)

if __name__ == "__main__":
    print("Run main.py")

# SIGNIFICADOS
# Bold Pasos:
    # Creación del tag
        # 1 --> Instancia de la clase Font --> Cuelga del texto, y text.cget('font') leerá los valores del atributo font del widget
        # 2 --> Configuro la nueva instancia Font creada con weigth = 'bold' o slank = 'italic'
    # Configuración del tag
        # 1 --> text.tag_configure(tagname, font = new_font) Establece como la fuente del widget nueva, y le asigna un nombre a la misma
        # El nombre del tag será a partir de ahora tagname
    # Un - bold o bold
        # 1 --> Creación de current_tags --> text.tag_names("sel.first"), recoge los tags presentes en la primera letra seleccionada o subrayada
        # 2 --> Si tagname está entre los current_tags, es decir, has sido ya utilizado, elimino de los tags que están actuando sobre
        # el widget text ese mismo, desde donde lo hemos seleccionado de inicio a fin
        # text.tag_remove("bold", inicio_seleccion, fin_seleccion) --> Donde inicio y fin son sel.first y sel.last

# ShortCuts
    # Especificar el accelerator en la opción del submenú, definir con bind_all sobre la ventana ppal
    # root.bind_all(event, action) evento que se tiene que dar, qué acción conlleva
    # El método estará recibiendo un evento / *args y text.edit_undo lleva ()