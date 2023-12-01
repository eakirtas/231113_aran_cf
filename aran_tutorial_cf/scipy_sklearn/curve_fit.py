import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def f(x):
    return x / 2.0 * np.sin(x / 3.0 + np.pi) - 0.5


def g(x):
    return np.tanh((x * np.pi) / 2.0) + np.cos(x)


def h(x):
    return np.cos(np.power(x, 2) / 2.0) * np.pi


def fit_fx():
    x = np.linspace(-5, 5, num=1000)
    f_x = f(x)

    mean, std = 0, 0.5
    noise = std * np.random.randn(1000) + mean

    f_x_noise = f_x + noise

    def objective(x, a, b, c, d, e, f):
        return (a * x) + (b * x**2) + (c * x**3) + (d * x**4) + (e * x**5) + f

    popt, _ = curve_fit(f=objective, xdata=x, ydata=f_x_noise)

    fig, (ax_curve, ax_noise) = plt.subplots(1, 2)

    ax_curve.scatter(x, f_x_noise, label='Data')
    ax_curve.plot(x, f_x, label='f*(x)', color='green', linewidth='4')
    ax_curve.plot(x,
                  objective(x, *popt),
                  label='f*(x)',
                  color='red',
                  linewidth='4')

    ax_noise.hist(noise, label=f'N{mean, std}', bins=100, alpha=0.5)

    plt.show()


fit_fx()


def fit_gx():
    x = np.linspace(-5, 5, num=1000)
    g_x = g(x)

    mean, std = 0, 0.5
    noise = std * np.random.randn(1000) + mean

    g_x_noise = g_x + noise

    def objective(x, a, b, c, d, e, f):
        return (a * x) + (b * x**2) + (c * x**3) + (d * x**4) + (e * x**5) + f

    popt, _ = curve_fit(f=objective, xdata=x, ydata=g_x_noise)

    fig, (ax_curve, ax_noise) = plt.subplots(1, 2)

    ax_curve.scatter(x, g_x_noise, label='Data')
    ax_curve.plot(x, g_x, label='g*(x)', color='green', linewidth='4')
    ax_curve.plot(x,
                  objective(x, *popt),
                  label='g*(x)',
                  color='red',
                  linewidth='4')

    ax_noise.hist(noise, label=f'N{mean, std}', bins=100, alpha=0.5)

    plt.show()


fit_gx()


def fit_hx():
    x = np.linspace(-5, 5, num=1000)
    h_x = h(x)

    mean, std = 0, 0.5
    noise = std * np.random.randn(1000) + mean

    h_x_noise = h_x + noise

    def objective(x, a, b, c, d, e, f):
        return (a * x) + (b * x**2) + (c * x**3) + (d * x**4) + (e * x**5) + f

    popt, _ = curve_fit(f=objective, xdata=x, ydata=h_x_noise)

    fig, (ax_curve, ax_noise) = plt.subplots(1, 2)

    ax_curve.scatter(x, h_x_noise, label='Data')
    ax_curve.plot(x, h_x, label='h*(x)', color='green', linewidth='4')
    ax_curve.plot(x,
                  objective(x, *popt),
                  label='h*(x)',
                  color='red',
                  linewidth='4')

    ax_noise.hist(noise, label=f'N{mean, std}', bins=100, alpha=0.5)

    plt.show()


fit_hx()


def fit_hx_better():
    x = np.linspace(-5, 5, num=1000)
    h_x = h(x)

    mean, std = 0, 0.5
    noise = std * np.random.randn(1000) + mean

    h_x_noise = h_x + noise

    def objective(x, a, b, c, d, e, g, h, i, j, f):
        return (a * x) + (b * x**2) + (c * x**3) + (d * x**4) + (e * x**5) + (
            g * x**6) + (h * x**7) + (i * x**8) + (j * x**9) + f

    popt, _ = curve_fit(f=objective, xdata=x, ydata=h_x_noise)

    fig, (ax_curve, ax_noise) = plt.subplots(1, 2)

    ax_curve.scatter(x, h_x_noise, label='Data')
    ax_curve.plot(x, h_x, label='h*(x)', color='green', linewidth='4')
    ax_curve.plot(x,
                  objective(x, *popt),
                  label='h*(x)',
                  color='red',
                  linewidth='4')

    ax_noise.hist(noise, label=f'N{mean, std}', bins=100, alpha=0.5)

    plt.show()


fit_hx_better()
