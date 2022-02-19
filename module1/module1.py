from matplotlib import pyplot
from matplotlib import colors
import numpy as np

img_rgb = pyplot.imread("sample.jpg")

lower = np.array([215, 130, -1])
upper = np.array([255, 200, 10])

for i in range(len(img_rgb)):
    for j in range(len(img_rgb[i])):
    	if not np.all(np.greater(img_rgb[i][j], lower)) and not np.all(np.less(img_rgb[i][j], upper)):
    		gray = (0.3*img_rgb[i][j][0])+(0.59*img_rgb[i][j][1])+(0.11*img_rgb[i][j][2])
    		img_rgb[i][j] = [gray, gray, gray]

pyplot.imshow(img_rgb)
pyplot.show()
