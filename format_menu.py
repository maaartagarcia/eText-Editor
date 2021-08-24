from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.font import Font, families

class Format():
    def __init__(self, root, text):
        self.text = text # Realiza cambios sobre el texto
        self.root = root

    def font_color(self,*args):
        (triple, hexstr) = askcolor()
        if hexstr:
            self.text.config(fg = hexstr)

    def bg_color(self,*args):
        (triple, hexstr) = askcolor()
        if hexstr:
            self.text.config(bg=hexstr)

    def bold(self, *args):
        try:
            bold_font = font.Font(self.text, self.text.cget("font")) # Cuelga de text y trackea la fuente del texto
            bold_font.configure(weight = "bold") # Servirá para cambiar el weight del texto a bold

            self.text.tag_configure("bold", font = bold_font) # Nombre y el cambio de fuente corresponde a bold_font
            current_tags = self.text.tag_names("sel.first") # Tags presentes en el texto

            if "bold" in current_tags:
                self.text.tag_remove("bold", "sel.first", "sel.last")
            else:
                self.text.tag_add("bold", "sel.first", "sel.last")
            return "break"
        except:
            pass

    def italic(self, *args):
        try:
            italic_font = font.Font(self.text, self.text.cget("font"))  # Cuelga de text y trackea la fuente del texto
            italic_font.configure(slant="italic")  # Servirá para cambiar el weight del texto a bold

            self.text.tag_configure("italic", font = italic_font)  # Nombre y el cambio de fuente corresponde a bold_font
            current_tags = self.text.tag_names("sel.first")  # Tags presentes en el texto

            if "italic" in current_tags:
                self.text.tag_remove("italic", "sel.first", "sel.last")
            else:
                self.text.tag_add("italic", "sel.first", "sel.last")
            return "break"
        except:
            pass

    def underline(self, *args):
        try:
            underline_font = font.Font(self.text, self.text.cget("font"))  # Cuelga de text y trackea la fuente del texto
            underline_font.configure(underline = 1)  # Servirá para cambiar el weight del texto a bold

            self.text.tag_configure("underline", font = underline_font)  # Nombre y el cambio de fuente corresponde a bold_font
            current_tags = self.text.tag_names("sel.first")  # Tags presentes en el texto

            if "underline" in current_tags:
                self.text.tag_remove("underline", "sel.first", "sel.last")
            else:
                self.text.tag_add("underline", "sel.first", "sel.last")
        except:
            pass

    def overstrike(self, *args):
        try:
            overstrike_font = font.Font(self.text, self.text.cget("font"))  # Cuelga de text y trackea la fuente del texto
            overstrike_font.configure(overstrike = 1)  # Servirá para cambiar el weight del texto a bold

            self.text.tag_configure("overstrike", font = overstrike_font)  # Nombre y el cambio de fuente corresponde a bold_font
            current_tags = self.text.tag_names("sel.first")  # Tags presentes en el texto

            if "overstrike" in current_tags:
                self.text.tag_remove("overstrike", "sel.first", "sel.last")
            else:
                self.text.tag_add("overstrike", "sel.first", "sel.last")
        except:
            pass

    def theme(self, *args):
        (triple, hexstr) = askcolor()
        if hexstr:
            self.root.configure(bg = hexstr)

def main(root, text, menubar):
    format = Format(root, text) # Instancia de formato
    formatMenu = Menu(menubar)

    # Create the font of ScrolledText
    font = Font(family = 'Consolas', size = 14)
    text.configure(font = font)

    # Submenus Font + Size
    font_submenu = Menu(formatMenu, tearoff = 0)
    size_submenu = Menu(formatMenu, tearoff = 0)

    families_list = families(root)

    for option in families_list:
        font_submenu.add_command(label = option, command = lambda option = option : font.config(family = option)) # Cambio en la familia de la instancia de Font llamada font, actualiza automáticamente text
    for n in range(1,41):
        size_submenu.add_command(label = str(n), command = lambda n = n : font.config(size = n))

    formatMenu.add_command(label = 'Change Font Color', command = format.font_color, accelerator = 'Ctrl+Shift+F')
    formatMenu.add_command(label = 'Change Background Color', command = format.bg_color, accelerator = 'Ctrl+Shift+B')
    formatMenu.add_cascade(label = 'Font', menu = font_submenu)
    formatMenu.add_cascade(label = 'Size', menu = size_submenu)
    formatMenu.add_command(label='Bold', command = lambda : format.bold(False), accelerator = 'Ctrl+B')
    formatMenu.add_command(label='Italic', command = lambda : format.italic(False), accelerator = 'Ctrl+T')
    formatMenu.add_command(label='Underline', command = format.underline, accelerator = 'Ctrl+Shift+U')
    formatMenu.add_command(label='Understrike', command= format.overstrike, accelerator = 'Ctrl+Shift+K')
    formatMenu.add_separator()
    formatMenu.add_command(label='Theme', command = format.theme, accelerator = 'Ctrl+Shift+T')
    menubar.add_cascade(label = 'Format', menu = formatMenu)
    root.config(menu = menubar)

    # Atajos
    root.bind_all('<Control-F>', format.font_color)
    root.bind_all('<Control-B>', format.bg_color)
    root.bind_all('<Control-b>', format.bold)
    root.bind_all('<Control-t>', format.italic)
    root.bind_all('<Control-U>', format.underline)
    root.bind_all('<Control-K>', format.overstrike)
    root.bind_all('<Control-T>', format.theme)

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

# Change Color Font / Change Bg Color
    # 1 --> module --> from tkinter.colorchooser import askcolor
    # 2 --> askcolor() despliega un menú completo y devuelve (x,y), x = color en RGB, y = color en hexadecimal

# Size / Font
    # 1 --> Guardamos en una variable la "TUPLE" de familias de fuentes que ofrece el módulo tkinter.font
    # 2 --> Creo un menu que cuelga del submenu 'Format' con tearoff = 0, y se le añade un comando por cada opción en el listado de familias
    # o en el caso de los tamaños, un comando por cada valor de 1 a 40 por ejemplo
    # 3 --> command es una función lambda o anónima definida tal cual tras el nombre lambda, x : y donde x es el argumento
    # que se recibe e y es la acción que realiza la función
    # 4 --> Cada opción es cada una de las fuentes, y al pulsar una de ellas se configura font.configure(family = option) con el nombre
    # de la fuente
    # 5 --> Instancia de Font, fuente propia que podemos configurar, asignado la fuente del texto como la recién creada para que se actualice