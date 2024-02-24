'''i have seen how to plot the bar graph from website
geeks for geeks-https://www.geeksforgeeks.org/'''

import matplotlib.pyplot as plt
import numpy as np
import random as rd
#part(a) taking sum of rolled dice
def sumofdice():
    a = rd.randint(1,6)
    b = rd.randint(1,6)
    return a+b
#part(b) repeating the process
x = [sumofdice() for i in range(10000)]

#part(c) Printing the tabulated frequency
frequency = [x.count(i) for i in range(2, 13)]
print("Sum\tFrequency")
for i in range(2, 13):
    print(f"{i}\t{frequency[i-2]}")


#part(d) Calculating the probability distribution
trials = 10000
probability = [freq/trials for freq in frequency]

#part(e) 
plt.bar(range(2, 13), probability, color='skyblue')
plt.title('Probability Distribution of Sum of Dice Rolls')
plt.xlabel('Sum of Dice')
plt.ylabel('Probability')
plt.xticks(range(2, 13))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()