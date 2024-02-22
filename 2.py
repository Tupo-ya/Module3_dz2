import scipy.stats as stats

sample = [1,2,3,4,5]
t_stat, p_value = stats.ttest_1samp(sample, popmean=3)

sample1 = [1,2,3,4,5]
sample2 = [6,7,8,9,10]
t_stat, p_value = stats.ttest_ind(sample1, sample2)
