# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.12.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Homework I 

# ## Question 0 

# ---
# This is *question 0* for [problem set 1](https://jbhender.github.io/Stats507/F21/ps/ps1.html) of [Stats 507](https://jbhender.github.io/Stats507/F21/).
# ```
# Question 0 is about Markdown.
# ```
# The next question is about the **Fibonnaci sequence**, $F_n=F_{n−2}+F_{n−1}$. In part **a** we will define a Python function ```fib_rec()```   
#
# Below is a ...
#
# ### Level 3 Header
# Next, we can make a bulleted list:  
# * Item 1
#     * detail 1
#     * detail 2
# * Item 2
#

# Finally, we can make an enumerated list: 
# 1. Item 1 
# 2. Item 2 
# 3. Item 3 
#
# ---

# ## Question 1

# ### a
# this producing the series with the recurision method and the test is below,
# if the calculation is correct there should be a "True" in the output

def fib_rec(n,a=0,b=1):
    if n==0 :
        return a
    if n==1:
        return b
    else:
        return fib_rec(n-1)+fib_rec(n-2)
print("the Test for F_7: correctly calculated as 13 {} \
        the Test for F_11: correctly calculated as 89 {} \
        the Test for F_13: correctly calculated as 233 {}" \
        .format(fib_rec(7)==13,fib_rec(11)==89,fib_rec(13)==233))


# ### b

# +
def fib_for(n):
    num_zero=0
    num_one=1
    sequencelst=[0,1]
    if n==0 :
        return 0
    if n==1:
        return 1
    else:    
        for i in range(2,n+1):
            sequencelst.append(sequencelst[-1]+sequencelst[-2])
        return sequencelst[-1]
    
print("the Test for F_7: correctly calculated as 13 {} \
        the Test for F_11: correctly calculated as 89 {} \
        the Test for F_13: correctly calculated as 233 {}" \
        .format(fib_for(7)==13,fib_for(11)==89,fib_for(13)==233))


# -

# ### c

# +
def fib_whl(n):
    num_zero=0
    num_one=1
    temp_sum=0
    sequencelst=[0,1]
    i=2
    if n==0 :
        return 0
    if n==1:
        return 1
    else:
        while i <= n :
            temp_sum=num_one+num_zero
            num_zero = num_one
            num_one = temp_sum
            i +=1
        return temp_sum
    
print("the Test for F_7: correctly calculated as 13 {} \
        the Test for F_11: correctly calculated as 89 {} \
        the Test for F_13: correctly calculated as 233 {}" \
        .format(fib_whl(7)==13,fib_whl(11)==89,fib_whl(13)==233))


# -

# ### d

# +
def fib_rnd(n):
    import numpy as np
    phi = 1/2*(np.sqrt(5)+1)
    return round((phi**n/np.sqrt(5)))

print("the Test for F_7: correctly calculated as 13 {} \
        the Test for F_11: correctly calculated as 89 {} \
        the Test for F_13: correctly calculated as 233 {}" \
        .format(fib_rnd(7)==13,fib_rnd(11)==89,fib_rnd(13)==233))


# -

# ### e

# +
def fib_flr(n):
    import numpy as np
    phi = 1/2*(np.sqrt(5)+1)
    return np.floor(phi**n/np.sqrt(5)+1/2)

print("the Test for F_7: correctly calculated as 13 {} \
        the Test for F_11: correctly calculated as 89 {} \
        the Test for F_13: correctly calculated as 233 {}" \
        .format(fib_flr(7)==13,fib_flr(11)==89,fib_flr(13)==233))

# -

# ### f
# first start with comparatively small values form 25 to 30

# +
import datetime
lst= [25,26,27,28,29,30]
# k is the loop time for each value of the n 
k = 10
a = datetime.datetime.now()
temp_lst=[]
tim_lst=[]
for i in lst:
    temp_lst=[i]*k
    for m in temp_lst:
        fib_rec(m)
    b = datetime.datetime.now()
    c = (b - a)/k
    tim_lst.append(c.microseconds)
rec_time=tim_lst

