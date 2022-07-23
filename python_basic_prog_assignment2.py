

# # Programming_Assignment2

# 1. Write a Python program to convert kilometers to miles?

def convert():
    km=int(input("enter the kilometer  "))
    con=km*0.621371   #1 km = 0.621371 miles
    print('{0} km is equal to miles is {1}'.format(km, con))
convert()    
    


# 2. Write a Python program to convert Celsius to Fahrenheit?

def cel_to_fah():
    cel=float(input("enter the celsius value"))
    fah=(cel*1.8)+32                                 
    print('%.2f celsius is equal %.2f'%(cel,fah))
cel_to_fah()    
    
    


# 3. Write a Python program to display calendar?

import calendar
def calender():
    yy=int(input("enter year in yyyy format")) # year in YYYY
    mm=int(input("enter date in mm format"))   # month in mm
    date=calendar.month(yy, mm)
    print(date)
calender()    


 
# 4. Write a Python program to solve quadratic equation?

import math
def quadequation():  #ax^2+bx+c and a!=0
    a=int(input("enter the value of a "))
    b=int(input("enter the value of b "))
    c=int(input("enter the value of c "))
    dis=b*b-4*a*c
    sqrt1=math.sqrt(abs(dis))
    if dis>0:        # real and distict root
        root1=((-b + sqrt1) / (2 * a))  
        root2=((-b - sqrt1) / (2 * a))
        print('root of the euqtion root1=%.2f root2=%.2f' %(root1,root2))
    elif dis==0:     #real and equal root
        root= (-b / (2 * a))
        print('root of the euqtion root=%.2f'%(root))
    else:    #imaginary root
        root=(- b / (2 * a))
        print(root,'+ j',sqrt1)
        print(root,'- j',sqrt1)
              
quadequation()        


# 5. Write a Python program to swap two variables without temp variable?

def swap():
    first_number=int(input("enter the first number  "))
    second_number=int(input("enter the second number  "))
    first_number=first_number+second_number
    second_number=first_number-second_number
    first_number=first_number-second_number
    print("number after swapping first number " ,first_number)
    print("number after swapping second number " ,second_number)
swap()






