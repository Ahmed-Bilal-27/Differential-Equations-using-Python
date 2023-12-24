"""
This code is complementary to my Differential Equations (MTH-242) course
taught at COMSATS University Islamabad, Wah Campus.
This code is developed using the following course:
    Course Name: 'Engineering Math: Differential Equations and Dynamical Systems'
    Course YouTube Playlist Link: https://youtube.com/playlist?list=PLMrJAkhIeNNTYaOnVI3QpH7jgULnAmvPA&si=Baz8274Ma2ce0UTN
"""
#---------------------Imports------------------
import numpy as np
from matplotlib import pyplot as plt
#---------------------Imports------------------
"""
For simplicicty we are considering the following three (03) weather states:
    1- Nice
    2- Rainy
    3- Cloudy
Observation: After running this code with the given values you will notice that
             at Day - 15 and onwards the rainy weather state has converged to 0.4 probability,
             nice weather state has converged to 0.2 probability and cloudy weather state has converged to 0.4 probability.
             All probabilities add to one (01).
"""
# The columns of matrix A represents the probabilities of tomorrow's weather state given that the weather state today is Nice, Cloudy or Rainy.
#              Rainy Nice Cloudy today
A = np.array([[0.5, 0.5, 0.25], # Rainy Tomorrow
              [0.25, 0, 0.25], # Nice Tomorrow
              [0.25, 0.5, 0.5]]) # Cloudy Tomorrow
# State of weather today
#        Rainy Nice Cloudy
xtoday = np.array([1, 0, 0]) # Today the weather state is Rainy
print("Day - 1 Weather State:\n", xtoday) # Printing the weather state probabilities for each day
the_weather = np.zeros((50, 3)) # The weather state for whole 50 days stored in a matrix of 50 days with three (03) weather states each
the_weather[0, :] = xtoday.transpose() # The first row is the weather state of today. It is a column matrix so taking transpose and storing it as a row matrix of the_weather matrix.
for i in range(1, 50): # Loop to predict weather state of 49 days based on today
    xtomorrow = np.dot(A, xtoday)  # xtomorrow is linear combination of xtoday
    xtoday = xtomorrow # For prediction of weather state of any day the weather state of previous day is used. So thats why updating xtoday to predict new xtomorrow
    print(f"Day - {i + 1} Weather State:\n", xtoday) # Printing the weather state probabilities for each day
    the_weather[i, :] = xtoday.transpose() # Adding the weather state of the day to the the_weather matrix. It is a column matrix so taking transpose and storing it as a row matrix of the_weather matrix.
plt.xlabel("Day") # Adding x-axis label
plt.ylabel("Weather State Probability") # Adding y-axis label
plt.plot(the_weather[:, 0], label = "Rainy") # Plotting the Rainy weather state of 50 days
plt.plot(the_weather[:, 1], label = "Nice") # Plotting the Nice weather state of 50 days
plt.plot(the_weather[:, 2], label = "Cloudy") # Plotting the Cloudy weather state of 50 days
plt.legend() # Adding legend
plt.grid(True) # Showing grid
plt.show() # Displaying the plot