import matplotlib.pyplot as plt
import numpy as np

MEANS = [0, 0, 1, 2, -1]
STDS = [1, 0.5, 1, 2, 1]


def f(x):
    return x / 2.0 * np.sin(x / 3.0 + np.pi) - 0.5


def g(x):
    return np.tanh((x * np.pi) / 2.0) + np.cos(x)


def h(x):
    return np.cos(np.power(x, 2) / 2.0) * np.pi


def gaussian_noise_ex_1():
    fig, axes = plt.subplots(2, 5)

    for i in range(len(MEANS)):
        noise = STDS[i] * np.random.randn(5000) + MEANS[i]
        axes[0][i].plot(np.arange(0, len(noise)), noise)
        axes[0][i].set_title(f'Line Plot N{MEANS[i], STDS[i]}')
        axes[0][i].set_xlabel('X')
        axes[0][i].set_ylabel('Y')

        axes[1][i].hist(noise, bins=100, label=f'N({MEANS[i], STDS[i]})')
        axes[1][i].set_title(f'Histogram N{MEANS[i], STDS[i]}')
        axes[0][i].set_xlabel('Values')
        axes[0][i].set_ylabel('Counts')

    plt.show()


def gaussian_noise_ex_2():
    fig, ax = plt.subplots(1, 1)
    for i in range(len(MEANS)):
        noise = STDS[i] * np.random.randn(1000) + MEANS[i]
        ax.hist(noise, label=f'N{MEANS[i], STDS[i]}', bins=100, alpha=0.5)

    ax.legend()
    plt.show()


def generate_noisy_data(path='./data/', num_of_points=1000, mean=0, std=1):
    functions = {
        'f_x': f,
        'g_x': g,
        'h_x': h,
    }

    x = np.linspace(-5, 5, num=num_of_points)
    np.savetxt(path + 'x.csv', x, delimiter=',')

    for name, func in functions.items():
        noise = std * np.random.randn(1000) + mean
        np.savetxt(path + name + '_noisy.csv', func(x), delimiter=',')

    fig, axes = plt.subplots(3, 2)
    for i in range(3):
        noise = STDS[i] * np.random.randn(1000) + MEANS[i]
        axes[i][0].scatter(x, g(x) + noise, label='f(x)')
        axes[i][0].plot(x, g(x), label='f(x)', color='red')
        axes[i][1].hist(noise,
                        label=f'N{MEANS[i], STDS[i]}',
                        bins=100,
                        alpha=0.5)

    plt.show()


def functions_with_noise():
    functions = [f, g, h]

    fig, axes = plt.subplots(3, 2)
    for i in range(3):
        x = np.linspace(-5, 5, num=1000)
        noise = STDS[i] * np.random.randn(1000) + MEANS[i]
        axes[i][0].scatter(x,
                           functions[i](x) + noise,
                           label=f'{functions[i].__name__}(x)')
        axes[i][0].plot(x,
                        functions[i](x),
                        label=f'{functions[i].__name__}(x)',
                        color='red')
        axes[i][1].hist(noise,
                        label=f'N{MEANS[i], STDS[i]}',
                        bins=100,
                        alpha=0.5)

    plt.show()


## https://numpy.org/doc/1.16/reference/routines.random.html#distributions
def distributions():
    dist_generators = {
        'triangular':
        lambda: np.random.triangular(left=-3, mode=0, right=8, size=1000),
        'binomial':
        lambda: np.random.binomial(n=10, p=0.5, size=1000),
        'chisquere':
        lambda: np.random.chisquare(df=2, size=1000),
        'poisson':
        lambda: np.random.poisson(lam=1, size=1000),
        'exponential':
        lambda: np.random.exponential(scale=1.0, size=1000),
        'laplace':
        lambda: np.random.laplace(loc=0, scale=1, size=1000)
    }

    fig, axes = plt.subplots(6, 2)
    functions = [f, g, h]

    for i, (name, func) in enumerate(dist_generators.items()):

        x = np.linspace(-5, 5, num=1000)
        noise = func()

        axes[i][0].scatter(x,
                           functions[i % 3](x) + noise,
                           label=f'{functions[i% 3].__name__}(x)')

        axes[i][0].plot(x,
                        functions[i % 3](x),
                        label=f'{functions[i% 3].__name__}(x)',
                        color='red')
        axes[i][0].grid()

        axes[i][1].hist(noise, bins=100, alpha=0.5)

    plt.show()
