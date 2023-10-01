import numpy as np
import matplotlib.pyplot as plt

fileA = open('sound_values.txt', 'r')
fileA_values = fileA.readlines()
fileA.close()

plt.figure(figsize=(13, 8))
x = np.arange(len(fileA_values)) 
plt.plot(x, [float(value) for value in fileA_values],color='green')
plt.title('Real-Time Audio Visualization') 
plt.xlabel('Sample Numbers')
plt.ylabel('Amplitude')
plt.gca().set_facecolor('gray')
plt.show()