import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button


def plot1():
    # Create subplot
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.35)

    # Create and plot sine wave
    t = np.arange(0.0, 1.0, 0.001)
    s = 5 * np.sin(2 * np.pi * 3 * t)
    l, = plt.plot(t, s)

    # Create axes for frequency and amplitude sliders
    axfreq = plt.axes([0.25, 0.15, 0.65, 0.03])
    axamplitude = plt.axes([0.25, 0.1, 0.65, 0.03])

    # Create a slider from 0.0 to 20.0 in axes axfreq
    # with 3 as initial value
    freq = Slider(axfreq, 'Frequency', 0.0, 20.0, 3)

    # Create a slider from 0.0 to 10.0 in axes axfreq
    # with 5 as initial value and valsteps of 1.0
    amplitude = Slider(axamplitude, 'Amplitude', 0.0,
                       10.0, 5, valstep=1.0)

    # Create function to be called when slider value is changed

    def update(val):
        f = freq.val
        a = amplitude.val
        l.set_ydata(a * np.sin(2 * np.pi * f * t))

    # Call update function when slider value is changed
    freq.on_changed(update)
    amplitude.on_changed(update)

    # display graph
    plt.show()

class PhysicsGui(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
        icon = tk.PhotoImage(file='C:\\Users\\EKLAVYA\\Pictures\\GUI\\icon_image.png')
        self.iconphoto(False, icon)

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
        button1 = tk.Button(text="Click to see plot 1", command=plot1)
        button1.place(relx=0.2, rely=0.2)
        SideNavigationBar().place(relx=0, rely=0)
        btn1 = SideButton(text="ABOUT THE PROJECT", command=lambda: master.switch_frame(AboutProject))
        btn1.place(relx=-0.02, rely=0.1)



class AboutProject(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.config(height=PhysicsGui.winfo_screenheight(self), width=PhysicsGui.winfo_screenwidth(self), bg='red')
        TopBar().place(rely=0)
        SideNavigationBar().place(relx=0, rely=0)
        btn1 = SideButton(text="ABOUT THE PROJECT", command=lambda: master.switch_frame(StartPage))
        btn1.place(relx=-0.02, rely=0.1)

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





app = PhysicsGui()
app.mainloop()


