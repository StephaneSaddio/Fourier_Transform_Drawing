import sys
import unittest
sys.path.append('..')
from ImageManipulation.Imgmanip import Imagemanip

url = 'https://www.seekpng.com/png/detail/116-1164659_line-drawing-bunny-rabbit-at-getdrawings-bunny-drawing.png'

class test_Imgmanip(unittest.TestCase):

    def test_img_object (self):
        """ Assert that the image object is created """
        img = Imagemanip(url)
        self.assertIsInstance(img, Imagemanip)