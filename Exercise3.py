
"""
Exercise 3 for bootcamp
"""
# Exercise 3 part a: look at files, etc.
# all comments are #, contain 3 extra lines of comments/headings

# Import all the important packages
import numpy as np
import scipy.stats

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

import seaborn as sns
rc={'lines.linewidth' : 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 18}
sns.set(rc=rc)

# Load data without extraneous beginning info
wt_data = np.loadtxt('data/wt_lac.csv', comments='#',
                     skiprows=3, delimiter=',')
q18a_data = np.loadtxt('data/q18a_lac.csv', comments='#',
                        skiprows=3, delimiter=',')
q18m_data = np.loadtxt('data/q18m_lac.csv', comments='#',
                        skiprows=3, delimiter=',')

# Split up x and y; x = [IPTG], y = exp fold change
wt_data_x = wt_data[:,0]
wt_data_y = wt_data[:,1]
q18a_data_x = q18a_data[:,0]
q18a_data_y = q18a_data[:,1]
q18m_data_x = q18m_data[:,0]
q18m_data_y = q18m_data[:,1]

#R/K for each cell line
wt_rk = 141.5 #mM^-1
q18a_rk = 16.56 #mM^-1
q18m_rk = 1332 #mM^-1

# Calculate the theoretical fold change
def fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """
    Calculates the theoretical fold change with respect to IPGT concentration
    """
    x = c
    y = ((1 + RK*(1 + x/KdA)**2)) /\
        ((1 + x/KdA)**2 + (Kswitch*(1 + c/KdI)**2))**-1

    return y
# Calculate theoretical fold change
wt_theor_y = fold_change(wt_data_x, wt_rk)
q18a_theor_y = fold_change(q18a_data_x, q18a_data_y)
q18m_theor_y = fold_change(q18m_data_x, q18m_data_y)

# Make smoothened IPGT concentrations
#THEOR_X VALUES ARE NOT THE SAME SIZE AS THEOR_Y
wt_theor_x = np.logspace(np.min(wt_data_x), np.max(wt_data_x), len(wt_theor_y))
q18a_theor_x = np.logspace(np.min(q18a_data_x), np.max(q18a_data_x), len(q18a_theor_y))
q18m_theor_x = np.logspace(np.min(q18m_data_x), (np.max(q18m_data_x), len(q18m_theor_y))




# # Plot the [IPGT] vs. experimental fold change of each mutant
# #plt.close()
# plt.semilogx(wt_data_x, wt_data_y, marker='.', linestyle='none',
#          markersize=10)
# plt.semilogx(q18a_data_x, q18a_data_y, marker='.', linestyle='none',
#          markersize=10)
# plt.semilogx(q18m_data_x, q18m_data_y, marker='.', linestyle='none',
#          markersize=10)

# Plot the theoretical fold change vs. regular conc intervals
# print(wt_theor_x)
# print(wt_theor_y)
plt.semilogx(wt_theor_x, wt_theor_y)
plt.semilogx(q18a_theor_x, q18a_theor_y)
plt.semilogx(q18m_theor_x, q18m_theor_y)

plt.show()

# Make the plot pretty misc.
plt.xlabel('[IPGT] (mM$^-1$)')
plt.ylabel('Fold Change')
plt.legend(('WT', 'Q18A Mut', 'Q18M Mut'), loc='upper right')
plt.show()
#x is conc, y is foldchange





# fold change=[1+RK(1+c/KAd)2(1+c/KAd)2+Kswitch(1+c/KId)2]−1
