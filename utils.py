# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018

def fact(n):
    """Computes the factorial of a natural number.
    
    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0
    """
    a=1
    b=1
    if n < 0:
        raise ValueError ("Can't negative")
    elif n==0:
        return 1
    return fact (n-1)*n




def roots(a, b, c):
    """Computes the roots of the ax^2 + bx + x = 0 polynomial.
    
    Pre: -
    Post: Returns a tuple with zero, one or two elements corresponding
          to the roots of the ax^2 + bx + c polynomial.
    """
    delta = (b**2) - (4*a*c)
    try:
	    X1 = (-b + (delta)**(1/2))/(2*a)
	    X2 = (-b - (delta)**(1/2))/(2*a)
    except:
	    return ()
    if X1 == X2:
        return X1
    else:
	    return (X1, X2)

def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """
    def f(x):
        return eval(function)
        
    print(f(4))

if __name__ == '__main__':
    print(fact(5))
    print(roots(1, 0, 1))
    print(integrate('x ** 2 - 1', -1, 1))