Fourier Approximation
=====================

In the second part, we create the FourierApprox class that computes the Fourier coefficients from the path 
generated  by the Imagemanip class.

Complex numbers can be thought of as vectors as their real and imaginary components give them both magnitude
and direction. Additionally from euler's formula every complex number in polar form lies on some circle centered about 
the origin. For example: 

.. math::
   z = x + iy = r(cos(t) + isin(t)) = r \exp^{it}. 


Now if we increase  (or time) by 1 unit, the new complex number is equivalent to walking around 
a circle by 1 unit. The specific circle in question will have radius , be centred about the origin, have an initial 
phase equal to . If we keep walking around the circle we will eventually end up back where we started. Specifically, 
when  (), we have walked all the way around the circle.

So therefore, since the fourier series expresses a function as a sum of complex sinusoids (these are also functions remember),
and the outputs of these functions are entirely described by circles in the complex plane, means we can represent each complex 
sinusoid by a circle and a revolving vector. Hence, we can represent a function as a sum of revolving circles and vectors.
Connected them tip to toe (i.e. adding them together) to find the final drawing.

The FourierAprox class 
The fourier coefficients of functin f are defined by : 

.. math::
   c_{n}(f) =  \frac{1}{T} \int_{0}^{T} f(t) \exp^{-2\pi n  i \frac{t}{T} }


The Fourier series of f of order N is then defined by:

 .. math::
   \sum_{n=0}^{N} c_{n}(f) \exp^{-2\pi n i \frac{t}{T} }


Class Fourier coefficients
---------------------------

.. autoclass:: FourierDrawing.FourierApproximation.Class_fourierApproximation.FourierApprox
   :members:


Note
----   

When studying Fourier series and Fourier transforms, sometimes a distortion of the signal appears, known as the Gibbs phenomenon. 
This phenomenon is a side effect which occurs near a discontinuity. Gibbs-type phenomenon causes perturbations 
near endpoints of interval. for more details https://en.wikipedia.org/wiki/Gibbs_phenomenon.

.. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Fourier_Series.svg/800px-Fourier_Series.svg.png
   :height: 300
   :width: 600
   :scale: 50
   :align: center
   :alt: Gibbs phenomenon

Spline function doesn't make endpoints exactly equal, so we set the first and last points to their average. In practice, the difficulties associated with the Gibbs phenomenon can be ameliorated by using a smoother method 
of Fourier series summation. We solve the problem by adjusting intercept to minimize distance between entire function, rather than 
just the intercepts.  

   

