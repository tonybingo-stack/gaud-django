import tensorflow as tf 
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.image as mImage
import cv2 
imagen = './static/images/input.png'

def generate_images(input):
  IMG_WIDTH = 256
  IMG_HEIGHT = 256
  cv2.imwrite("./test.png", cv2.imread(input))
  input_image = tf.io.read_file("test.png")
  input_image = tf.io.decode_jpeg(input_image)
  # Convert both images to float32 tensors
  input_image = tf.cast(input_image, tf.float32)
  input_image = tf.image.resize(input_image, [IMG_HEIGHT, IMG_WIDTH],method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
  input_image = (input_image / 127.5) - 1
  # modelo = tf.keras.models.load_model('generator.h5')
  modelo = tf.keras.models.load_model('https://drive.google.com/file/d/1VKdHyCN6APD-yK1fI8uq1H4oq46iMhAM/view?usp=share_link')
  prediction = modelo(input_image[tf.newaxis, ...], training=True)
  result = (prediction[0, ...] )
  tf.keras.utils.save_img(
    './dwitter/static/result.png', result, data_format=None, file_format=None, scale=True)

# generate_images(imagen)

