from PIL import Image
import requests
from io import BytesIO
import pylab
from copy import deepcopy
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