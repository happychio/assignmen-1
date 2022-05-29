#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Assignment 1

This assignment covers your basic profiency with
    Python. It engages your ability to transform
    data without affecting anything outside the program.

This assignment places heavy emphasis on basic Python constructs.
'''    '''Item 1. 
    Factorial. 1 point.
    
    Returns the factorial of an integer.
    An integer's factorial is the product of the integer and all
        integers below it.

    Parameters
    ----------
    x: int
        the integer whose factorial to return

    Returns
    -------
    integer
        the factorial of the argument
    '''
    # Write your code below this line


# In[49]:


def factorial(x):
    num=1
    for i in range (1,x):
        num = x*i
        x = num
    return num


# In[50]:


x= int(input("Enter Number: "))
result = factorial(x)
print(result)
    


# In[48]:


def classify_grade(number_grade):
    '''Item 2.
    Classify Grade. 2 points.
    
    Returns the letter grade equivalent of a number grade.
    For this item, use these letter grade buckets:
        A: 92-100
        B+: 86-91.9
        B: 80-85.9
        C+: 74-79.9
        C: 67-73.9
        D: 60-66.9
        F: 0-59.9

    Parameters
    ----------
    number_grade: float
        the number grade to convert into a letter grade.

    Returns
    -------
    str
        the letter grade equivalent of the number grade.
    '''
    # Write your code below this line


# In[24]:



def classify_grade(number_grade):
    grade="NA"
    
    if number_grade <= 59.9:
        grade = "F"
    elif number_grade <= 66.5:
        grade= "D"
    elif number_grade <= 73.9:
        grade = "C"
    elif number_grade <= 79.9:
        grade = "C+" 
    elif number_grade <= 85.9:
        grade = "B"
    elif number_grade <= 91.9:
        grade = "B+"
    elif number_grade <= 100:
        grade = "A"
        
    
    return grade
    


# In[22]:


number_grade=float(input("Enter Grade: "))
letter= classify_grade(number_grade)
print(letter)


# In[23]:


def average_weight(item_quantity_1, item_weight_1, item_quantity_2, item_weight_2):
    '''Item 3.
    Average Weight. 3 points.
    
    You have purchased two bags of items. 
    The first bag contains one type of item, and the second bag contains another type.
    Return the weighted average weight of the items.
        
    Parameters
    ----------
    item_quantity_1: int
        the quantity of items in the first bag.
    item_weight_1: float
        the weight of each individual item in the first bag.
    item_quantity_2: int
        the quantity of items in the second bag.
    item_weight_2: float
        the weight of each individual item in the second bag.

    Returns
    -------
    float
        the weighted average weight of one item.
    '''
    # Write your code below this line


# In[25]:


def average_weight(item_quantity_1, item_weight_1, item_quantity_2, item_weight_2):
    average = ((item_quantity_1*item_weight_1)+(item_quantity_2* item_weight_2))/(item_quantity_1+item_quantity_2)
    return average


# In[27]:


item_quantity_1= int(input("Enter Item 1 Quantity: "))
item_weight_1= float(input("Enter Item 1 Weight: "))

item_quantity_2= int(input("Enter Item 2 Quantity: "))
item_weight_2= float(input("Enter Item 2 Weight: "))

ave = average_weight(item_quantity_1, item_weight_1, item_quantity_2, item_weight_2)

print(ave)


# In[ ]:


def string_sum(string):
    '''Item 4.
    String Sum. 3 points.
    
    Returns the sum of the digits provided in a string.
    For this item:
        1. Sum the digits contained in the string.
        2. Ignore any non-digit characters contained in the string.

    Parameters
    ----------
    string: str
        a string that can contain any character.

    Returns
    -------
    int
        the sum of the digits contained in the string.
    '''
    # Write your code below this line


# In[58]:


def string_sum(string):
    n = ["0","1","2","3","4","5","6","7","8","9"]
    sum = 0
    length = len(string)
    for i in range (length):
        if string[i] in n:
            sum = int(string[i])+sum
    return sum


# In[59]:


string = str(input("Enter Word: "))
word = string_sum(string)
print(word)


# In[ ]:


def distance(x_1, y_1, x_2, y_2):
    '''Item 5.
    Distance. 3 points.

    Returns the distance between two points.
    To get the distance between two points:
        1. Get the difference between the two x-coordinates
        2. Get the difference between the two y-coordinates
        3. Sum the previous two values
        4. Return the square root of the sum

    You may want to import the `math` library for this number.

    Parameters
    ----------
    x_1: float
        the first x-coordinate
    y_1: float
        the first y-coordinate
    x_2: float
        the second x-coordinate
    y_2: float
        the second y-coordinate

    Returns
    -------
    float
        the distance between the two coordinates
    '''
    # Write your code below this line


# In[64]:


import math
def distance(x_1, y_1, x_2, y_2):
    dif_x = x_1-x_2
    dif_y=y_1-y_2
    sum = abs(dif_x) + abs(dif_y)
    square = math.sqrt(sum)
    
    return square


# In[65]:


x_1= float(input("Enter 1st X-Coordinate: "))
x_2= float(input("Enter 2nd X-Coordinate: "))
y_1= float(input("Enter 1st Y-Coordinate: "))
y_2= float(input("Enter 2nd Y-Coordinate: "))

dist= distance(x_1, y_1, x_2, y_2)
print(dist)


# In[ ]:



def make_change(amount):
'''Item 6.
Make Change. 5 points.

Return the combination of coins needed to make change for the given amount,
    which is given in centavos.
For this item:
    1. You can return 1 peso, 25 centavos, 10 centavos, 5 centavos, and 1 centavo coins.
    2. Use the minimum number of coins possible.

Parameters
----------
amount: int
    the amount, in centavos, to make change for.

Returns
-------
str
    the string representation of the change to be given.
    Format it like this:
        "1P:{amount}/25C:{amount}/10C:{amount}/5C:{amount}/1C:{amount}"
'''
# Write your code below this line


# In[180]:


def make_change(amount):
    piso=0
    quarter=0
    fives=0
    ones=0
    tens=0
 
    piso= amount//1
    amount = amount - piso*1
    piso = str(piso)

    quarter = amount// 0.25
    amount = amount - quarter*0.25
    quarter = str(quarter)

    tens = amount// 0.1
    amount = amount - tens*0.1
    tens = str(tens)

    fives = amount// 0.05
    amount = amount - fives*0.05
    fives = str(fives)

    ones = amount// 0.01
    amount = amount - ones*0.01
    ones = str(ones)
    
    total = "1P:{}/25C:{}/10C:{}/5C:{}/1C:{}".format(piso, quarter,tens,fives,ones)

    return total
      


# In[181]:


amount = float(input("Enter amount: "))
change = make_change(amount)
print(change)


# In[ ]:





# In[ ]:




