from scipy.integrate import cumtrapz
import numpy as np
from scipy.interpolate import interp1d
from scipy.integrate import quad
import matplotlib.pyplot as plt


class custom_distribution:
    '''Pass a pdf function and an xrange'''

    def __init__(self, pdf, x_range):

        self.pdf = pdf
        area = quad(self.pdf, x_range[0], x_range[1])[0]
        self.x_range = x_range
        self.x = np.linspace(self.x_range[0], self.x_range[1], 10000)
        self.pdf_array = np.array([self.pdf(xi) for xi in self.x]) / area
        self.cdf_array = np.array(list(cumtrapz(self.pdf_array, self.x)) + [1])
        self.cdf_array[0] = 0
        self.cdf = interp1d(self.x, self.cdf_array)
        self.inverse_cdf = interp1d(self.cdf_array, self.x)

    def sample(self, n=None):

        random = np.random.random(n)
        return self.inverse_cdf(random)

    def plot_pdf(self, ls=None, title='pdf', plotlabel=None, xlabel=None, ylabel='Probability Density'):

        x = self.x
        y = self.pdf_array
        plt.plot(x, y, color='black', linestyle=ls, label=plotlabel)
        plt.ylim([0, 1.1 * max(y)])
        plt.title(title)
        ax = plt.gca()
        ax.fill_between(x, 0, y, alpha=0.2, color='black')
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
        plt.legend()
        plt.show()

    def plot_cdf(self):

        plt.plot(self.x, self.cdf_array)
        plt.title('cdf')
        plt.show()


def test():

    def my_pdf(x):
        if 0 < x < np.pi / 2:
            return -(24 * x) / (7 * np.pi**2) + 16 / (7 * np.pi)
        if np.pi / 2 <= x < np.pi:
            return 4 / (7 * np.pi)
        else:
            return 0

    dist = distribution(my_pdf, (0, np.pi))

    dist.plot_pdf()
    dist.plot_cdf()
    print(dist.sample(20))
