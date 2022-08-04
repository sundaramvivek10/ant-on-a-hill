import random as rnd
from statistics import mean
from numpy import linspace
import matplotlib.pyplot as plt

#Function to randomly select a direction of jump
def randomselection(x, y):
    selection = rnd.choice(["vertical", "horizontal"])
    if selection == "vertical":
        y+=rnd.choice([-1,1])
    else:
        x+=rnd.choice([-1,1])
    return x,y

number_of_runs = int(input("Enter the number of runs to obtain a statistical average: "))
num_of_trials = linspace(1,number_of_runs,number_of_runs)
time = [] #time for 1 run 
average_time = [] #average over all times

for i in range(number_of_runs):
    x,y = 0,0 #starting point of the ant
    number_of_steps = 0
    #Please modify the function in the while loop below to suit your needs   
    while  ((x-0.25)/3)**2 + ((y-0.25)/4)**2 - 1 < 0:
        x,y = randomselection(x, y)
        number_of_steps+=1
    print("No. of steps: %s" %number_of_steps)
    time.append(number_of_steps)
    print("Average time to reach food: %.2f seconds" %mean(time))
    average_time.append(mean(time))

plt.plot(num_of_trials, average_time)
plt.xlabel('Number of runs')
plt.ylabel('Average time')
plt.savefig("time_to_reach_food.eps", format="eps")
plt.show()
