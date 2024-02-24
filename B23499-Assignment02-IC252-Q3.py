'''supppose there are n cards the probability of winning will be 
   1 - (if all the n card doesn't match with numbers) 
   i.e 1- dearrangment of n
   How to add annotate i have seen it 
 from website geeks for geeks https://www.geeksforgeeks.org/
'''
import matplotlib.pyplot as plt
import numpy as np
import math as m

def prob(n):
    sum = 0
    for i in range(n+1):
        sum += (-1)**i/m.factorial(i)
    return 1 - sum

x = np.arange(2, 102)
y = [prob(i) for i in x]

# Finding the index corresponding to the maximum probability
max_prob_index = np.argmax(y)
max_prob_n = x[max_prob_index]

plt.plot(x, y, color='blue', linestyle='-')  
plt.title('Probability of Winning Card Game')
plt.xlabel('Number of Cards')
plt.ylabel('Probability of Winning')
plt.grid(True)  
plt.xticks(np.arange(0, 102, step=10)) 
plt.yticks(np.arange(0.5, 0.7, step=0.02))  
plt.tight_layout()  # Adjust layout to prevent cropping of labels

# Annotating the maximum probability point
plt.annotate(f'Maximum Probability\n(n={max_prob_n})', xy=(max_prob_n, y[max_prob_index]),
             xytext=(max_prob_n + 10, y[max_prob_index] - 0.1),
             arrowprops=dict(facecolor='red', arrowstyle='->'))

plt.show()

print(f"The maximum probability occurs at n = {max_prob_n}")





