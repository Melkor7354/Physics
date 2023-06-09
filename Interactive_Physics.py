import tkinter as tk
import plots
import ctypes as ct
import webbrowser
import wolfram_api

font_sidebutton = ('Courier', 16)
font_topbar_name = ('Courier', 30)
font_topbar_credits = ('Courier', 15)
color_topbar = '#2F9599'
color_frame = '#2F9599'
color_sidebutton_hover = '#B4CBD9'
color_main = 'black'


def dark_title_bar(window):
    window.update()
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, 20, ct.byref(value),
                         4)


def open_github():
    webbrowser.open(url='https://github.com/Melkor7354/Physics')


class PhysicsGui(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
        icon = tk.PhotoImage(file='C:\\Users\\EKLAVYA\\Pictures\\GUI\\Icon_new1.png')
        self.iconphoto(False, icon)
        self.title("INTERACTIVE PHYSICS")
        dark_title_bar(self)
        self.minsize(self.winfo_screenwidth(), self.winfo_screenheight())
        self.maxsize(self.winfo_screenwidth(), self.winfo_screenheight())
        self.attributes('-fullscreen', False)
        self.bind("<F11>", self.toggle_full_screen)
        self.FullScreen = True

    def toggle_full_screen(self, event):
        self.FullScreen = not self.FullScreen
        self.attributes('-fullscreen', self.FullScreen)
        dark_title_bar(self)

    def switch_frame(self, page_class):
        new_frame = page_class(self)
        # Destroys original frame
        if self._frame is not None:
            self._frame.destroy()
        # switches to the new frame class
        self._frame = new_frame
        self._frame.pack()


class BasicPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.config(height=PhysicsGui.winfo_screenheight(self), width=PhysicsGui.winfo_screenwidth(self), bg=color_topbar)
        TopBar().place(rely=0)
        SideNavigationBar().place(relx=0, rely=0)
        btn1 = SideButton(text="ABOUT THE PROJECT", command=lambda: master.switch_frame(WolframApi))
        btn1.place(relx=-0.015, rely=0.15)
        btn3 = SideButton(text="WOLFRAM ALPHA", command=lambda: master.switch_frame(WolframApi))
        btn3.place(relx=-0.031, rely=0.24)
        home = tk.PhotoImage(file="C:\\Users\\EKLAVYA\\Pictures\\GUI\\home_icon-removebg-preview.png")
        homebutton = HomeButton(command=lambda: master.switch_frame(StartPage), image=home)
        homebutton.place(relx=0.01, rely=0.08)
        icon = tk.PhotoImage(file="C:\\Users\\EKLAVYA\\Pictures\\GUI\\Icon_new1.png")
        icon_img = HomeButton(image=icon)
        icon_img.place(relx=0.01, rely=0)
        btn2 = SideButton(text="GITHUB REPOSITORY", command=open_github)
        btn2.place(relx=-0.015, rely=0.195)





class StartPage(BasicPage):
    def __init__(self, master):
        BasicPage.__init__(self, master)
        chap1 = ChapterName(text='Chapter 1 - Electrostatics', command=lambda: master.switch_frame(ChapterOne))
        chap1.pack()



class WolframApi(BasicPage):
    def __init__(self, master):
        BasicPage.__init__(self, master)
        def query_perform():
            entry = enter.get()
            try:
                output = wolfram_api.query(entry)
                answer.config(text=output)
            except:
                answer.config(text="Query was unable to be performed.")
        enter = EntryField()
        enter.place(relx=0.3, rely=0.3)
        submit = ChapterName(command=query_perform, text="Submit")
        submit.place(relx=0.3, rely=0.4)
        answer = tk.Label()
        answer.place(relx=0.3, rely=0.5)
        answer.config(width=50, height=10, font=font_sidebutton, bg='black', fg='white', justify="left", anchor="w", wraplength=675)
        tk.Label(text="Enter query here", fg='white', bg=color_topbar, width=50, font=font_sidebutton, anchor='w').place(relx=0.3, rely=0.25)


# Creating a button class that will change text color on hover
class SideButton(tk.Button):
    def __init__(self, text, command, image=None, compound=None):
        tk.Button.__init__(self)
        self.text = text
        self.command = command
        self.image = image
        self.compound = compound
        self['text'] = self.text
        self['command'] = self.command
        self['image'] = self.image
        self['compound'] = self.compound
        self.config(bg=color_main, fg=color_sidebutton_hover, activebackground=color_main, activeforeground=color_frame, borderwidth=0, font=font_sidebutton, width=24)

        def hover(e):
            self.config(fg=color_frame)

        def leave(e):
            self.config(fg=color_sidebutton_hover)
        self.bind('<Enter>', hover)
        self.bind('<Leave>', leave)


class SideNavigationBar(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.config(bg=color_main, height=PhysicsGui.winfo_screenheight(self), width=300)


class TopBar(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.config(width=PhysicsGui.winfo_screenwidth(self), height=55, bg=color_main)
        label1 = tk.Label(text='INTERACTIVE PHYSICS', bg=color_main, fg=color_topbar, highlightthickness=0, font=font_topbar_name)
        label1.place(relx=0.5, rely=0.03, anchor='center')
        label2 = tk.Label(
            text=
            '''        Made by: 
            EKLAVYA RAMAN''', bg=color_main, fg=color_frame, font=font_topbar_credits)
        label2.place_configure(x=PhysicsGui.winfo_screenwidth(self)-350, y=0.8)


class HomeButton(tk.Button):
    def __init__(self, command=None, image=None, text=None, bg=color_main, borderwidth=0):
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


class ChapterName(tk.Button):
    def __init__(self, text, command):
        tk.Button.__init__(self)
        self.text = text
        self.command = command
        self['text'] = self.text
        self['command'] = self.command
        self.config(bg="black", font=("Courier", 16), fg=color_topbar, activeforeground=color_frame, activebackground=color_main)

        def hover(e):
            self.config(fg=color_frame)

        def leave(e):
            self.config(fg=color_topbar)
        self.bind('<Enter>', hover)
        self.bind('<Leave>', leave)


class ChapterOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.config(height=PhysicsGui.winfo_screenheight(self), width=PhysicsGui.winfo_screenwidth(self), bg=color_topbar)
        TopBar().place(rely=0)
        button1 = tk.Button(text="Click to see plot 1", command=plots.electrostatics1)
        button1.place(relx=0.2, rely=0.2)
        SideNavigationBar().place(relx=0, rely=0)
        btn1 = SideButton(text="ABOUT THE PROJECT", command=lambda: master.switch_frame(WolframApi))
        btn1.place(relx=-0.015, rely=0.15)
        home = tk.PhotoImage(file="C:\\Users\\EKLAVYA\\Pictures\\GUI\\home_icon-removebg-preview.png")
        homebutton = HomeButton(command=lambda: master.switch_frame(BasicPage), image=home)
        homebutton.place(relx=0.01, rely=0.08)
        icon = tk.PhotoImage(file="C:\\Users\\EKLAVYA\\Pictures\\GUI\\Icon_new1.png")
        icon_img = HomeButton(image=icon)
        icon_img.place(relx=0.01, rely=0)
        btn2 = SideButton(text="GITHUB REPOSITORY", command=open_github)
        btn2.place(relx=-0.015, rely=0.195)
        labl1 = tk.Label(text='Electrostatics')
        labl1.place(relx=0.5, rely=0.5)


class TextAbout(tk.Text):
    def __init__(self, text):
        tk.Text.__init__(self)
        self.text = text
        self['text'] = self.text
        self.config(bg=color_frame)


class EntryField(tk.Entry):
    def __init__(self, fg='white', bg='black', font=font_sidebutton):
        tk.Entry.__init__(self)
        self.fg = fg
        self.bg = bg
        self.font = font
        self['fg'] = self.fg
        self['bg'] = self.bg
        self['font'] = self.font
        self.config(width=50, insertbackground='white', selectbackground="cyan", selectforeground='black')



class Submit(tk.Button):
    def __init__(self, command, text):
        tk.Button.__init__(self)
        self.command = command
        self.text = text
        self['command'] = self.command
        self['text'] = self.text
        self.config(fg='white', bg='black', width=100)
    def query(self, entry):
        a = wolfram_api.query(entry)



app = PhysicsGui()

app.mainloop()


