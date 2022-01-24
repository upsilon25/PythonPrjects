import random
import math
def finGer(finger):
      if(finger==0):return "stone"
      if(finger==1):return "paper"
      else:         return "scissors"
         
def stonePaperSci():
    num=math.floor(random.random()*1000)
    if(num < 333):          return "stone"
    if(num>=333 and num<665): return "paper" 
    else :                  return "scissors"      

def compare():
     
     choice=True
     num="-1"
     print("Guess \n0 for Stone\n1 for Paper\n2 for Scissors\n")
     while(choice):
        num=int(input())
        if(num<0 or num>2):
            print("Guess Again ")
            choice=True
        else:
            choice=False 
            
     comp=stonePaperSci()
     finger=finGer(num)
     print("You  :",finger)
     print("Comp :",comp)
     choice=True
      
     if (finger == comp): 
              return "same"  
     if ((finger=="stone" and comp=="scissors") 
             or (finger=="paper" and comp=="stone")
             or (finger=="scissors" and comp=="paper") ):
                  
                   return f"->You Won with {finger} and Computer lost with {comp}"
               
     elif ((comp=="stone" and finger=="scissors") 
             or (comp=="paper" and finger=="stone")
             or (comp=="scissors" and finger=="paper") ):
                   return f"->Computer Won with {comp} and You lost with {finger}"                                    
               
               