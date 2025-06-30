import tkinter as tk
import tkinter.messagebox as mb
class MyGUI:
    def __init__(self):
        self.window= tk.Tk()

        # Addition of a menu bar to the window
        self.menubar= tk.Menu(self.window)
        # This menu will be part of the menubar, tearoff removes the dashed line that would appear on top otherwise
        self.filemenu= tk.Menu(self.menubar, tearoff=0)
        # This command closes the window
        self.filemenu.add_command(label="Close", command=exit)
        # This line adds the filemenu to the window
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.root.config(menu= self.menubar)
        self.window.geometry("400x600")
        self.label= tk.Label(self.window, text= "enter your names", font= ('Arial',30))
        self.label.pack(padx= 20, pady=10)
        self.textbox= tk.Text(self.window, height=3, font=('Arial', 30))
        # We add a functionality to accept a combination of keys and pass it to the function shortcut
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=30, pady=10)
        self.check_state = tk.IntVar()
        self.checkbox = tk.Checkbutton(self.window, text="show message", font= ('Arial', 30), variable= self.check_state)
        self.checkbox.pack(padx=30, pady=10)
        self.button1= tk.Button(self.window, text="show message", font=('Arial', 30), command= self.showmessage)
        self.button1.pack(padx=20, pady=10)

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.window.mainloop()



    def shortcut(self, event):
        if event.state==12 and event.keysym=="Return":
            self.showmessage()

    """The on_closing function handles the case when the user closes the window and asks if he 
    wants to proceed, if yes, it closes, otherwise it keeps on"""
    def on_closing(self):
        if mb.askyesno(title= "Quit?", message= "Do you really want to quit"):
            self.window.destroy()
    def showmessage(self):
        if self.check_state.get()==0:
            print(self.textbox.get('1.0', tk.END))
        else:
            mb.showinfo(title="Message", message= self.textbox.get('1.0', tk.END))

MyGUI()