# eText-Editor
This is a text editor to work with .txt files and edit them

* TECHNOLOGIES USED IN THIS PROJECT:
      This application uses a GUI built in Python mainly with tkinter, making use of its widgets and tools such as colorchooser    
      (colorchooser.askcolor ()), messagebox (messagebox.askyesorno (), messagebox.showerror (), messagebox.showinfo ( )), font (font.Font ()), 
      filedialog (filedialog.akopenfilename () or filedialog.asksaveasfilename ()), widgets: ScrolledText, Menu's ...
      It is based on a simple window, from which there is a Menu and a ScrolledText. As for the Menu (Includes "File", "Edit", "Format", 
      "Help"), each submenu is in turn a menu that descends from the main one, and that contains options such as "Open", "Save", " Save As "... 
      in the case of" File ".
      
 In addition, most of the utilities are accessible by clicking on the options (command activates the corresponding functions) or by
 keyboard with shortcuts of all kinds. 
      
 At a conceptual level, the editor elements are thought of as classes, "File", "Edit", "Format" and "Help" are classes whose instances act 
 as methods (Submenus options) and have attributes (Elements such as ScrolledText, which the instances of the classes require to make 
 changes to the text box) 
      
  Finally, it is worth noting the combined use of filedialog and messagebox, which, through methods such as messagebox.askyesorno (), 
  messagebox.showerror (), messagebox.showinfo (), allow us to capture errors that occur when the user initiates the by action example 
  "Open", but finally it does not finish it, and thus indicate when the processes have finished successfully or not. For his part, the user 
  indicates the paths to save or open files with the file explorer thanks to filedialog.akopenfilename () or filedialog.asksaveasfilename ()

* INSTRUCTIONS:
      To use eText it is necessary to have Python installed on your device, it is as simple as grouping and downloading all the files, executing       in this case main.py.

**/ * DISCLAIMER * /
This application is in trial version, some of the errors it has is that some formatting options such as "bold" or "italic" are not saved in the files when using "Save As" or "Save", in addition, you cannot put the text in "bold" and at the same time change the "size" of the text (I think it has to do with the use of tags). Finally, I have tried to create a single .exe with the whole app to make it easier to run and reach more people, using pyinstaller and auto-py-to-exe, but my device does not allow it and identifies my app as a virus.

**If you have any advice or know solutions to these problems, do not hesitate to contact me, it is of great help since I am starting. Thank you.
/ * END * /****

FILE: (Submenus can be detached or booted)
      New: Create a new unnamed file from scratch (Ctrl + N)
      Open: Open the file explorer and select the file to be loaded in the text box (Ctrl + Shift + O)
      Save: Overwrite a file already saved previously, if it is used when it has not yet been saved, it will redirect to Save As (Ctrl + S)
      Save As: Open the file explorer, choose the location and the name with which the file will be saved (Ctrl + Shift + S)
      Quit: Cut the application execution (Ctrl + Q)
  
EDIT:
      Undo (Ctrl + U), Redo (Ctrl + R): Undo the last action performed or redo it
      Cut (Ctrl + Shift + C), Copy (Ctrl + P), Paste (Ctrl + X): Cut and Copy require selected text, Paste places saved text where sel.first is       placed
      Select All (Ctrl + A): Underline all the text entered in the text.tag_add box (SEL, "1.0", END)
 
FORMAT:
      Change Font Color, Change Background Color, Theme (Ctrl + Shift + T): Makes use of colorchooser.askcolor () and applies the selected color       to the font, text box background or application.
      Font, Size, Bold (Ctrl + B), Italic (Ctrl + T), Underline (Ctrl + Shift + U), Understrike (Ctrl + Shift + K): Text customization        
      possibilities.
