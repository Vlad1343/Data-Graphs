
import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('ggplot')
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, c='red', s=10)
# ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set name for graph and axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set font size for labels on the markup
ax.tick_params(axis='both', which='major', labelsize=14)

# Set range for each axis
ax.axis([0, 1100, 0, 1100000])

plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')