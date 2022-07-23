
## Programming_Assignment1

# 1. Write a Python program to print "Hello Python"?

# In[4]:


def Hellopython():
    print("Hello Python")
Hellopython()    


# 2. Write a Python program to do arithmetical operations addition and division.?

# In[24]:


def Arthmetical():
    number1=int(input("enter the number1 "))
    number2=int(input("enter the number2 "))
    addition=number1+number2
    division=number1/number2
    print("Addition of two number is ",addition)
    print("Division of two number is ",division)
Arthmetical()    


# 3. Write a Python program to find the area of a triangle?

# In[25]:


def Area():
    base=int(input("enter the base of triangle  "))
    height=int(input("enter the height of triangle  "))
    area=0.5*base*height
    print("Area of triangle is ",area)
Area()    


# 4. Write a Python program to swap two variables?

# In[27]:


def swap():
    first_number=int(input("enter the first number  "))
    second_number=int(input("enter the second number  "))
    temp=first_number
    first_number=second_number
    second_number=temp
    print("number after swapping first number " ,first_number)
    print("number after swapping second number " ,second_number)
swap()
    


# 5. Write a Python program to generate a random number?

# In[23]:


import random
def randomnumber():
    num = random.random()
    print(num)
randomnumber()    





