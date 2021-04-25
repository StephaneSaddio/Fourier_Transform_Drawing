Fourier Approximation
=====================

In the second part, we create the FourierApprox class that computes the Fourier coefficients from the path 
generated  by the Imagemanip object.

The  fourier coefficients of functin f are defined by : 

.. math::
   c_{n}(f) =  \frac{1}{T} \int_{0}^{T} f(t) \exp^{-2\pi n  i \frac{t}{T} }

The Fourier series of f of order N is then defined by:

 .. math::
   \sum_{n=0}^{N} c_{n}(f) \exp^{-2\pi n i \frac{t}{T} }


Class  Fourier coefficients
---------------------------

.. autoclass:: FourierDrawing.FourierApproximation.Class_fourierApproximation.FourierApprox
   :members:


Note
-----    

When studying Fourier series and Fourier transforms, sometimes a distortion of the signal appears, known as the Gibbs phenomenon. 
This phenomenon is a side effect which occurs near a discontinuity. Gibbs-type phenomenon causes perturbations 
near endpoints of interval.

.. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Fourier_Series.svg/800px-Fourier_Series.svg.png
   :height: 300
   :width: 600
   :scale: 50
   :align: center
   :alt: Gibbs phenomenon

In practice, the difficulties associated with the Gibbs phenomenon can be ameliorated by using a smoother method 
of Fourier series summation. We solve the problem by adjusting intercept to minimize distance between entire function, rather than 
just the intercepts.  

   

