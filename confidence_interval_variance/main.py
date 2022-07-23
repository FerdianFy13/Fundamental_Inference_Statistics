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
