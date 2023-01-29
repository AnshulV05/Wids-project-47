import numpy as np
import mat73
import matplotlib.pyplot as plt

data_dict = mat73.loadmat('mnist.mat')

digits = data_dict['digits_train']
labels = data_dict['labels_train']
mean = np.array(np.zeros([28,28,10]))
size = np.array(np.zeros(10))

for id,x in np.ndenumerate(labels):
    mean[:,:,x] += digits[:,:,id[0]]
    size[x] +=1

for a in range(0,10):
    plt.subplot(5,2,a+1)
    plt.imshow(mean[:,:,a])

plt.show()