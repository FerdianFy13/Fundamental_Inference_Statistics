# confidence interval

# 6.1 confidence intervals for the mean (sigma known)
# * estimating population parameters
# in this chapter, we will learn an important technique or statistical inference to use sample statistics to estimate the value of an unknown population paramter
# in this section and the next, we will learn how to use sample statistics to make an estimate of the population parameter u when the population standard deviation sigma is known this section or when sigma is unknown
# to make such an inference, begin by finding a point estimate

# * point estimate
# a point estimate is a single value estimate for a population parameter
# the most unbiased point estimate of the population mean u is the sample mean x bar
# the validity of an estimation method is increased when you use a sample statistics that is unbiased and has low variability
# a sample statistics is unbiased if it does not overestimate or underestimate the populations parameter

#* finding a point estimate
# x = ex / n
# this is called making an interval estimate

# * interval estimate
# an interval estimate is an intervalm or range of values used to estimate a population parameter
# to form an interval estimate use the point estimate as the center of the interval and then add and substract a margin of error
# for instance, if the margin of error is 2.1 then an interval estimate would be given by
# x += 2.1 or 
# x - 2.1 (lef endpoint) < u(point estimate) < x + 2.1 (right endpoint)
# the point estimate and inteval estimate are shown in the figure
# beforing finding a margin of error for an interval estimate, we should first determine how confident we need to be that yout interval estimate contains the population mean x

# * level of confidence
# the level of confidence c is the proabability that the interval estimate contains the populations parameter, assuming that the estimation process is repeated a large number of times
# we know from the central limit theorem that when n >= 30, the sampling distribution of sample means is a normal distribution
# the level of confidence c is the area under the standard normal curve between the critical values, -zc and zc
# critical values are values that seperate sample statistics that are probable from sample statistics that are improbable or unusual
# we can see form the figure shown below that c is the percent of the area under the normal curve between -zc and zc

# * sampling error
# the difference between the point estimate and the actual parameter value is called the sampling error
# when x is estimated the sampling error is the difference x - u
# in most cases of course u is unknown and x varies from sample to sample
# homever you can calculate a maximum value for the erro when you know the level confidence and the sampling distribution

# * margin of error
# given a level of confidence c the margin of error E(sometimes also called the maximum error of estimate or error tolerance) is the greatest possible distance between the point estimate and the value of the parameter it is estimating
# for a population mean u where sigma is known, the margin of error is
# . E = zc.sigmax = zc sigma/akar n (zc is critical values)
# when the conditions are met:
# . the sample is random
# . at least one the following is true: the populations is normally distributed or n >= 30


# * confidence intervales for a populations mean
# using a pointt estimate and a margin of error, you can construct an interval estimate of a population parameter such as u
# this interval estimate is called a confidence interval
# a confidence interval for a population mean u is
# . x - e < u < x + e
# the probability that the confidence interval contains u is c, assuming that the estimation process is repeated a large number of times

# guidelines for costructiong a confidence interval for a population mean, if sigma known
# verify that sigma is known, the sample is random and either the populations is normally distributed or n >= 30
# find the sample statistics x
# . x bar = total x / n
# find the critical value zc that corresponds to the given level of confidence
# find the margin of error e
# . e = zc sigma / sqrt n
# find the left and right endpoints and form the confidence interval
# . left endpoint: x bar - E
# . right endpoint: x bar + E
# . interval: x bar - E < u < x bar + E