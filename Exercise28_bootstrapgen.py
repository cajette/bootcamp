import numpy as np

def draw_bs_reps(data, func, size=1):
    """Function to draw bootsrap replicates"""
    n = len(data)
    #Initialize array of replicates
    reps = np.empty(n)
    for i in range(n):
        bs_sample = np.random.choice(data, replace=True, size=n)
        reps[i]= func(bs_sample)
    return reps
