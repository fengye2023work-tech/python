import imageio.v3 as iio

filenames = ['Goo1.jpg', 'Goo2.jpg']
images = []
for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite("Goob.gif", images, duration = 500, loop = 0)