a = datetime.datetime.now()
temp_lst=[]
tim_lst=[]
for i in lst:
    temp_lst=[i]*k
    for m in temp_lst:
        fib_for(m)
    b = datetime.datetime.now()
    c = (b - a)/k
    tim_lst.append(c.microseconds)
for_time=tim_lst

a = datetime.datetime.now()
temp_lst=[]
tim_lst=[]
for i in lst:
    temp_lst=[i]*k
    for m in temp_lst:
        fib_whl(m)
    b = datetime.datetime.now()
    c = (b - a)/k
    tim_lst.append(c.microseconds)
whl_time=tim_lst

a = datetime.datetime.now()
temp_lst=[]
tim_lst=[]
for i in lst:
    temp_lst=[i]*k
    for m in temp_lst:
        fib_rnd(m)
    b = datetime.datetime.now()
    c = (b - a)/k
    tim_lst.append(c.microseconds)
rnd_time=tim_lst

a = datetime.datetime.now()
temp_lst=[]
tim_lst=[]
for i in lst:
    temp_lst=[i]*k
    for m in temp_lst:
        fib_flr(m)
    b = datetime.datetime.now()
    c = (b - a)/k
    tim_lst.append(c.microseconds)
flr_time=tim_lst
# -

# after calculating all the necessary times for different values of n we can put a table to show the result 

import pandas as pd
from itables import show
from IPython.display import display, HTML
data = {'Recursion':rec_time, 'For Loop': for_time, 
        'While Loop': whl_time, 'Rounding': rnd_time, 
        'Truncation': flr_time, 'N':lst}
df=pd.DataFrame(data)
df=df.set_index('N')
display(df)


# It can be shown that the recursive method is considerably slower than the others, paticularly we can see that when n=35 it is significantly slower than any other methods 

import time
lst=[35]
start_time = time.time()
for i in lst:
    fib_rec(i)
time_rec=((time.time() - start_time))
print('the time for recursion method when n=35 is {}s'.format(round(time_rec,2)))

# for the other 4 method we can do some further comparision 

# +
import datetime
lst=[900, 950,1000,1050,1100]

k = 30
a = datetime.datetime.now()
temp_lst=[]
tim_lst=[]
for i in lst:
    temp_lst=[i]*k
    for m in temp_lst:
        fib_for(m)
    b = datetime.datetime.now()
    c = (b - a)/k
    tim_lst.append(c.microseconds)
for_time=tim_lst

a = datetime.datetime.now()
temp_lst=[]
tim_lst=[]
for i in lst:
    temp_lst=[i]*k
    for m in temp_lst:
        fib_whl(m)
    b = datetime.datetime.now()
    c = (b - a)/k
    tim_lst.append(c.microseconds)
whl_time=tim_lst

a = datetime.datetime.now()
temp_lst=[]
tim_lst=[]
for i in lst:
    temp_lst=[i]*k
    for m in temp_lst:
        fib_rnd(m)
    b = datetime.datetime.now()
    c = (b - a)/k
    tim_lst.append(c.microseconds)
rnd_time=tim_lst

a = datetime.datetime.now()
temp_lst=[]
tim_lst=[]
for i in lst:
    temp_lst=[i]*k
    for m in temp_lst:
        fib_flr(m)
    b = datetime.datetime.now()
    c = (b - a)/k
    tim_lst.append(c.microseconds)
flr_time=tim_lst
# -

import pandas as pd
from itables import show
from IPython.display import display, HTML
data = {'For Loop': for_time, 
        'While Loop': whl_time, 'Rounding': rnd_time, 
        'Truncation': flr_time, 'N':lst}
df=pd.DataFrame(data)
df=df.set_index('N')
display(df)


# from the above table we can see that the for loop and the while loop is slower than the other two methods 

# ## Question 2 

# ### a
#
# To create each row of the Pascal’s triangle, we can use the formula that 
# $\begin{pmatrix} n \\ k \end{pmatrix} = \frac{n!}{k!*(n-k)!}$

def pas_row(n):
    import numpy as np 
    string=''
    if n == 1:
        return '1      '
    else:        
        for i in range(n):
            temp_val=np.math.factorial(n-1)/(np.math.factorial(i)*np.math.factorial(n-1-i))
            string = string + str(round(temp_val)) + '       '
        return string


