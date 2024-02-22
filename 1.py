import scipy.stats as stats

dist = stats.norm(loc=0, scale=1)
pdf = dist.pdf(0)
cdf = dist.cdf(1)
rand_values = dist.rvs(size=10)
