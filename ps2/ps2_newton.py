# 6.00 Problem Set 2
#
# Successive Approximation
#
# Name: Jane Lee
# Collaborators (Discussion): N/A
# Collaborators (Identical Solution): N/A
# Problem #1
# Time: 1:30
#
# Problem #2
# Time: 0:30
#
# Problem #3
# Time: 0

#Problem #1 
##def evaluate_poly(poly, x):
##    """
##    Computes the polynomial function for a given value x. Returns that value.
##
##    Example:
##    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
##    >>> x = -13
##    >>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
##    180339.9
##
##    poly: tuple of numbers, length > 0
##    x: number
##    returns: float
##    """
##    
##    # polynomials
##        
##    fifth = poly[4] * x**4
##    fourth = poly[3] * x**3
##    third = poly[2] * x**2
##    second = poly[1] * x**1
##    first = poly[0] * x*0
##    total = fifth + fourth + third + second + first
##
##    # short code
##    #return poly[ : ] + (x)**len(poly)
##    
##    return total
##
##print "function = ", evaluate_poly([0.0, 0.0, 5.0, 9.3, 7.0], -13)

# test math
# print "math = ", 7.0*(-13)**4 + 9.3*(-13)**3 + 5.0*(-13)**2


##
##
###Problem #2
##def compute_deriv(poly):
##    """
##    Computes and returns the derivative of a polynomial function. If the
##    derivative is 0, returns (0.0,).
##
##    Example:
##    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
##    >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
##    (0.0, 35.0, 9.0, 4.0)
##
##    poly: tuple of numbers, length > 0
##    returns: tuple of numbers
##    """
##    poly[4] = poly[4] * 4
##    poly[3] = poly[3] * 3
##    poly[2] = poly[2] * 2
##    poly[1] = poly[1] * 1
##    poly[0] = poly[0] * 0
##
##    return poly
##
##print compute_deriv([-13.39, 0.0, 17.5, 3.0, 1.0])
##    

###Problem #3
def compute_root(poly, x_0, epsilon):
    """
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print compute_root(poly, x_0, epsilon)
    (0.80679075379635201, 8.0)

    poly: tuple of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: tuple (float, int)
    """
##    assert len(poly) > 1
##    assert x_0 != 0
##    assert epsilon > 0

    count = 0
    poly = [-13.39, 0.0, 17.5, 3.0, 1.0]

    # while answer > epsilon:
    for i, val in enumerate(poly):
        print i, val
            
