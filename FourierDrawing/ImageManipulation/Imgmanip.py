from PIL import Image
import requests
from io import BytesIO
import pylab
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
from scipy.spatial import distance
from scipy.interpolate import UnivariateSpline


class Imagemanip:

    def __init__(self, url ):
        """ Create image object  """

        # Import raw image
        self.url = url
        response = requests.get(url)
        self.img_raw = Image.open(BytesIO(response.content))
        
    def show(self):
        """ Show raw image and his informations """

        # Show raw image 
        pylab.imshow(np.asarray(self.img_raw))

        # Show image informations
        print("The image format is : {}".format(self.img_raw.format))
        print("The image size is : {}".format(self.img_raw.size))
        print("The image mode is : {}".format(self.img_raw.mode))

    def single_color(self):
        """ Convert image to single color """  

        #Convert image to single color
        self.img_single_color = self.img_raw.convert('L')

    def convert_binary(self, scale=3, thresh_val=200):   
        """ Convert to binary image with 0 or 255 array values """

        # convert image to nympy array
        self.thresh_val = thresh_val
        image_array = np.array(self.img_single_color)

        # convert to binary image_array using thresh_val to cut
        for i in range(len(image_array)):
            for j in range(len(image_array[0])):
                if image_array[i][j] > thresh_val:
                    image_array[i][j] = 255 #white
                else:
                    image_array[i][j] = 0   #black
        self.image_array = image_array
        image = Image.fromarray(image_array)
        
        # reduce number of non-zero pixels by scaling down the image
        self.img_scale = image.resize(tuple([int(v/scale) for v in image.size]),Image.ANTIALIAS)

    def black_and_white(self):
        """  Convert image to black and white """

        # convert image to black and white
        self.img_blackwhite = self.img_scale.convert(mode='1', dither=2)
        self.pixels = (1 - np.asarray(self.img_blackwhite).astype(int))
        self.pixels_vector = np.reshape(self.pixels, self.pixels.size)

    def show_black_and_white(self):
        """  Show black and white image  """

        # Show black and white image 
        pylab.imshow(np.asarray(self.img_blackwhite))

        # Show black and white image informations
        print("The image format is : {}".format(self.img_blackwhite.format))
        print("The image size is : {}".format(self.img_blackwhite.size))
        print("The image mode is : {}".format(self.img_blackwhite.mode))
        print("Numbre of pixels is: {}".format(self.pixels.sum()))
