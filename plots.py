
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
    ax.set_xlim(-10, 10)
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
    x = np.arange(0.0001, 1000.0, 0.01)
    y = (1)/((x)**2)
    ax.plot(x, y, color='red', lw=3)
    plt.title(r'$\frac{kq_1q_2}{r^2}$', fontsize=20)
    plt.axhline(linewidth=2, color='grey')
    plt.axvline(linewidth=2, color='grey')
    plt.ylabel("Displacement", fontsize=12)
    plt.xlabel("Time", fontsize=12)
    plt.grid(axis='both', color='grey')
    ax.set_facecolor("black")
    ax.set_xlim(-2, 10)
    ax.set_ylim(-2, 10)
    fig.set_facecolor("#45ADA8")

    plt.show()

def electrostatics2():
    k = 9 * (10 ** 4)
    def f(g, R):
        if g < R:
            return 0.3
        elif g == R:
            return k/R**2
        else:
            return k/g**2

    fig, ax = plt.subplots()
    x = np.arange(0, 200, 0.01)
    y = []
    for i in range(x.size):
        y.append(f(x[i], 50))
    ax.plot(x, y, color='red', lw=3)
    plt.title("Electric Field for a hollow sphere", fontsize=20)
    plt.axhline(linewidth=2, color='grey')
    plt.axvline(linewidth=2, color='grey')
    plt.ylabel("Electric Field", fontsize=12)
    plt.xlabel("Radius (r)", fontsize=12)
    plt.grid(axis='both', color='grey')
    ax.set_facecolor("black")
    ax.set_xlim(-5, 200)
    ax.set_ylim(-5, 60)
    fig.set_facecolor("#45ADA8")
    plt.annotate('''r=R
    Maximum E''', (50, k/50**2), color='red', textcoords='offset points', xytext=(0, 5), ha='center')
    plt.show()

def electrostatics3():
    k = 9 * (10 ** 2)
    def f(g, R):
        if abs(g) < R:
            return k/R
        elif abs(g) > R:
            return k/abs(g)

    fig, ax = plt.subplots()
    x = np.arange(-200, 200, 0.01)
    y = []
    for i in range(x.size):
        y.append(f(x[i], 50))
    ax.plot(x, y, color='red', lw=3)
    plt.title("Electric Field for a hollow sphere", fontsize=20)
    plt.axhline(linewidth=2, color='grey')
    plt.axvline(linewidth=2, color='grey')
    plt.ylabel("Electric Field", fontsize=12)
    plt.xlabel("Radius (r)", fontsize=12)
    plt.grid(axis='both', color='grey')
    ax.set_facecolor("black")
    ax.set_xlim(-200, 200)
    ax.set_ylim(-5, 60)
    fig.set_facecolor("#45ADA8")
    plt.annotate('''r=R
    Maximum E''', (50, k/50**2), color='red', textcoords='offset points', xytext=(0, 5), ha='center')
    plt.show()

electrostatics3()
