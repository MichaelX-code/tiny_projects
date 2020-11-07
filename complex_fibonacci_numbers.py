import matplotlib.pyplot as plt


numsP = []      # list for all numbers >= 0
numsN = []      # list for all numbers <= 0
start = -10
stop = 10
step = 0.001
golden = (1 + 5 ** 0.5) / 2     # golden ratio

# fill lists
i = start
while i <= stop:
    if i >= 0:
        numsP.append((golden ** i - (-1 / golden) ** i) / 5 ** 0.5)
    if i <= 0:
        numsN.append((golden ** i - (-1 / golden) ** i) / 5 ** 0.5)
    i += step

# create a graph using matplotlib
fig, (ax1, ax2) = plt.subplots(2, 1)
plt.suptitle("Complex Fibonacci sequence")

# upper plot for positive numbers
plt.subplot(2, 1, 1)
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.grid(color='gray', linestyle=':')
plt.axis('equal')
plt.plot([x.real for x in numsP], [x.imag for x in numsP])

# lower plot for negative numbers
plt.subplot(2, 1, 2)
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.grid(color='gray', linestyle=':')
plt.axis('equal')
plt.plot([x.real for x in numsN], [x.imag for x in numsN])
plt.show()
