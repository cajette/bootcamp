import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark') # Gets rid of gridlines

# Load image processing modules
import skimage.io
import skimage.filters
import skimage.measure
import skimage.segmentation


# Load an example phase image.
phase_im = skimage.io.imread('data/HG105_images/noLac_phase_0004.tif')

# Show the original image.
plt.imshow(phase_im, cmap=plt.cm.viridis)
plt.show()

# Apply a gaussian blur with large radius to the image, show image
plt.figure() # This lets you look at multiple plots at same time in dif windows
im_blur = skimage.filters.gaussian(phase_im, 50.0) #radius must be larger than bacteria
plt.title('blurred image')

# # Show the blurred image
# plt.imshow(im_blur, cmap=plt.cm.viridis)

# Convert our phase image to a float
phase_float = skimage.img_as_float(phase_im)
phase_sub = phase_float - im_blur

# Show both.
plt.figure()
plt.imshow(phase_float, cmap=plt.cm.viridis)
plt.title('orignal')

plt.figure()
plt.imshow(phase_sub, cmap=plt.cm.viridis)
plt.title('subtracted')

# Apply otsu thresholding
thresh = skimage.filters.threshold_otsu(phase_sub)
seg = phase_sub < thresh

# Plot our segmentation
plt.close ('all')
plt.imshow(seg, cmap=plt.cm.Greys_r)

# Label 'em
seg_lab, num_cells = skimage.measure.label(seg, return_num=True, background=0)
plt.close()
plt.imshow(seg_lab, cmap=plt.cm.Spectral_r)

# Compute the regionproperties and extract area of each object.
ip_dist = 0.063 #um per pixel
props = skimage.measure.regionprops(seg_lab)

# props[0].area; gives area of single object

# Get the areas as an array.
areas = np.array([prop.area for prop in props])
cutoff = 300

im_cells = np.copy(seg_lab) > 0
#for objects less than your cutoff in your mask copy, change to background
for i, _ in enumerate(areas):
    if areas[i] < cutoff:
        im_cells[seg_lab==props[i].label] = 0

area_filt_lab = skimage.measure.label(im_cells)


plt.figure()
plt.imshow(area_filt_lab, cmap=plt.cm.Spectral_r)
