from scipy.ndimage import convolve
from matplotlib import pyplot
from skimage import filters
from skimage import feature

guassian = [[1/16,1/8,1/16],[1/8,1/4,1/8],[1/16,1/8,1/16]]
laplacian = [[0.5,1,0.5],[1,-6,1],[0.5,1,0.5]]

src3d = pyplot.imread("sample.jpg")
src2d = src3d[:,:,0]

window = pyplot.figure()

window.add_subplot(331)
pyplot.imshow(src3d, cmap='gray')

img = convolve(src2d, guassian)
window.add_subplot(332)
pyplot.imshow(img, cmap='gray')

img = convolve(img, laplacian)
window.add_subplot(333)
pyplot.imshow(img, cmap='gray')

img = filters.prewitt(src3d)
window.add_subplot(334)
pyplot.imshow(img, cmap='gray')

img = filters.scharr(src3d)
window.add_subplot(335)
pyplot.imshow(img, cmap='gray')

img = filters.sobel(src3d)
window.add_subplot(336)
pyplot.imshow(img, cmap='gray')

img = feature.canny(src2d)
window.add_subplot(338)
pyplot.imshow(img, cmap='gray')

pyplot.show()
