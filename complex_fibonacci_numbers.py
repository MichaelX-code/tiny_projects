import numpy as np
import matplotlib.pyplot as plt

golden = (1 + 5 ** 0.5) / 2
numsP = []
numsN = []
for i in np.arange(0, 6, 0.00001):
    i = float(i)
    numsP.append((golden ** i - (-1 / golden) ** i) / 5 ** 0.5)

for i in np.arange(-10, 0, 0.001):
    i = float(i)
    numsN.append((golden ** i - (-1 / golden) ** i) / 5 ** 0.5)

print(numsN)
print(numsP)

# ------------------------------------------------------------------- #

fig, (ax1, ax2) = plt.subplots(2, 1)

plt.suptitle("Complex Fibonacci sequence")
plt.subplot(2, 1, 1)
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.grid(color='gray', linestyle=':')
plt.axis('equal')
plt.plot([x.real for x in numsP], [x.imag for x in numsP])

plt.subplot(2, 1, 2)
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.grid(True, linestyle='-.')
plt.axis('equal')
plt.plot([x.real for x in numsN], [x.imag for x in numsN])
plt.show()
