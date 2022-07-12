# normal binomial distribution

# approximating a binomial distribution
# . if np >= 5 and nq >= 5, then the binomial random variabke x is approximately normally distributed, with
# mean: u = np
# standard deviation sigma = akara npq
# nilai q dapat dicari dengan cara => 1 - dengan nilai dari p
# sedangkan untuk nilai p dapat dicari dengan cara => 1 - dengan nilai dari q

# continuty correction
# a binomial distribution is discrete and can be represented by a probability histogram
# remember that each bar has a width of one unit and x is the midpoint of the interval
# when you use a continuous normal distribution to approximate a binomial probability, you need to move 0.5 unit to the left and right of the midpoint to include all possible x-values in the interval
# when you do this, you are making a continuity correction

# approximating binomial probabilities
# verify that a binomial distibution
# . specify n, p, and q
# determine whether you can use a normal distribution to approximate x, the binomial variable
# . is np >= 5 and nq >= 5
# find the mean u and standard deviation sigma for the distribution
# . u = npgit 
# apply the appropriate continuity correction. shade the corresponding area under the normal curve
# . add 0.5 to (or substract 0.5 from) the binomual probabilities
# find the correspoding z-score
# . x = x - u / sigma
# find the probabilities 
# . using the standard normal table, z-score calculator, or scipy