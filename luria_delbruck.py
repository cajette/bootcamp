import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Specify parameters
# Number of generations
n_gen = 16

# Chance of having a beneficial mutation
r = 1e-5 #we picked this kind of arbitrarily; just wanted small number for qualitative view

# Total number of cells
n_cells = 2**(n_gen - 1)

# Adaptive immunity: binomial distribution
ai_samples = np.random.binomial(n_cells, r, size=100000)

# Report mean and std
print('AI mean:', np.mean(ai_samples))
print('AI std:', np.std(ai_samples))
print('AI Fano:', np.var(ai_samples) / np.mean(ai_samples)) #fano factor; variance:mean; shoudl be close to 1

# Function to draw out random mutation hypothesis
def draw_random_mutation(n_gen, r):
    """Draw sampole under random mutation hypothesis."""
    # Initialize number of mutations
    n_mut = 0

    for g in range(n_gen):
        #total cells that can get mutations = 2 * (2^(g-1) - nmut); aka 2^g - 2nmut cells that can mutate
        n_mut = 2*n_mut + np.random.binomial(2**g - 2*n_mut, r)

    return n_mut

def sample_random_mutation(n_gen, r, size=1):
    # Initialize samples
    samples = np.empty(size)

    # Draw the samples
    for i in range(size):
        samples[i] = draw_random_mutation(n_gen, r)

    return samples

rm_samples = sample_random_mutation(n_gen, r, size=100000)

# Report mean and std
print ('RM mean:', np.mean(rm_samples))
print('RM std:', np.std(rm_samples))
print('RM Fano:', np.var(rm_samples) / np.mean(rm_samples)) #fano factor; variance:mean; shoudl be close to 1
