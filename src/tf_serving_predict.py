import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

print(tf.__version__)

# Import MNIST Dataset
fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


import json
data = json.dumps({"signature_name": "serving_default", "instances": test_images[0:3].tolist()})
# print('Data: {} ... {}'.format(data[:50], data[len(data)-52:]))


import requests
headers = {"content-type": "application/json"}
json_response = requests.post('http://localhost:8501/v1/models/test_model:predict', data=data, headers=headers)
predictions = json.loads(json_response.text)['predictions']

def show(idx, title):
  plt.figure()
  plt.imshow(test_images[idx].reshape(28,28))
  plt.axis('off')
  plt.title('\n\n{}'.format(title), fontdict={'size': 16})

for i in range(0,3):
  show(i, 'The model thought this was a {} (class {}), and it was actually a {} (class {})'.format(
    class_names[np.argmax(predictions[i])], np.argmax(predictions[i]), class_names[test_labels[i]], test_labels[i]))

plt.show()