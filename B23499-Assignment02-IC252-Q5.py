''' i have taken reference from a youtube video
channel Numberphile-https://youtu.be/7u6kFlWZOWg?feature=shared
and also taken help from some website to write the code '''

import random
import matplotlib.pyplot as plt

def monty_hall(switch_door, num_trials=10000):
    wins = 0
    result = []
    for i in range(num_trials):
        # Place the prize behind one of the doors
        doors = [0, 0, 0]
        prize = random.randint(0, 2)
        doors[prize] = 1

        choice = random.randint(0, 2)  # Player's choice
        #reveals one of the other doors, which does not have the prize
        doors_to_reveal = [i for i in range(3) if i != choice and doors[i] == 0]
        door_revealed = random.choice(doors_to_reveal)

        # Player switches the choice if enabled
        if switch_door:
            choice = next(i for i in range(3) if i != choice and i != door_revealed)

        # Check if the player wins
        if doors[choice] == 1:
            wins += 1
        result.append(wins/(i+1))
    return result
    # return wins / num_trials

prob = monty_hall(True)
prob_not = monty_hall(False)

plt.plot(prob, label='Switching Doors')
plt.plot(prob_not, label='Not Switching Doors')
plt.title('Probability Distribution of Winning the Monty Hall Problem')
plt.xlabel('Number of Trials')
plt.ylabel('Probability of Winning')
plt.legend()
plt.grid(True)
plt.show()