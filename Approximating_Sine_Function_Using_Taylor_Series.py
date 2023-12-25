"""
This code is complementary to my Differential Equations (MTH-242) course
taught at COMSATS University Islamabad, Wah Campus.
This code is developed using the following course:
    Course Name: 'Engineering Math: Differential Equations and Dynamical Systems'
    Course YouTube Playlist Link: https://youtube.com/playlist?list=PLMrJAkhIeNNTYaOnVI3QpH7jgULnAmvPA&si=Baz8274Ma2ce0UTN
"""
#---------------------Imports------------------
import numpy as np # URL: https://numpy.org/
from matplotlib import pyplot as plt # URL: https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html
from scipy.integrate import solve_ivp # URL: https://docs.scipy.org/doc/scipy/tutorial/integrate.html
from scipy.special import factorial # URL: https://docs.scipy.org/doc/scipy/reference/special.html
#---------------------Imports------------------
"""
In this code we are approximating sine function using taylor series specifically maclaurin
series. We are only approximating the function upto 5 terms or Ninth-order maclaurin series.
Observation: You will notice that by addition of terms the approximation keeps getting better
             and better and it will be exactly equal to sine (x) if we use n-terms.
"""
# Taking 2000 points in the domain of -10 and 10 inclusive.
x = np.linspace(-10, 10, 2000)
y = np.sin(x) # Corresponding 2000 y-values for each 2000 x-values
plt.plot(x, y, 'k', linewidth=2) # Plotting x and y
plt.xlim(-10, 10) # Limit of x-values is -10 and 10 inclusive
plt.ylim(-10, 10) # Limit of y-values is -10 and 10 inclusive
plt.grid(True) # Keeping the grid
# First-order Taylor expansion
P = [1, 0]  # x + 0 (First-order Taylor series polynomial)
first_order = np.polyval(P, x) # Evaluating the polynomial at x
plt.plot(x, first_order, 'b--', linewidth=1.2)
# Third-order Taylor expansion
P = [-1 / factorial(3), 0, 1, 0]  # -(1/3!)x^3 + x + 0 (Third-order Taylor series polynomial)
third_order = np.polyval(P, x) # Evaluating the polynomial at x
plt.plot(x, third_order, 'r--', linewidth=1.2)
# Fifth-order Taylor expansion
P = [1 / factorial(5), 0, -1 / factorial(3), 0, 1, 0]  # (1/5!)x^5 -(1/3!)x^3 + x + 0 (Fifth-order Taylor series polynomial)
fifth_order = np.polyval(P, x); # Evaluating the polynomial at x
plt.plot(x, fifth_order, 'g--', linewidth=1.2)
# Seventh-order Taylor expansion
P = [-1 / factorial(7), 0, 1 / factorial(5), 
     0, -1 / factorial(3), 0, 1, 0] # -(1/7!)x^7 + (1/5!)x^5 -(1/3!)x^3 + x + 0 (Seventh-order Taylor series polynomial)
seventh_order = np.polyval(P, x); # Evaluating the polynomial at x
plt.plot(x, seventh_order, 'm--', linewidth=1.2)
# Ninth-order Taylor expansion
P = [1 / factorial(9), 0, -1 / factorial(7), 
     0, 1 / factorial(5), 0, -1 / factorial(3), 0, 1, 0] # (1/9!)x^9 - (1/7!)x^7 + (1/5!)x^5 -(1/3!)x^3 + x + 0 (Ninth-order Taylor series polynomial)
ninth_order = np.polyval(P, x); # Evaluating the polynomial at x
plt.plot(x, ninth_order, 'c--', linewidth=1.2)
plt.legend(['sin(x)', '1st order', '3rd order', '5th order', '7th order', '9th order'])
plt.show()