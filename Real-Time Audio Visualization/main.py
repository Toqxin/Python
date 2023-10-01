import pyaudio
import numpy as np
import matplotlib.pyplot as plt

FORMAT = pyaudio.paInt16   
CHANNELS = 1   
RATE = 50000  
CHUNK = 1024   

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
 
plt.figure(figsize=(10, 6))
x = np.arange(0, CHUNK)
line, = plt.plot(x, np.random.rand(CHUNK), color='green', linewidth=3.0)
plt.ylim(-50000, 50000)
plt.title('Real-Time Audio Visualization') 
plt.xlabel('Sample Numbers')
plt.ylabel('Amplitude')
plt.gca().set_facecolor('gray')

yellow_amplitude_threshold = 10000
red_amplitude_threshold = 20000
plt.yticks([-50000,-40000,-30000,-20000,-10000,0, 10000, 20000, 30000, 40000,50000])
 
while True:

    data = stream.read(CHUNK)
    data_int = np.frombuffer(data, dtype=np.int16)
    line.set_ydata(data_int)
    
    amplitude = np.max(np.abs(data_int))

    fileA = open('sound_values.txt','a')
    fileA.write(str(amplitude)+'\n')
    fileA.close()

    if amplitude >= red_amplitude_threshold:
        line.set_color('red')
       
    elif amplitude >= yellow_amplitude_threshold:
        line.set_color('yellow')
      
    else:
        line.set_color('green')
        
    plt.pause(0.001) 

stream.stop_stream()
stream.close()
p.terminate()
plt.close()
