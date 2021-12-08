import matplotlib.pyplot as plt
import numpy as np

plt.subplot(1,2,1)
plt.plot([1,2,3,4],[1,4,9,13],"go")
plt.title("1st")

plt.subplot(1,2,2)
plt.plot([1,2,3,4],[1,4,9,13],"r^")
plt.title("2nd")

plt.suptitle("My subplot")
plt.show()