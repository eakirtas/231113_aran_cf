import matplotlib.pyplot as plt


def visualize(data_dict):
    fig, (ax_scatter, ax_line) = plt.subplots(1, 2)

    ax_scatter.scatter(data_dict['x'], data_dict['f_x'], label='f(x)')
    ax_scatter.scatter(data_dict['x'], data_dict['g_x'], label='g(x)')
    ax_scatter.scatter(data_dict['x'], data_dict['h_x'], label='h(x)')
    ax_scatter.set_title('Scatter plot')
    ax_scatter.set_xlabel('x')
    ax_scatter.set_ylabel('y')
    ax_scatter.grid()
    ax_scatter.legend()

    ax_line.plot(data_dict['x'], data_dict['f_x'], label='f(x)')
    ax_line.plot(data_dict['x'], data_dict['g_x'], label='g(x)')
    ax_line.plot(data_dict['x'], data_dict['h_x'], label='h(x)')
    ax_line.set_title('Line plot')
    ax_line.set_xlabel('x')
    ax_line.set_ylabel('y')
    ax_line.grid()
    ax_line.legend()

    plt.show()
