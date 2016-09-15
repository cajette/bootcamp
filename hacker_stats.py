"""
using hacker statistics to determine confidence intervals and run
simulations on finch beak data

np.random.choice() is the way to repeat experiment over and over again
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')


bs_sample = np.random.choice(bd_1975, replace=True, size=len(bd_1975))
bs_replicate = np.mean(bs_sample)

# Generate bootstrap for 1975 data
n_reps = 100000
bs_replicates_1975 = np.empty(n_reps)
for i in range(n_reps):
    bs_sample = np.random.choice(bd_1975, replace=True, size=len(bd_1975))
    bs_replicates_1975[i] = np.std(bs_sample)
    """if you want to change what statistic
    you're checking conf int for, just change np.std(bs_sample) code;
    ie np.mean(), etc"""
# Confidence interval
conf_int_1975 = np.percentile(bs_replicates_1975, [2.5, 97.5])

# Generate boostrap for 2012 data
n_reps = 100000
bs_replicates_2012 = np.empty(n_reps)
for i in range(n_reps):
    bs_sample = np.random.choice(bd_2012, replace=True, size=len(bd_2012))
    bs_replicates_2012[i] = np.std(bs_sample)





# Confidence interval of 2012 bootstrap
conf_int_2012 = np.percentile(bs_replicates_2012, [2.5, 97.5])


def ecdf(data):
    return np.sort(data), np.arange(1, len(data)+1) / len(data)

#
# x_1975, y_1975 = ecdf(bd_1975)
# x_2012, y_2012 = ecdf(bd_2012)
# x_1975_bs, y_1975_bs = ecdf(bs_sample)
#
#
# plt.plot(x_1975, y_1975, marker='.', linestyle='none')
# plt.plot(x_1975_bs, y_1975_bs, marker='.', linestyle='none')
# plt.legend(('1975', 'bootstrap'), loc='lower right')
# plt.xlabel('beak depth (mm)')
# plt.ylabel('ECDF')
# plt.show()
