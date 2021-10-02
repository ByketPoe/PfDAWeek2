import matplotlib.pyplot as plt 
import numpy as np

x = np.arange(0.0, 10.0, 0.01)
y = 3.0 * x + 1.0

noise = np.random.normal(0.0, 1.0, len(x))


# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'b.') # b. means blue coloured and dots instead of lines
plt.plot(x, y + noise, 'r.', label = "Noise") 
plt.plot(x, y, 'b-', label = "Signal")

# plt.ylabel("Some numbers")
plt.title("Simple plot")
plt.xlabel("x values")
plt.ylabel("y values")
plt.legend()

plt.show()
