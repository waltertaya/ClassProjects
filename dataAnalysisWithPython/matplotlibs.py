from matplotlib import pyplot as plt

x = [2, 4, 6, 8, 10]

y = [6, 7, 8, 2, 4]

plt.plot(x, y)
plt.title('Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()

# x-axis values
x = [5, 2, 9, 4, 7]
# Y-axis values
y = [10, 5, 8, 4, 2]
# Function to plot the bar
plt.bar(x,y)
# function to show the plot
plt.show()

plt.scatter(x, y)
plt.show()