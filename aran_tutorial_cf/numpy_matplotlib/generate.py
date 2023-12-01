import logging
import os

import numpy as np


def f(x):
    return x / 2.0 * np.sin(x / 3.0 + np.pi) - 0.5


def g(x):
    return np.tanh((x * np.pi) / 2.0) + np.cos(x)


def h(x):
    return np.cos(np.power(x, 2) / 2.0) * np.pi


def generete_data_at(path, num_of_points, list_of_data):

    x = np.linspace(-5, 5, num=num_of_points)

    for data_name in list_of_data:
        if 'x' == data_name:
            np.savetxt(path + 'x.csv', x, delimiter=',')
        elif 'f_x' == data_name:
            f_x = f(x)
            np.savetxt(path + 'f_x.csv', f_x, delimiter=',')
        elif 'h_x' == data_name:
            h_x = h(x)
            np.savetxt(path + 'h_x.csv', h_x, delimiter=',')
        elif 'g_x' == data_name:
            g_x = g(x)
            np.savetxt(path + 'g_x.csv', g_x, delimiter=',')


def load_data(path, list_of_data):
    data_dict = {}

    for data_name in list_of_data:
        data_dict[data_name] = np.loadtxt(path + "/" + data_name + '.csv',
                                          delimiter=',')

    logging.debug(data_dict)

    return data_dict
