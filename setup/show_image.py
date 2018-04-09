import gzip
import pickle


with gzip.open('/home/killwithme/Desktop/projects/handwriting-recognition-installer/setup/mnist.pkl.gz', 'rb') as f:
    train_set, valid_set, test_set = pickle.load(f)

train_x, train_y = train_set

import matplotlib.cm as cm
import matplotlib.pyplot as plt


plt.imshow(train_x[0].reshape((28, 28)), cmap=cm.Greys_r)
plt.show()