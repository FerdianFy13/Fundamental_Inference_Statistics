# normal probability distribusi
# dalam normal probability distribution terdapat dua tipe distribution, yaitu

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


def draw_z_score(x, cond, mu=0, sigma=1):
    y = stats.norm.pdf(x, mu, sigma)
    z = x[cond]
    plt.plot(x, y)
    plt.fill_between(z, 0, stats.norm.pdf(z, mu, sigma))
    plt.show()


x = np.arange(-3, 3, 0.001)
draw_z_score(x, x < z_score)

# normal distribution
# a normal distribution is a contrinous probability distribution for a random variable x
# the graph of a normal distribution is called the normal curve
# properties of a normal distribution
# 1. the mean, median, and mode are equal
# 2. the normal curve is bell-shapeed and is about the mean
# 3. the total area under the normal curve is equal to 1
# 4. the normal curve approaches, but never touches, the x-axis as itt extends farther and farther away from the mean
# 5. betwen u - 6 and 8 + 6 in the center of the cuver, the graph curves downwrad
# the graph curves upward to the left of u - 6 and to the right of u + 6
# the points at which the curve changes from curving upward to curving downward are called inflection points

# standard normal distribution
