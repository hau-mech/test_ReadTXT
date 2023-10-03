from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize = (8, 6))
plt.rcParams["font.size"] = 12
speed_range = np.arange(0, 26)

plt.plot(stats.weibull_min.pdf(speed_range, *(1.5, 0, 8.15)),
         color = "blue",
        label = "k = 1.5")

plt.plot(stats.weibull_min.pdf(speed_range, *params),
         color = "green",
        label = "k = 2.23")   #shape factor

plt.plot(stats.weibull_min.pdf(speed_range, *(3, 0, 8.15)),
        label = "k = 3",
        color = "red")

plt.xlabel("Speed class (m/s)")
plt.ylabel("Probability density function")
plt.title("Wind speed distribution with different shape parameters")

plt.legend()
