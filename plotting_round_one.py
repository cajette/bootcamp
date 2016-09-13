import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Set matplotlib rc params.
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 18}
sns.set(rc=rc)

# Load the food data
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

# Make the bin boundaries.
low_min = np.min(xa_low)
low_max = np.max(xa_high)
high_min = np.min(xa_high)
high_max = np.max(xa_high)
global_min = np.min([low_min, high_min])
global_max = np.max([low_max, high_max])
bins = np.arange(global_min -50, global_max+50, 50) #(minimum bin, max bin, stepsize)

# Plot the data as a histogram
_ = plt.hist(xa_low, normed=True, bins=bins, histtype='stepfilled', alpha=0.5) #underscore works as garbage collector
_ = plt.hist(xa_high, normed=True, bins=bins, histtype='stepfilled', alpha=0.5)
plt.xlabel('Cross-sectional area (µm$^2$)')
plt.ylabel('count')
plt.legend(('low concentration', 'high concentration'), loc='upper right')
#plt.show() note you don't actually have to show a plot to save it; if you close figure,
#will save empty plot; put after save command so that it will open after it saves

# Save the figure
#plt.savefig('egg_area_histograms.svg', bbox_inches='tight')

plt.savefig('egg_pdf_test.pdf', bbox_inches='tight')
plt.show()

"""
# Plot the data as a histogram
_ = plt.hist(xa_low, bins=bins) #underscore works as garbage collector
plt.xlabel('Cross-sectional area (µm$^2$)', fontsize=18)
plt.ylabel('count', fontsize=18, rotation='horizontal')
plt.show()
"""
