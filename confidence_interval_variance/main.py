# confidence interval for variance and standard deviation

# * point estimate for variance and standard deviation
# in manufacturing it is necessary to control the amount that a process varies
# for instance an automobile part manufacture must produce thousands of parts to be used in the manufacturing process
# it is important that the parts vary little or not at all
# we can start with a point estimate
# the pointer estimate for sigma2 is s2 and the point estimate for sigma is s

# * the chi-square distribution
# we can use a chi-square distribution to construct a confidence interval for the variance and standard deviation
# if a random variable x has a nonrmal distributionm the then distribution of x2 forms a chi-square distribution for samples of any size n > 1 
# . x2 = (n - 1)s2 / sigma2


# * propoerties of the chi-square distribution
# all values of x2 are greater than or equal to 0
# the chi-square distribution is a family of curves. each determineed by th degrees of freedom. to form a confidence interval for sigma2, use the chi-square distribution with degrees of freedom equal to one less than the sample size
# . df = n - 1
# the total are under each chi-square distribution curve is equal to 1
# the chi-square distribution is positively skewed and therefore the distribution is not symmetric
# the chi-square distribution is different for each number of degrees of freedom as shown in the figure as the degees of freedom increase the chi-square distribution approaches a normal distribution

from scipy.stats import chi2
from math import sqrt

n = 18
df = n-1
c = 0.95

xr2 = (1-c)/2
xl2 = (1+c)/2

print(f'xr2: {xr2}')
print(f'xl2: {xl2}')
print()

xr2_critical = chi2.ppf(1-xr2, df)
xl2_critical = chi2.ppf(1-xl2, df)
print(f'xr2_critical: {xr2_critical}')
print(f'xl2_critical: {xl2_critical}')

# * confidence intervals for sigma2 and sigma
# we can use the critical values xr2 dan xl2 to construct confidence intervals for a populations variance and standard deviation
# the best point estimate for the variance is s2 and the best point estimate for the standard deviation is s
# because the chi-square distribution is not symmetric the confidence interval for sigma2 cnanot be written as s2 +- E
# we must do separate calculations for the endpoints of the confidence interval
# the probability that the confience intervals caontain sigma2 or sigma is c assuming that the estimation process is repeated a large number of times

# * guidelines for constructing a confidence intervals for a variance and standard deviation
# verify that the population has a normal distribution
# identify the sample statistics n and the degrees of freedom
# find the point estimate s2
# find the critical value xr2 and xl2 that correspond to the given level of confidence c and the degrees of freedom
# find the left and right endpoints and form the confidence interval for the populations variance
# find the confidence interval for the populations standard deviation by taking the square root of each endpoint