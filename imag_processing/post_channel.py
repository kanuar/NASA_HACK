# %%
import tensorflow_hub as hub
import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np
import cv2

# %%
model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

# %%
def load_image(img_path):
    img = tf.io.read_file(img_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]
    return img

# %%
content_image = load_image('andy.png')
style_image = load_image('..\\mergefinal.png')

# %%
""" content_image.shape """


# %%
""" plt.imshow(np.squeeze(style_image))
plt.show()  """

# %%
stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]
t=np.squeeze(stylized_image)

# %%
plt.imsave("..\\art.png",t)


