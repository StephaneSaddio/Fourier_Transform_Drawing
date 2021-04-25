from setuptools import setup
from FourierDrawing import __version__ as current_version

setup(
  name='FourierDrawing',
  version=current_version,
  description='Fourier drawing',
  url='https://github.com/KamalAyoubi/Fourier_Transform_Drawing',
  author='Stephane SADIO, Kamal AYOUBI and Otmane JABBAR',
  author='Stephane SADIO, Kamal AYOUBI and Otmane JABBAR',
  author_email=['stephane.sadio@etu.umontpellier.fr','kamal.ayoubi@etu.umontpellier.fr','otmane.jabbar@etu.umontpellier.fr'],
  license='MIND',
  packages=['FourierDrawing','FourierDrawing.ImageManipulation', 'FourierDrawing.FourierApproximation',
   'FourierDrawing.Circles_radii_center','FourierDrawing.Animate_FT'],
  zip_safe=False
)
