import random
import math

def ran():
    num=math.floor(random.random()*10)
    analyse(num)
    
def analyse(num):
    choice =True
    while (choice):
        a=int(input("Enter Number "))
        if(a<num): print("low")                
        if(a>num): print("high")
        if(a==num):
             print(a," is the Correct Number")
             choice = False
        
     
      