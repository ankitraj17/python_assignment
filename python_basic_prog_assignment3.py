

# # Programming_Assignment3

# 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

def checknumber():
    num=int(input("enter the number "))
    if num>0:
        print("the number %.0f entered is positive "%num)
    elif num==0:
        print("the number %.0f entered is zero"%num)
    else:
        print("the number %.0f entered is negative"%num)
checknumber()        


# 2. Write a Python Program to Check if a Number is Odd or Even?

def evenodd():
    num=int(input("enter the number "))
    if num%2==0:
         print("the number %.0f entered is even "%num)
    else:
         print("the number %.0f entered is odd "%num)
evenodd()        
    


# 3. Write a Python Program to Check Leap Year?


def leapyear():
    year=int(input("enter the year in yyyy format "))
    if(year%400==0 and year%100==0):
        print("the year %.0f entered is leap year "%year)
    elif(year%4==0 and year%100!=0):
        print("the year %.0f entered is leap year "%year)
    else:
        print("the year %.0f entered is non leap year "%year)
leapyear()        


# 4. Write a Python Program to Check Prime Number?


def prime():
    num=int(input("enter the number "))
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                print("the number %.0f entered is non prime "%num)
                break
        else:
            print("the number %.0f entered is prime "%num)
            
    else:
        print("the number %.0f entered is non prime "%num)
prime()        


# 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?


def prime():
    for num in range(2,10000):
        if num>1:
            for i in range(2,num):
                if(num%i==0):
                    break
            else:
                print(num)
prime()          