# we can then test and print the 10th row of the triangle 

print(pas_row(10))

# we can create the triangle and print it in this way 

for i in range(1,12):
    print(str(pas_row(i)).center(135))

# ## Question 3

# ### a 
# In this part there will be the point estimation for the mean and confidence interval 

import pandas as pd 
import numpy as np
from itables import show

arry=np.array(range(111))
def ci_cal(array,ci,form='string'):
    import numpy as np
    import scipy.stats        
    if type(array) != type(np.array(1)):
        return 'the Input array should be a numpy array'
    else:
        mu=np.mean(array)
        se=np.std(array,ddof=1)
        k = float(scipy.stats.norm.ppf(1-(1-ci)/2))
        upr = se+ k*se
        lwr = se- k*se
        dic={'est': mu, 
                 'lwr': lwr, 
                 'upr': upr,
                 'level': ci}
        string = '{}[{}%CI:({},{})]'.format(mu,ci,lwr,upr)
        if form == 'string':
            return string
        elif form == 'None': 
            return dic


# #the following is the testing code for the normal approximation  
# test_array=np.random.randint(2,size=100)
# print(binorm(test_array,0.9,'None'))    

# ### b 
# #### i 
# in this part the normal distribution 

def binorm(array,ci,form='string'):
    # first we need to do the testing 
    import numpy as np
    import scipy.stats
    if type(array) != type(np.array(1)):
        return 'the Input array should be a numpy array'
    else: 
        p_hat = np.mean(array)
        n = len(array)
        if np.maximum(n*p_hat,n*(1-p_hat))>12:
            se = np.sqrt(p_hat*(1-p_hat)/n)
            k = float(scipy.stats.norm.ppf(1-(1-ci)/2))
            upr = p_hat+ k*se
            lwr = p_hat- k*se
            dic={'est': p_hat, 
                 'lwr': lwr, 
                 'upr': upr,
                 'level': ci}
            string = '{}[{}% CI:({},{})]'.format(p_hat,round(ci*100),lwr,upr)
            if form == 'string':
                return string
            elif form == 'None': 
                return dic
            else:
                return 'Warning condition not satisfied !!'

# #the following is the testing code for the normal approximation  
# test_array=np.random.randint(2,size=100)
# print(binorm(test_array,0.9))    

# #### ii  
# the Clopper-Person interval 

def binorm_Clopper(array,ci,form='string'):
    import numpy as np
    import scipy.stats
    if type(array) != type(np.array(1)):
        return 'the Input array should be a numpy array'
    else: 
        p_hat = np.mean(array)
        n = len(array)
        alpha = 1-ci
        x = p_hat* n 
        upr = scipy.stats.beta.ppf(1-alpha/2,x+1,n-x)
        lwr = scipy.stats.beta.ppf(alpha/2,x,n-x+1)
        dic={'est': p_hat, 
                'lwr': lwr, 
                'upr': upr,
                'level': ci}
        string = '{}[{}% CI:({},{})]'.format(p_hat,round(ci*100),lwr,upr)
        if form == 'string':
            return string
        elif form == 'None': 
            return dic


# #the following is the testing code for the Clopper method  
# test_array=np.random.randint(2,size=1000000)
# print(binorm_Clopper(test_array,0.9,'none'))    

# #### iii  
# the Jefferey's interval

def binorm_Jeffery(array,ci,form='string'):
    import numpy as np
    import scipy.stats
    if type(array) != type(np.array(1)):
        return 'the Input array should be a numpy array'
    else: 
        p_hat = np.mean(array)
        n = len(array)
        alpha = 1-ci
        x = p_hat* n 
        upr = np.minimum(scipy.stats.beta.ppf(1-alpha/2,x+0.5,n-x+0.5),1)
        lwr = np.maximum(scipy.stats.beta.ppf(alpha/2,x+0.5,n-x+0.5),0)
        dic={'est': p_hat, 
                'lwr': lwr, 
                'upr': upr,
                'level': ci}
        string = '{}[{}%CI:({},{})]'.format(p_hat,round(ci*100),lwr,upr)
        if form == 'string':
            return string
        elif form == 'None': 
            return dic

