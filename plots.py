import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

def plot1():
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.35)

    t = np.arange(-100, 100, 0.001)
    s = 5 * np.sin(2 * np.pi * 3 * t)
    l, = plt.plot(t, s)
    l.set_color('red')
    plt.title(r'$A\sin({2\pi\omega t})$')
    plt.axhline(linewidth=2, color='grey')
    plt.axvline(linewidth=2, color='grey')
    plt.ylabel("Displacement")
    plt.xlabel("Time")
    plt.grid(axis='both', color='grey')
    ax.set_facecolor("black")
    ax.set_xlim(-1, 1)
    ax.set_ylim(-10, 10)
    fig.set_facecolor("#45ADA8")
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
    freq.on_changed(update)
    amplitude.on_changed(update)
    plt.show()


def electrostatics1():
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.35)
    x = np.arange(0.0, 1.0, 0.01)
    y = (9 * 10**9 * 1 * 1)/(x**2)
    p, = plt.plot(x, y)
    plt.show()

def electrostatics2():
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.35)
    x = np.arange()

