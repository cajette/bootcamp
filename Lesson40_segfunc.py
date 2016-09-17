"""
Write a boilerplate function for streamlined image processing.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark') # Gets rid of gridlines

# Load image processing modules
import skimage.io
import skimage.filters
import skimage.measure
import skimage.segmentation

"""
image is original filters
radius is radius used for your gaussian blur;
    must be larger than important parts of image
cmap
"""

"""
to plot more than one graph at a time in the same window in matplotlib.py

fig, ax = plt.subplots(2, 3, figsize=(9.5, 8))
    ax[0,0].imshow(im....., cmap)...
    ax[0, 1]

"""
#def boilerplate(image, radius, cmap=plt.cm.viridis):

#image = 'data/HG105_images/noLac_FITC_0000.tif'

def image_load(image, cmap=plt.cm.viridis):
    """
    Load the images
    save as im
    """

    im = skimage.io.imread(image)
    plt.imshow(im, cmap=cmap)
    plt.title('Original Image')
    return im


#image='im'
def hot_pixel(image, squaresize=3, cmap=plt.cm.viridis):
    """
    remove hot pixels
    save as im_no_hp
    """
    selem = skimage.morphology.square(squaresize)
    im_no_hp = skimage.filters.median(image, selem)
    plt.figure()
    plt.imshow(im_no_hp, cmap=cmap)
    plt.title('Hot Pixels Removed')
    return im_no_hp

#image='im_no_hp'
def gauss(image, radius, cmap=plt.cm.viridis):
    """
    radius=50 for our example e.coli image
    Correct for uneven illumination or gradient using gaussian blur.
    save as im_sub
    """

    # Apply gaussian blur with large radius to image then plot
    #radius must be bigger than what you want to see
    im_blur = skimage.filters.gaussian(image, radius)

    # Convert original image to float, subtract gaus. blur image
    im_float = skimage.img_as_float(image)
    im_sub = im_float - im_blur

    # Show blurred, original, and subtracted images.
    plt.figure()
    plt.imshow(im_blur, cmap=cmap)
    plt.title('Blurred Image')

    plt.figure()
    plt.imshow(im_sub, cmap=cmap)
    plt.title('Gradient corrected Image')

    plt.figure()
    plt.imshow(image, cmap=cmap)
    plt.title('Original Image')
    return im_sub

"""THIS IS NOT WORKING"""
def threshold(image, cmap=plt.cm.Greys_r):
    """
    threshold image using otsu thresholding
    save as seg_im
    """

    # Find otsu threshold then set limit to image
    thresh = skimage.filters.threshold_otsu(image)
    seg = image > thresh
    return seg
    plt.close()
    plt.imshow(seg, cmap=plt.cm.Greys_r)

def plot_seg(image, cmap=plt.cm.Greys_r):
    """
    use seg_im from threshold
    Plot segmentation aka cleaned image.
    """

    plt.close('all')
    plt.imshow(image)

    seg_im, num_obj = skimage.measure.label(seg, return_num=true, background=0)
    plt.close()
    plt.imshow(seg_im, cmap=cmap)
