import random
print("Enter 1 is you want to roll the dice or press 0 if you do not want to roll the dice.");
n=int(input())
while(n):
    print(str(random.sample(range(1,7),1)))
    print("Enter 1 if you want to roll the dice again or press 0")
    n=int(input())

    

    
