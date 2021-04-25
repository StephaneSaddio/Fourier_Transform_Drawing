****************
Complex circles
****************

In this part we create a third class that compute a Fourier transform objet from the path genereted in
the second class fourierApprox. This class Tracks radii and centers of circles implied by 
Fourier decomposition of given FourierTransform object.


Class circles coefficients
--------------------------

.. autoclass:: FourierDrawing.Circles_radii_center.ComplexCircles.Circles
   :members:


Simple and intuitive principle explanation
------------------------------------------

The image below demonstrates how a simple sum of complex numbers in terms of phases/amplitudes can be nicely visualized as a set of 
concatenated circles in the complex plane. Each red line is a vector representing the a term in the sequence of summands: 

.. math::
   c_{n}(f) \exp^{2\pi i (\frac{n}{T})t }


Adding the summands corresponds to simply concatenating each of these red vectors in complex space:

.. image:: https://d33wubrfki0l68.cloudfront.net/6db965f0678e487d4d04a8882fbc794e472b4e4b/99187/img/phase-amplitude.png
   :height: 300
   :width: 600

Reference :

https://www.myfourierepicycles.com/?fbclid=IwAR08t8gMSmbMT_asfAIrZ1K-io3hq09reEl1J_F_O_kC5l26blfPdo9Tyl8

https://betterexplained.com/articles/an-interactive-guide-to-the-fourier-transform/


