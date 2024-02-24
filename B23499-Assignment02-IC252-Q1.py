'''How to add styles and use xticks and y ticks i have seen it 
 from website geeks for geeks https://www.geeksforgeeks.org/
'''
import matplotlib.pyplot as plt
import numpy as np
#function to calculate probability 
def prob(k):
    p = 1
    for i in range(1, k):
        p = p * (365 - i) / 365
    return 1 - p

x = np.arange(2, 101)
y = [prob(i) for i in x] 
#simple plot the graph between number of people and probability
plt.plot(x, y, color='red', linestyle='-', marker='.') 
plt.title('Probability of at Least Two People Sharing a Birthday')
plt.xlabel('Number of People')
plt.ylabel('Probability')
plt.grid(True) 
plt.xticks(np.arange(0, 101, step=10)) 
plt.yticks(np.arange(0, 1.1, step=0.1)) 
plt.tight_layout()  # Adjust layout to prevent cropping of labels
plt.show()



