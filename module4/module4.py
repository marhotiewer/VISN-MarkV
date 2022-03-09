from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

# flatten the images
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

clf = svm.SVC(gamma=0.001, C=100)

data_train, data_test, target_train, target_test = train_test_split(data, digits.target, test_size=0.333, shuffle=True)

# train and predict
clf.fit(data_train, target_train)
predicted = clf.predict(data_test)

#plot out four sample images with prediction and answer
_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, prediction, target in zip(axes, data_test, predicted, target_test):
    ax.set_axis_off()
    image = image.reshape(8, 8)
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    ax.set_title(f"P:{prediction} A:{target}")

#calculate and print accuracy
correct, wrong = 0, 0
for answer, predicted in zip(target_test, predicted):
    if predicted == answer:
        correct += 1
        continue
    wrong += 1

print(f"accuracy: {round(correct / (correct + wrong) * 100, 2)}%")

plt.show()
