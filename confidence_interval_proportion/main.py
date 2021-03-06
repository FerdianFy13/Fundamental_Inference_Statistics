# confidence intervals for populations proportions

# * point estimate for a population proportion
# the probability of success in a single trial of a binomial experiment is p
# this probability is a population proportion
# in this section, we will learn how to estimate a population proportion p using a confidence interval
# as with confidence intervals for x, we will start a a point estimate

# * point estimate for p
# the point estimate for p, the population proporion of successses is given by the proportion of success in a smaple and is denoted by
# . p = x / n
# where x is the number of successes in the sample and n is the sample size
# the point estimate for the populations proportion of failure is q = 1 - p
# the symbols  p^ and q^ are read as p hat and q hat

# * confidence intervals for a populations proportion
# constructing a confidence interval for a populations proportion p is similar to constructing a confidence interval for a populations mean
# we start with a point estimate and calculate a margin of error
# a confidence interval for a population proportion p is:
# . p^ - E < p < p^ + E
# where margin of error for p is:
# . E = zc sqrt p^q^/n
# the probability that the confidence interval contains p is c, assuming that the estimation process is repeated a large number of times.

# * guidelines for constructing a confidence interval for a populations proportion
# identify the sample statistics n and x bar
# find the point estimate p^
# . p^ = x / n
# verify that the sampling distribution p^ can be approximated by a normal distribution
# . np^ >= 5, nq^ >= 5
# find the critical value zc that corresponds to the given level of confidence c
# . we can use SciPy
# find the margin of error E
# find the left and right endpoints and form the confidence interval

# * finding a minimum sample size
# one way to increase the precision of a confidence interval without decreasing the level of confidence is to increase the sample size
# given a c-confidence level and margin of error E, the minimum sample size n needed to estimate the population proporion p is:
# . n = p^q^(zc/E)2
# this formula assumes that we have preliminary estimated of p^ and q^
# if not use p^ = 0.5 and q^ = 0.5