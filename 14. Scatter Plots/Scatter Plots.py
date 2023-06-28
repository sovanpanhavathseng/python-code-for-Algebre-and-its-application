import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.random.randint(0, 100, 100)
y = np.random.randint(0, 100, 100)

# Create a scatter plot
plt.scatter(x, y)

# Add a title
plt.title('Scatter Plot')

# Add labels to the axes
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

# Show the plot
plt.show()

// This code will create a scatter plot of the two random variables x and y. The title of the plot will be "Scatter Plot" and the axes will be labeled "X-Axis" and "Y-Axis". The plot will be shown in a new window.

// Here is an explanation of the code:

//     The first line imports the matplotlib.pyplot module and the numpy module. These modules are used to create and show the scatter plot.
//     The second line creates two arrays, x and y, that contain random numbers. The random.randint() function is used to generate the random numbers.
//     The third line creates a scatter plot using the scatter() function. The scatter() function takes two arrays as input, the x-axis values and the y-axis values.
//     The fourth line adds a title to the plot using the title() function.
//     The fifth line adds labels to the axes using the xlabel() and ylabel() functions.
//     The sixth line shows the plot using the show() function.

// To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as scatter_plot.py, you can run it by typing the following command into the command line:
