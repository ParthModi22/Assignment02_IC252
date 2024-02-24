'''How to add styles and use xticks and y ticks i have seen it 
 from website geeks for geeks https://www.geeksforgeeks.org/
'''
import matplotlib.pyplot as plt
import numpy as np
import math

#function to create factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
#function for stirling's formula
def func(n):
    return factorial(n) / (np.sqrt(2 * np.pi * n) * ((n / np.e) ** n))

#ploting the graph
x = np.arange(1,21) 
y = [func(i) for i in x]

plt.plot(x, y, color='red', linestyle='-', marker='.') 
plt.title('Stirling\'s Approximation for Factorial')
plt.xlabel('n')
plt.ylabel('f(n)')
plt.grid(True) 
plt.xticks(np.arange(0, 21, step=1))  
plt.yticks(np.arange(1,1.09,step=0.01))
plt.tight_layout() 
plt.show()


    

    
