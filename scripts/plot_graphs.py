import matplotlib.pyplot as plt
import numpy as np


def scatterplot(x_data, y_data, x_label="", y_label="", title="", color="r", yscale_log=False):
    # Create the plot object
    _, ax = plt.subplots()
    # Plot the data, set the size (s), color and transparency (alpha)
    # of the points
    ax.scatter(x_data, y_data, s=10, color=color, alpha=0.75)

    if yscale_log == True:
        ax.set_yscale('log')

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)


def main():
    scatterplot(x_data=range(5), y_data=range(5), x_label='x-axis', y_label='y-axis', title='ScatterPlot')

main()