# #the following is the testing code for the Jeffery method  
# test_array=np.random.randint(2,size=100)
# print(binorm_Clopper(test_array,0.99)) 

# #### iv
# Agresti-Coull interval 

def binorm_Agresti(array,ci,form='string'):
    import numpy as np
    import scipy.stats
    if type(array) != type(np.array(1)):
        return 'the Input array should be a numpy array'
    else: 
        alpha = 1-ci
        n = len(array)
        p_hat = np.mean(array)
        x = p_hat* n 
        
        z= scipy.stats.norm.ppf(1-alpha/2)
        n_tilda= n+z**2
        p_tilda= 1/n_tilda*(x+ z**2/2)
        
        se = np.sqrt(p_tilda*(1-p_tilda)/n_tilda)
        k = float(scipy.stats.norm.ppf(1-(1-ci)/2))
        
        upr = p_tilda+ k*se
        lwr = p_tilda- k*se    
        
        dic={'est': p_tilda, 
                'lwr': lwr, 
                'upr': upr,
                'level': ci}
        string = '{}[{}% CI:({},{})]'.format(p_tilda,round(ci*100),lwr,upr)
        if form == 'string':
            return string
        elif form == 'None': 
            return dic


# #the following is the testing code for the Agrestu-Coull Method  
# test_array=np.random.randint(2,size=10000)
# print(binorm_Agresti(test_array,0.95)) 

# Finally we can define the function that combines all the features mentioned above, it will contain a variable called *method*  
# the method variable will take four different values  
# 1. **norm** for the one using normal distribution
# 2. **clopper** for the Clopper-Pearson interval 
# 3. **jeffery** for the jefferys interval 
# 4. **agresti** for the Agresti-Coull interval 

def binom_approx(array,ci,method,form='string'):
    """
    Parameters
    ----------
    array : i-d numpy array
        this is a One-d array.
    ci : Confidence interval 
        Ci is in [0,1].
    method : string
        there are a total of four methods 
        1. norm
        2. clopper
        3. jeffery
        4. agresti
    form : the form for the output
    Returns a sting 
    -------
    None.

    """
    if method == 'norm':
        return binorm(array,ci,form)
    elif method == 'clopper':
        return binorm_Clopper(array,ci,form)
    elif method == 'jeffery':
        return binorm_Jeffery(array,ci,form)
    elif method == 'agresti':
        return binorm_Agresti(array,ci,form)


# #the following is the testing code for the function  
# test_array=np.random.randint(2,size=100)
# print(binom_approx(test_array,0.9,'norm','None'))

# ### c 
# the comparison 
# firsr we need to create the test 1d array, 
# the following is the 1-d array used for the testing 

test_array = np.array([1]*42 + [0]*48)

# then we can use the above function and define anoter function to generate a sequence of lists 
# the lists are used for the later comparison. 

def lst_generate(method):
    """
    Parameters
    ----------
    method : string
        there are a total of four methods 
        1. norm
        2. clopper
        3. jeffery
        4. agresti
    Returns
    -------
    None.

    """
    array = test_array
    lst=[]
    for ci in [0.9,0.95,0.99]:
        upr=round(binom_approx(array,ci,method,'None')['upr'],4)
        lwr=round(binom_approx(array,ci,method,'None')['lwr'],4)
        width = round(upr-lwr,4)
        lst.append('[{},{}], width {}'.format(lwr,upr,width))
    return lst 

norm_lst=lst_generate('norm')
clopper_lst=lst_generate('clopper')
jeffery_lst=lst_generate('jeffery')
agresti_lst=lst_generate('agresti')

# with all the necessary data we will be able to compare all the different methods in a table  

# +
from IPython.display import display, HTML
from itables import show

df = pd.DataFrame({'Normal':norm_lst, 'Clopper-Pearson': clopper_lst,
                   'Jeffery': jeffery_lst, 'Agresti-Coull': agresti_lst,
                   'CI': ['90 %','95 %','99 %']})
df = df.set_index('CI')
display(df)