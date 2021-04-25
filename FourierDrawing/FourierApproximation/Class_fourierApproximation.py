import numpy as np
from copy import deepcopy
from scipy.interpolate import UnivariateSpline 

class FourierApprox:
    """
            This class will calculate the complex Fourier coefficients for a given spline function  

        :type fxn:  scipy.interpolate.UnivariateSpline.
        :param fxn: Spline function (i.e coordinates found by Imagemanip class) to be Converted  to complex numbers with real and imaginary part
        :type rnge: tuple
        :param rnge: the range at which to evaluate fxn.
        :type N: int, default = 500 
        :param N: Number of  Fourier coefficients  that will be  calculate.
        :type period: int, default = None 
        :param period: the period, if the period == None then it's equal to the entire length of the function.
        :type num_points: int, default = 1000
        :param num_points: Number of points at which to evalute function.
        :type num_circles: int, default = 50
        :param num_circles: Number of cercles that will be used for drawing, this is needed to calculate proper offsets

    """

    def __init__(self, fxn, rnge, N=500, period=None,  num_points=1000, num_circles=50 ):

        
        assert isinstance(fxn , UnivariateSpline), f"Parameter 'fxn' should be scipy.interpolate.UnivariateSpline object, but it's of type {type(fxn)}.. Try again!"
        assert isinstance(rnge, tuple) ,f"Parameter 'rnge' should be a tuple, but it's of type {type(rnge)}.. Try again!"
        assert isinstance(N, int), f"Parameter 'N' should be an integer, but it's of type {type(N)}.. Try again!"
        assert isinstance(period,( int ,type(None))) , f"Parameter'period' should be an integer or equal a None , but it's of type {type(period)}.. Try again!"
        assert isinstance(num_points, int), f"Parameter 'num_points' should be an integer, but it's of type {type(num_points)}.. Try again!"
        assert isinstance(num_circles, int), f"Parameter 'num_circles' should be an integer, but it's of type {type(num_circles)}.. Try again!"
        
        self.num_circles = num_circles
        
        t_vals, y = zip(*[(v, fxn(v)) for v in np.linspace(rnge[0], rnge[1]-1, num_points)])
        t_vals = np.array(t_vals)        
        self.t_vals = t_vals
        
        
        # Save the original coords when plotting
        y = np.array(y)
        y = y - y[0]
        self.fxn_vals = np.array(deepcopy(y))
        
        # Spline function doesn't make endpoints exactly equal
        # This sets the first and last points to their average
        endpoint = np.mean([y[0], y[-1]])
        y[0] = endpoint
        y[-1] = endpoint
        
        # Transform works best around edges when function starts at zero
        # (Can't figure out how to avoid Gibbs-type phenomenon when 
        #  intercept !=0 )
        y = y - y[0]
        
        self.N = N
        if period==None:
            period = rnge[1]
        self.period = period
            
        def cn(n):
            c = y*np.exp(-1j*2*n*np.pi*t_vals/period)
            return(c.sum()/c.size)

        coefs = [cn(i) for i in range(1,N+1)]
        self.coefs = coefs
        self.real_coefs = [c.real for c in self.coefs]
        self.imag_coefs = [c.imag for c in self.coefs]
        
        self.amplitudes = np.absolute(self.coefs)
        self.phases = np.angle(self.coefs)
        
        
        def fourier_coefs(x, degree=N):
            """ Evaluate the function y at time t using Fourier approximiation of degree N  """
            # Evaluate the function y at time t using Fourier approximiation of degree N
            fourier_coefs = np.array([2*coefs[i-1]*np.exp(1j*2*i*np.pi*x/period) for i in range(1,degree+1)])
            return(fourier_coefs.sum())
        

        # Evaluate function at all specified points in t domain
        fourier_approximation = np.array([fourier_coefs(t, degree=N).real for t in t_vals])
        circles_approximation = np.array([fourier_coefs(t, degree=self.num_circles).real for t in t_vals])
        
        # Adjust intercept to minimize distance between entire function, 
        # rather than just the intercepts. Gibbs-type phenomenon causes
        # perturbations near endpoints of interval
        fourier_approximation = fourier_approximation - (fourier_approximation - self.fxn_vals).mean()
        
        circles_approximation = circles_approximation - (circles_approximation - self.fxn_vals).mean()
        self.circles_approximation = circles_approximation
        
        # Origin offset
        self.origin_offset = fourier_approximation[0] - self.fxn_vals[0]
        
        # Circles offset
        self.circles_approximation_offset = circles_approximation[0] - self.fxn_vals[0]
        
        # Set intercept to same as original function
        self.fourier_approximation = fourier_approximation

