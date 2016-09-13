import numpy as np

xa_high = np.loadtxt('data/xa_high_food.csv', comment=#)
xa_low = np.loadtxt('data/xa_low_food.csv', comment=#)

def xa_to_diameter(xa):
    """
    Convert an array of cros-sectional areas to
    diameters with commensurate units
    """

    #Compute diameter from area
    # A = pi * d^2 / 4
    diameter = np.sqrt((xa * 4 / np.pi))
