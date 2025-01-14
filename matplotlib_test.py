import matplotlib.pyplot as plt
import numpy as np
import math


x_vals = np.linspace(0, 20, 20)
print (x_vals)
y_vals = [math.sqrt(i) for i in x_vals]
plt.plot(x_vals, y_vals)
print(y_vals)
plt.title("Graf över  NÅGOT")
plt.xlabel("x") 
plt.ylabel("y") 
plt.show()