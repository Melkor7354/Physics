import tkinter as tk
import plots




class PhysicsGui(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
        icon = tk.PhotoImage(file='C:\\Users\\EKLAVYA\\Pictures\\GUI\\icon_image.png')
        self.iconphoto(False, icon)
        self.title("INTERACTIVE PHYSICS")

    def switch_frame(self, page_class):
        new_frame = page_class(self)
        # Destroys original frame
        if self._frame is not None:
            self._frame.destroy()
        # switches to the new frame class
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.config(height=PhysicsGui.winfo_screenheight(self), width=PhysicsGui.winfo_screenwidth(self), bg='red')
        TopBar().place(rely=0)
        button1 = tk.Button(text="Click to see plot 1", command=plots.plot1)
        button1.place(relx=0.2, rely=0.2)
        SideNavigationBar().place(relx=0, rely=0)
        btn1 = SideButton(text="ABOUT THE PROJECT", command=lambda: master.switch_frame(AboutProject))
        btn1.place(relx=-0.02, rely=0.1)
        home = tk.PhotoImage(file="C:\\Users\\EKLAVYA\\Pictures\\GUI\\home_icon-removebg-preview.png")
        homebutton = Home_Button(command=lambda: master.switch_frame(StartPage), image=home)
        homebutton.place(relx=0.5, rely=0.5)



class AboutProject(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.config(height=PhysicsGui.winfo_screenheight(self), width=PhysicsGui.winfo_screenwidth(self), bg='red')
        TopBar().place(rely=0)
        SideNavigationBar().place(relx=0, rely=0)
        btn1 = SideButton(text="ABOUT THE PROJECT", command=lambda: master.switch_frame(StartPage))
        btn1.place(relx=-0.02, rely=0.1)
        home = tk.PhotoImage(file="C:\\Users\\EKLAVYA\\Pictures\\GUI\\home_icon-removebg-preview.png")
        homebutton = Home_Button(command=lambda: master.switch_frame(StartPage), image=home)
        homebutton.place(relx=0.01, rely=0.01)


# Creating a button class that will change text color on hover
class SideButton(tk.Button):
    def __init__(self, text, command):
        tk.Button.__init__(self)
        self.text = text
        self.command = command
        self['text'] = self.text
        self['command'] = self.command
        self.config(bg='black', fg='grey', activebackground='black', activeforeground='white', borderwidth=0, font=('Courier', 16), width=24)
        def hover(e):
            self.config(fg='white')
        def leave(e):
            self.config(fg='grey')
        self.bind('<Enter>', hover)
        self.bind('<Leave>', leave)


class SideNavigationBar(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.config(bg='black', height=PhysicsGui.winfo_screenheight(self), width=300)


class TopBar(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.config(width=PhysicsGui.winfo_screenwidth(self), height=55, bg='black')
        label1 = tk.Label(text='INTERACTIVE PHYSICS', bg='black', fg='red', highlightthickness=0, font=('Courier', 30))
        label1.place(relx=0.5, rely=0.03, anchor='center')
        label2 = tk.Label(
            text=
            '''        Made by: 
            EKLAVYA RAMAN''', bg='black', fg='red', font=('Courier', 15))
        label2.place_configure(x=PhysicsGui.winfo_screenwidth(self)-350, y=0.8)
class Home_Button(tk.Button):
    def __init__(self, command, image, text=None, bg='black', borderwidth=0):
        tk.Button.__init__(self)
        self.command = command
        self.text = text
        self.image = image
        self.bg = bg
        self.borderwidth = borderwidth
        self['command'] = command
        self['image'] = image
        self['text'] = text
        self['bg'] = bg
        self['borderwidth'] = borderwidth




app = PhysicsGui()

app.mainloop()
