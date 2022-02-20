from matplotlib import pyplot
from matplotlib import colors
import numpy as np

def color_range(src, lower, upper):
    dst = src.copy()
    for i in range(len(dst)):
        for j in range(len(dst[i])):
            if not np.all(np.greater(dst[i][j], lower)) and not np.all(np.less(dst[i][j], upper)):
                gray = (0.3*dst[i][j][0])+(0.59*dst[i][j][1])+(0.11*dst[i][j][2])
                dst[i][j] = [gray, gray, gray]
    return dst

def getHSV_HUE(src):
    dst = src.copy()
    dst = colors.rgb_to_hsv(dst)
    dst = dst[..., 0].flatten()
    return dst

lower = np.array([215, 130, -1])
upper = np.array([255, 200, 10])

image = pyplot.imread("sample.jpg")
image_hue = getHSV_HUE(image)
colorrange = color_range(image, lower, upper)
colorrange_hue = getHSV_HUE(colorrange)

window = pyplot.figure()
window.add_subplot(221)
pyplot.imshow(image)
window.add_subplot(222)
pyplot.hist(image_hue, 50)
window.add_subplot(223)
pyplot.imshow(colorrange)
window.add_subplot(224)
pyplot.hist(colorrange_hue, 50)
pyplot.show()
