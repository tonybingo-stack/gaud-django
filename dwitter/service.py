import tensorflow as tf 
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.image as mImage
import cv2 

# import torch
# from tqdm import tqdm
# from torchvision.transforms import Compose, Resize, CenterCrop, ToTensor, Normalize
# import torchvision
# import BigGAN_utils.utils as utils
# import clip
# import torch.nn.functional as F
# from DiffAugment_pytorch import DiffAugment
# import numpy as np
# from fusedream_utils import FuseDreamBaseGenerator, get_G, save_image
# import sys
# import os

def generatefromimage(input, count):
  IMG_WIDTH = 256
  IMG_HEIGHT = 256
  cv2.imwrite("./test.png", cv2.imread(input))
  input_image = tf.io.read_file("test.png")
  input_image = tf.io.decode_jpeg(input_image)
  # Convert both images to float32 tensors
  input_image = tf.cast(input_image, tf.float32)
  input_image = tf.image.resize(input_image, [IMG_HEIGHT, IMG_WIDTH],method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
  input_image = (input_image / 127.5) - 1
  modelo = tf.keras.models.load_model('generator.h5')
  # modelo = tf.keras.models.load_model('https://drive.google.com/file/d/1VKdHyCN6APD-yK1fI8uq1H4oq46iMhAM/view?usp=share_link')
  prediction = modelo(input_image[tf.newaxis, ...], training=True)
  result = (prediction[0, ...] )
  tf.keras.utils.save_img(
    './dwitter/static/result/' + str(count) + '.png', result, data_format=None, file_format=None, scale=True)

# def generatefromtext(text, count):
#     #@title Parameters
#     SENTENCE = text #@param {type:"string"}
#     INIT_ITERS =  1000#@param {type:"number"}
#     OPT_ITERS = 1000#@param {type:"number"}
#     NUM_BASIS = 5#@param {type:"number"}
#     MODEL = "biggan-256" #@param ["biggan-256","biggan-512"]
#     SEED = 0#@param {type:"number"}

#     sys.argv = [''] ### workaround to deal with the argparse in Jupyter

#     ### Generation: Click the 'run' button and the final generated image will be shown after the end of the algorithm
#     utils.seed_rng(SEED) 

#     sentence = SENTENCE

#     print('Generating:', sentence)
#     if MODEL == "biggan-256":
#         G, config = get_G(256) 
#     elif MODEL == "biggan-512":
#         G, config = get_G(512) 
#     else:
#         raise Exception('Model not supported')
#     generator = FuseDreamBaseGenerator(G, config, 10) 
#     z_cllt, y_cllt = generator.generate_basis(sentence, init_iters=INIT_ITERS, num_basis=NUM_BASIS)

#     z_cllt_save = torch.cat(z_cllt).cpu().numpy()
#     y_cllt_save = torch.cat(y_cllt).cpu().numpy()
#     img, z, y = generator.optimize_clip_score(z_cllt, y_cllt, sentence, latent_noise=False, augment=True, opt_iters=OPT_ITERS, optimize_y=True)
#     ### Set latent_noise = True yields slightly higher AugCLIP score, but slightly lower image quality. We set it to False for dogs.
#     score = generator.measureAugCLIP(z, y, sentence, augment=True, num_samples=20)
#     print('AugCLIP score:', score)

#     # if not os.path.exists('./samples'):
#     #     os.mkdir('./samples')
#     save_image(img, './dwitter/static/result/' + str(count) + '.png')

#     # from IPython import display
#     # display.display(display.Image('samples/fusedream_%s_seed_%d_score_%.4f.png'%(sentence, SEED, score)))