import numpy as np
import matplotlib.pyplot as plt

# Define the function
def function(s, k):
    return k / (s**2 + 4*s - 5)

# Generate values for s
s_values = np.linspace(-10, 10, 400)

# Plot the graph for k before k=5 (let's say k=3)
k_before = 4
plt.plot(s_values, function(s_values, k_before), label=f'k={k_before}', color='blue')

# Plot the graph for k after k=5 (let's say k=7)
k_after = 6
plt.plot(s_values, function(s_values, k_after), label=f'k={k_after}', color='red')

# Mark k=5 on the graph
plt.axhline(y=function(0, 5), color='green', linestyle='--', label='k=5')

# Labeling and styling
plt.title('Graph of $\\frac{k}{s^2 + 4s - 5}$')
plt.xlabel('s')
plt.ylabel('Function Value')
plt.legend()
plt.grid(True)
plt.ylim(-10, 10)  # Adjust ylim for better visualization if needed

# Show plot
plt.show()

