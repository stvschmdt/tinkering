import urllib
import pandas as pd
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import subprocess

from color_extractor import ImageToColor

npz = np.load('color_names.npz')
imgs = pd.read_csv('site_images.csv')
urls = list(imgs.absolute_image_url)
img_to_color = ImageToColor(npz['samples'], npz['labels'])
for idx,i in enumerate(urls[:10]):
    get_img = urllib.request.urlretrieve(i, 'image.jpg')
    proc = subprocess.call(["./color-extractor", "color_names.npz", "image.jpg"])
    #proc.wait()
    proc1 = subprocess.call(["xdg-open", "image.jpg"])
    #proc.wait()
    #img = Image.open('image.jpg')
    #img = cv2.imread('image.jpg')
    #img.show(command='xdg-open')
    #print('image:', i, 'color:',img_to_color.get(img)[0])
    #plt.imshow(img, 'gray')
    #plt.show()
    #col = img_to_color.get(img)[0]
    #imgs['color'][idx] = col
#imgs.to_csv('site_images_w_color.csv')

