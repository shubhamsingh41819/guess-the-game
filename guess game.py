class C2dvec:
    def __init__(self, i , j):
        self.icap = i
        self.jcap = j
    
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"



'''class C3dvec(C2dvec):
    def __init__(self , i , j , k):
        super().__init__(i , j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}K"

v2d = C2dvec(1,3)
v3d = C3dvec(8,3,5)
print(v2d)  
print(v3d)'''
    
    
'''class Animals:

    A1 = "horse"
    A2 = "dogs"
    A3 = "armadillo"

class pets(Animals):
    A4 = "RAT"
    A5 = "snake"
    A6 = "deer"

class dogs(pets):
    @staticmethod
    def bark():
        print("bow","bow")

ani = Animals
ani1 = pets
ani2 = dogs
ani2.bark()'''

"""class employee:
    salary = 9000
    increment = 1.5

    @property
    def salaryafterincrement(self):
        return salary*increment

    @salaryafterincrement.setter
    def salaryafterincrement(self, sai):
        increment = sai/self.salary

e = employee
print(e.salaryafterincrement)

print(e.increment)
e.salayafterincrement = 10000
print(e.increment)"""

import random
randnumber = random.randint(1,100)
userguess = None
guesses = 0

while(userguess != randnumber):

    try:

        userguess = int(input("Enter your guess: "))
        guesses += 1

        if(userguess == randnumber):
            print("you guessed it right!")

        else:
            if(userguess>randnumber):
                print("you guessed it wrong!, Enter a samaller number")
        
            else:
                print("you guessed it wrong! Enter a larger number")
   
   
    
    except Exception as e:
        print("please enter any valid number: ")

print(f"congratulations!, you guessed the number in {guesses} attempts")





'''with open("code.py/HighScore.txt" , "r") as f:
    HighScore = int(f.read())

if (guesses<HighScore):
    print("Congratulations!, you made a new HighScore")

    with open("code.py/HighScore.txt" , "w") as f:
        f.write(str(guesses))'''


