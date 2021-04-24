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