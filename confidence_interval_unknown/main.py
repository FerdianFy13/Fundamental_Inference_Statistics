# confidence interval for the mean (sigma unknown)

# * the t-distribution
# in many real life situations, the populations standard deviation sigma is unknown
# so, how can you construct a confidence interval for a population mean when sigma is nott known
# for a random variable that is normally distributed (or approximately normally distributed), you can use a t-distribution

# if the distribution of a random variable x is approxiametly normal, then
# . t = x bar - u / s / sqrt n
# critical values of t are denoted by tc. here are several properties of the t-distribution
# 1. the mean, median, and mode of the t-distribution are equal to 0
# 2. th t-distribution is bell-shaped and symetric about the mean
# 3. the total area under the t-distribution curve is equal to 1
# 4. the tails in the t-distribution are "thicker" than those in the standard normal distribution
# 5. the standatd deviation of the t-distribution varies with the sample size, but it is greater than 1
# 6. tht t-distribution is a family of curves, each determineed by a parameter called the degress of freedom. the degress of freedom (sometimes abbreviated as d.f) are the number of free choices left after a sample statistics such as x bar is calculated. when you use t-distribution to estimate a population mean, the degrees of freedom are equal to one less than the sample size d.f. = n - 1
# 7. as the degrees of freedom increase, the t-distribution approaches the standard normal distribution, as shown in the figure, after 30 d.f., the t-distributbion is close to the standard  normal distribution

# * confidence intervals and t-distributions
# constructiong a confidence interval for u when sigma is not knwon using the t-distribution is similar to constructing a confidence interval for u when sigam is known using the standard normal distribution --both use a point estimate x bar and a margin of error E
# when sigam is not known, the margin of error E is calculated using the sample standard deviation s and the critical value tc
# the formula for E is: E = tc.s/sqrt n
# before using this formula, verify that the sample is ranodm and either the population is normally distributed or n >= 30

# * Guidelines for constructinf a confidence interval for a sigma unknown
# verify that sigma is not known, the sample is random and either the population is normally distributed or n >= 30
# find the sample statistics n, x bar, and s
# . x bar = Equals z / n
# . s = sqrt Equals(x-z)2/n-1
# identify the degrees of freedom the level of confidence c and the critical value tc
# . df = n - 1
# find the margin of error E
# . E = tc.s/sqrt n
# find the left and right endpoint and form the confidence interval
