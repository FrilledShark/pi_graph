from random import random
import matplotlib.pyplot as plt
import numpy as np
from time import time
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'frames')

#
# Create the graphics
#
fig, ax = plt.subplots()
x = np.linspace(0, 1)
y = np.sqrt(-x**2 + 1)
ax.plot(x, y)
ax.axis([0, 1, 0, 1])
ax.axis('off')
ax.axis('equal')
#
# Calculate
#

# Deleting old files
for the_file in os.listdir(filename):
    file_path = os.path.join(filename, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)

inside = 0
outside = 0
takenlist = []
try:
    for frame in range(100000):
        start = time()
        for i in range(100):
            x = random()
            y = random()
            if x * x + y * y < 1:
                inside += 1
                ax.plot(x, y, 'ro', markersize=1)
            else:
                outside += 1
                ax.plot(x, y, 'go', markersize=1)
        pi = 4 * inside / (inside + outside)
        ax.set_title("π = 4*{inside}/{total} = {pi:.10f}".format(
            pi=pi, inside=inside, total=inside + outside))
        fig.savefig('frames/frame{frame}.png'.format(frame=frame))
        taken = time() - start
        takenlist.append(taken)
        print("Frame {0} took {1} seconds".format(frame, taken))
finally:
    print(takenlist)
