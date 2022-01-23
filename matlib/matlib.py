def insertGram(job,name,age):
     return f"Daily Life : My {job}, Journal requires Android with an {name} version In addition, the app has a content rating of {age*20}"
 
job= input("Job")
name=input("Name")
age=int(input("Age"))

if __name__ == "__main__":
    print(insertGram(job,name,age))