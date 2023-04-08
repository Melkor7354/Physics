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

    def switch_frame(self, page_class):
        new_frame = page_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.config(height=PhysicsGui.winfo_screenheight(self), width=PhysicsGui.winfo_screenwidth(self), bg='red')
        label1 = tk.Label(text=
                          '''PHYSICS GUI
                          THIS IS THE FIRST PAGE''', bg='black', fg='white', width=PhysicsGui.winfo_screenwidth(self))
        label1.place(relx=0.5, rely=0.01, anchor='center')
        button1 = tk.Button(text="Click to see plot 1", command=plot1)
        button1.place(relx=0.2, rely=0.2)
class SecondPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.config(height=PhysicsGui.winfo_screenheight(self), width=PhysicsGui.winfo_screenwidth(self), bg='red')
        label2 = tk.Label(text='''PHYSICS GUI
        THIS IS THE SECOND PAGE''', bg='black', fg='white', width=PhysicsGui.winfo_screenwidth(self))
        label2.place(relx=0.5, rely=0.01, anchor='center')
        button1 = SideButton(text='This is the first button', command=lambda: master.switch_frame(StartPage))
        button1.place(relx=0.5, rely=0.5)
class SideButton(tk.Button):
    def __init__(self, text, command):
        tk.Button.__init__(self)
        self.text = text
        self.command = command
        self['text'] = self.text
        self['command'] = self.command
        self.config(bg='black', fg='grey', activebackground='black', activeforeground='white')
        def hover(e):
            self.config(fg='white')
        def leave(e):
            self.config(fg='grey')
        self.bind('<Enter>', hover)
        self.bind('<Leave>', leave)






app = PhysicsGui()
app.mainloop()


