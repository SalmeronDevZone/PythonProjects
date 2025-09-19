import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


x = np.linspace(1,150,200)
y = x + x**2

#print(x)
#print(y)

plt.plot(x,y, 'blue')
plt.title("Mi grafica")
plt.xlabel("Valores x")
plt.ylabel("Valores Y")

plt.show()


#Subplots

plt.subplot(1, 2, 1)
plt.plot(x, y, 'g')
plt.subplot(1, 2, 2)
plt.plot(x, y, 'red')
plt.show()

