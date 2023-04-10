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
                       10.0, 5, valstep=0.01)

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


def electrostatics1():
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.35)
    x = np.arange(0.0, 1.0, 0.01)
    y = (9 * 1 * 1)/(x**2)
    p, = plt.plot(x, y)
    axq1 = plt.axes([0.25, 0.15, 0.65, 0.03])
    axq2 = plt.axes([0.25, 0.1, 0.65, 0.03])
    charge1 = Slider(axq1, "q1", 1.0, 20.0, 1.0, valstep=1)
    charge2 = Slider(axq2, "q2", 1.0, 20.0, 1.0, valstep=1)
    def update(val):
        q1 = charge1.val
        q2 = charge2.val
        p.set_ydata((9*q1*q2)/(x**2))

    charge1.on_changed(update)
    charge2.on_changed(update)
    plt.show()