import tkinter as tk

# setting the display window
window= tk.Tk()

# Setting the caption for the window
window.title("My_first_window")

# specifying the size of the window using the geometry attribute
window.geometry("600x600")

# setting a sample label using the label attribute
label= tk.Label(window, text= "welcome bro", font=('arial', 30))
# Adding a padding to the x and y axes
label.pack(padx=30, pady=30)

# Adding a text_box
textbox= tk.Text(window, height=3, font=('arial', 30))
textbox.pack(padx=20, pady= 10)

# Adding a button
button= tk.Button(window, text= "hello again! click me please" , font=('arial', 30))
button.pack(padx=30, pady=15)

# Adding a frame
buttonframe= tk.Frame(window)
# This helps the buttons to stretch to fill the space available
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

# We pass buttonframe not root because buttonframe is already in root
btn1= tk.Button(buttonframe, text="1", font= ('arial', 30))
""" Also here,we don't use the pack, we use grid and pass in the 
    row and column parameters, 0 for both signifies that they are the starting point, first row and first column"""
btn1.grid(row=0, column= 0, sticky= tk.W + tk.E)
# Options for sticky include e, w, n, s, and nsew for full fit
btn2= tk.Button(buttonframe, text="2", font= ('arial', 30))
btn2.grid(row=0, column= 1, sticky= tk.W + tk.E)
btn3= tk.Button(buttonframe, text="3", font= ('arial', 30))
btn3.grid(row=0, column= 2, sticky= tk.W + tk.E)
btn4= tk.Button(buttonframe, text="4", font= ('arial', 30))
btn4.grid(row=1, column= 0, sticky= tk.W + tk.E)
btn5= tk.Button(buttonframe, text="5", font= ('arial', 30))
btn5.grid(row=1, column= 1, sticky= tk.W + tk.E)
btn6= tk.Button(buttonframe, text="6", font= ('arial', 30))
btn6.grid(row=1, column= 2, sticky= tk.W + tk.E)
btn7= tk.Button(buttonframe, text="7", font= ('arial', 30))
btn7.grid(row=2, column= 0, sticky= tk.W + tk.E)
btn8= tk.Button(buttonframe, text="8", font= ('arial', 30))
btn8.grid(row=2, column= 1, sticky= tk.W + tk.E)
btn9= tk.Button(buttonframe, text="9", font= ('arial', 30))
btn9.grid(row=2, column= 2, sticky= tk.W + tk.E)
btn0= tk.Button(buttonframe, text="0", font= ('arial', 30))
btn0.grid(row=3, column= 1, sticky= tk.W + tk.E)

# We can also use place to add a button as well, without respecting the grid, exactly where we want
check_button= tk.Button(window, text= "check")
check_button.place(x=200, y=300, height=100, width=100)

buttonframe.pack(fill='x')
# fill x fills the button container to the whole available space


# running the mainloop for the window
window.mainloop()