from skimage.feature import graycomatrix
import numpy as np
import cv2

# Read in the image
img = cv2.imread('0500.jpg', 0)
gray_levels = 256
distances = [1]
angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]

# Extract RGB features
r = img
g = img
b = img

# First order features
mean = np.mean(img)
median = np.median(img)
max_val = np.max(img)
min_val = np.min(img)
variance = np.var(img)
std_dev = np.std(img)
skewness = cv2.moments(img)['mu03']
kurtosis = cv2.moments(img)['mu02']
entropy = cv2.moments(img)['mu11']

# Second order features
glcm = graycomatrix(img, distances, angles,
                    levels=gray_levels, symmetric=True, normed=True)
glcm_2d = np.reshape(glcm, (gray_levels**2, 1))
contrast = cv2.compareHist(glcm_2d, np.ones(
    (gray_levels**2, 1), dtype=np.float32), cv2.HISTCMP_CHISQR_ALT)
homogeneity = cv2.compareHist(glcm_2d, np.ones(
    (gray_levels**2, 1), dtype=np.float32), cv2.HISTCMP_INTERSECT)
energy = cv2.compareHist(glcm_2d, np.ones(
    (gray_levels**2, 1), dtype=np.float32), cv2.HISTCMP_BHATTACHARYYA)
correlation = cv2.compareHist(glcm_2d, np.ones(
    (gray_levels**2, 1), dtype=np.float32), cv2.HISTCMP_CORREL)

# Print the features
print("RGB Features:")
print("R:", r)
print("G:", g)
print("B:", b)
print("\nFirst Order Features:")
print("Mean:", mean)
print("Median:", median)
print("Max:", max_val)
print("Min:", min_val)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
print("Skewness:", skewness)
print("Kurtosis:", kurtosis)
print("Entropy:", entropy)
print("\nSecond Order Features:")
print("Contrast:", contrast)
print("Homogeneity:", homogeneity)
print("Energy:", energy)
print("Correlation:", correlation)
