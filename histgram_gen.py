# Python Scrip to plot the histogram
import numpy as np 
import matplotlib.pyplot as plt

file_t = open("count1", "r")
file_s = open("count2", "r")

# data input from files
times, counts = [], []
for line in file_t:
    time = line[0:2]
    if (time[0] == '0'):
         time = time[1]
        
    count = line[line.find(' ')+1:len(line)-1]
    times.append(int(time))
    counts.append(int(count))

times2, counts2 = [], []
for line in file_s:
    time = line[0:2]
    if (time[0] == '0'):
         time = time[1]
        
    count = line[line.find(' ')+1:len(line)-1]
    times2.append(int(time))
    counts2.append(int(count))

# generate histograms
fig, ax = plt.subplots(2)
ax[0].bar(times, counts)
ax[0].set_title("Tweets Count vs Hour")
ax[1].bar(times2, counts2)
ax[1].set_title("Sleep Tweets Count vs Hour")

for a in ax:
    a.set(xlabel='Time of Day', ylabel='Number of Tweets')
fig.tight_layout()
plt.show()