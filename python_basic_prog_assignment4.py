#!/usr/bin/env python
# coding: utf-8

# # Programming_Assignment4

# In[ ]:


get_ipython().set_next_input('1. Write a Python Program to Find the Factorial of a Number');get_ipython().run_line_magic('pinfo', 'Number')


# In[4]:


def factorial():
    num=int(input("enter the number "))
    fact=1
    for i in range (1,num+1):
        fact=fact*(i)
    print(fact)
factorial()    


# In[ ]:


get_ipython().set_next_input('2. Write a Python Program to Display the multiplication Table');get_ipython().run_line_magic('pinfo', 'Table')


# In[4]:


def table():
    num=int(input("enter the number you want to display multiplication table "))
    for i in range(1,11):
        print(num*i)
table()        


# In[ ]:


get_ipython().set_next_input('3. Write a Python Program to Print the Fibonacci sequence');get_ipython().run_line_magic('pinfo', 'sequence')


# In[7]:


def fibonacci():
    num=int(input("enter the number of term"))
    a=0
    b=1
    if num==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,num):
            c=a+b
            a=b
            b=c
            print(c)
fibonacci()        


# In[ ]:


get_ipython().set_next_input('4. Write a Python Program to Check Armstrong Number');get_ipython().run_line_magic('pinfo', 'Number')


# In[6]:


def armstrong():
    num=int(input("enter the number "))
    temp=num
    sum=0
    while temp>0:
        digit=temp%10
        sum=sum+digit**3
        temp=temp//10
    if sum==num:
        print("Armstrong Number")
    else:
        print("Not a Armstrong Number")
armstrong()        


# In[ ]:


get_ipython().set_next_input('5. Write a Python Program to Find Armstrong Number in an Interval');get_ipython().run_line_magic('pinfo', 'Interval')


# In[2]:


def armstrong():
    lower=int(input("enter the lower number "))
    higher=int(input("enter the higher number "))
    for num in range(lower,higher):
        temp=num
        sum=0
        order=len(str(num))
        while temp>0:
            digit=temp%10
            sum=sum+digit**order
            temp=temp//10
        if sum==num:
            print(num)
        
armstrong()


# In[ ]:


get_ipython().set_next_input('6. Write a Python Program to Find the Sum of Natural Numbers');get_ipython().run_line_magic('pinfo', 'Numbers')


# In[2]:


def naturalsum():
    num=int(input("enter the natural number till were you want sum of numbeer"))
    sum=0
    for i in range(num+1):
        sum=sum+i
    print(sum)    
naturalsum()    

