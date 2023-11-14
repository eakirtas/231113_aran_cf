import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x / 2.0 * np.sin(x / 3.0 + np.pi) - 0.5


def g(x):
    return np.tanh((x * np.pi) / 2.0) + np.cos(x)


def h(x):
    return np.cos(np.power(x, 2) / 2.0) * np.pi


means = [0, 0, 1, 2, -1]
stds = [1, 0.5, 1, 2, 1]

fig, axes = plt.subplots(2, 5)

for i in range(len(means)):
    noise = stds[i] * np.random.randn(5000) + means[i]
    axes[0][i].plot(np.arange(0, len(noise)), noise)
    axes[0][i].set_title(f'Line Plot N{means[i], stds[i]}')

    axes[1][i].hist(noise, bins=100, label=f'N({means[i], stds[i]})')
    axes[1][i].set_title(f'Histogram N{means[i], stds[i]}')
plt.show()

fig, ax = plt.subplots(1, 1)
for i in range(len(means)):
    noise = stds[i] * np.random.randn(1000) + means[i]
    ax.hist(noise, label=f'N{means[i], stds[i]}', bins=100, alpha=0.5)
ax.legend()
plt.show()

fig, axes = plt.subplots(3, 2)
for i in range(3):
    x = np.linspace(-5, 5, num=1000)
    noise = stds[i] * np.random.randn(1000) + means[i]
    axes[i][0].scatter(x, g(x) + noise, label='f(x)')
    axes[i][0].plot(x, g(x), label='f(x)', color='red')
    axes[i][1].hist(noise, label=f'N{means[i], stds[i]}', bins=100, alpha=0.5)

ax.legend()
plt.show()

functions = [f, g, h]
fig, axes = plt.subplots(3, 2)
for i in range(3):
    x = np.linspace(-5, 5, num=1000)
    noise = stds[i] * np.random.randn(1000) + means[i]
    axes[i][0].scatter(x,
                       functions[i](x) + noise,
                       label=f'{functions[i].__name__}(x)')
    axes[i][0].plot(x,
                    functions[i](x),
                    label=f'{functions[i].__name__}(x)',
                    color='red')
    axes[i][1].hist(noise, label=f'N{means[i], stds[i]}', bins=100, alpha=0.5)

ax.legend()
plt.show()

## https://numpy.org/doc/1.16/reference/routines.random.html#distributions

dist_generators = {
    'triangular':
    lambda: np.random.triangular(left=-3, mode=0, right=8, size=1000),
    'binomial': lambda: np.random.binomial(n=10, p=0.5, size=1000),
    'chisquere': lambda: np.random.chisquare(df=2, size=1000),
    'poisson': lambda: np.random.poisson(lam=1, size=1000),
    'exponential': lambda: np.random.exponential(scale=1.0, size=1000),
    'laplace': lambda: np.random.laplace(loc=0, scale=1, size=1000)
}

fig, axes = plt.subplots(6, 2)
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

ax.legend()
plt.show()
