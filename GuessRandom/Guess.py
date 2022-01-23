import random
import math

def ran(a):
    num=math.floor(random.random()*10)
    if(num==a):
        print("a== number ",num,a)
        return True
    else:
        return False 
      