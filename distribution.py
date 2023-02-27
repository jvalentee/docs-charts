import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0, 6, 0.01)
s = 55 + 14.8*(t - np.square(t)/12)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='Time (years)', ylabel='Supply (%)')

plt.xlim([0, 6])
plt.ylim([0, 100])
plt.show()
fig.savefig("distribution.png")
